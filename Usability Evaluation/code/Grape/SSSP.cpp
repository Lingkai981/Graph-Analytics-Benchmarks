#ifndef EXAMPLES_ANALYTICAL_APPS_SSSP_SSSP_H_
#define EXAMPLES_ANALYTICAL_APPS_SSSP_SSSP_H_

#include <iomanip>
#include <iostream>
#include <limits>
#include <test/test.h>

namespace test {

/**
 * @brief Context for the parallel version of SSSP.
 *
 * @tparam FRAG_T
 */
template <typename FRAG_T>
class SSSPContext : public VertexDataContext<FRAG_T, double> {
 public:
  using oid_t = typename FRAG_T::oid_t;
  using vid_t = typename FRAG_T::vid_t;

  explicit SSSPContext(const FRAG_T& fragment)
      : VertexDataContext<FRAG_T, double>(fragment, true),
        partial_result(this->data()) {}

  void Init(ParallelMessageManager& messages, oid_t source_id) {
    auto& frag = this->fragment();

    this->source_id = source_id;
    partial_result.SetValue(std::numeric_limits<double>::max());
    curr_modified.Init(frag.Vertices());
    next_modified.Init(frag.Vertices());

#ifdef PROFILING
    preprocess_time = 0;
    exec_time = 0;
    postprocess_time = 0;
#endif
  }

  void Output(std::ostream& os) override {
    // If the distance is the max value for vertex_data_type
    // then the vertex is not connected to the source vertex.
    // According to specs, the output should be +inf
    auto& frag = this->fragment();
    auto inner_vertices = frag.InnerVertices();
    for (auto v : inner_vertices) {
      double d = partial_result[v];
      if (d == std::numeric_limits<double>::max()) {
        os << frag.GetId(v) << " infinity" << std::endl;
      } else {
        os << frag.GetId(v) << " " << std::scientific << std::setprecision(15)
           << d << std::endl;
      }
    }
#ifdef PROFILING
    VLOG(2) << "preprocess_time: " << preprocess_time << "s.";
    VLOG(2) << "exec_time: " << exec_time << "s.";
    VLOG(2) << "postprocess_time: " << postprocess_time << "s.";
#endif
  }

  oid_t source_id;
  typename FRAG_T::template vertex_array_t<double>& partial_result;

  DenseVertexSet<typename FRAG_T::vertices_t> curr_modified, next_modified;

#ifdef PROFILING
  double preprocess_time = 0;
  double exec_time = 0;
  double postprocess_time = 0;
#endif
};

/**
 * @brief SSSP application, determines the length of the shortest paths from a
 * given source vertex to all other vertices in graphs, which can work
 * on both directed and undirected graph.
 *
 * This version of SSSP inherits ParallelAppBase. Messages can be sent in
 * parallel with the evaluation process. This strategy improves the performance
 * by overlapping the communication time and the evaluation time.
 *
 * @tparam FRAG_T
 */
template <typename FRAG_T>
class SSSP : public ParallelAppBase<FRAG_T, SSSPContext<FRAG_T>>,
             public ParallelEngine {
 public:
  // specialize the templated worker.
  INSTALL_PARALLEL_WORKER(SSSP<FRAG_T>, SSSPContext<FRAG_T>, FRAG_T)
  using vertex_t = typename fragment_t::vertex_t;

  /**
   * @brief Partial evaluation for SSSP.
   *
   * @param frag
   * @param ctx
   * @param messages
   */
  void PEval(const fragment_t& frag, context_t& ctx,
             message_manager_t& messages) {
    messages.InitChannels(thread_num());

    vertex_t source;
    bool native_source = frag.GetInnerVertex(ctx.source_id, source);

#ifdef PROFILING
    ctx.exec_time -= GetCurrentTime();
#endif

    ctx.next_modified.ParallelClear(GetThreadPool());

    // Get the channel. Messages assigned to this channel will be sent by the
    // message manager in parallel with the evaluation process.
    auto& channel_0 = messages.Channels()[0];

    if (native_source) {
      ctx.partial_result[source] = 0;
      auto es = frag.GetOutgoingAdjList(source);
      for (auto& e : es) {
        vertex_t v = e.get_neighbor();
        ctx.partial_result[v] =
            std::min(ctx.partial_result[v], static_cast<double>(e.get_data()));
        if (frag.IsOuterVertex(v)) {
          // put the message to the channel.
          channel_0.SyncStateOnOuterVertex<fragment_t, double>(
              frag, v, ctx.partial_result[v]);
        } else {
          ctx.next_modified.Insert(v);
        }
      }
    }

#ifdef PROFILING
    ctx.exec_time += GetCurrentTime();
    ctx.postprocess_time -= GetCurrentTime();
#endif

    messages.ForceContinue();

    ctx.next_modified.Swap(ctx.curr_modified);
#ifdef PROFILING
    ctx.postprocess_time += GetCurrentTime();
#endif
  }

  /**
   * @brief Incremental evaluation for SSSP.
   *
   * @param frag
   * @param ctx
   * @param messages
   */
  void IncEval(const fragment_t& frag, context_t& ctx,
               message_manager_t& messages) {
    auto inner_vertices = frag.InnerVertices();

    auto& channels = messages.Channels();

#ifdef PROFILING
    ctx.preprocess_time -= GetCurrentTime();
#endif

    ctx.next_modified.ParallelClear(GetThreadPool());

    // parallel process and reduce the received messages
    messages.ParallelProcess<fragment_t, double>(
        thread_num(), frag, [&ctx](int tid, vertex_t u, double msg) {
          if (ctx.partial_result[u] > msg) {
            atomic_min(ctx.partial_result[u], msg);
            ctx.curr_modified.Insert(u);
          }
        });

#ifdef PROFILING
    ctx.preprocess_time += GetCurrentTime();
    ctx.exec_time -= GetCurrentTime();
#endif

    // incremental evaluation.
    ForEach(ctx.curr_modified, inner_vertices,
            [&frag, &ctx](int tid, vertex_t v) {
              double distv = ctx.partial_result[v];
              auto es = frag.GetOutgoingAdjList(v);
              for (auto& e : es) {
                vertex_t u = e.get_neighbor();
                double ndistu = distv + e.get_data();
                if (ndistu < ctx.partial_result[u]) {
                  atomic_min(ctx.partial_result[u], ndistu);
                  ctx.next_modified.Insert(u);
                }
              }
            });

    // put messages into channels corresponding to the destination fragments.

#ifdef PROFILING
    ctx.exec_time += GetCurrentTime();
    ctx.postprocess_time -= GetCurrentTime();
#endif
    auto outer_vertices = frag.OuterVertices();
    ForEach(ctx.next_modified, outer_vertices,
            [&channels, &frag, &ctx](int tid, vertex_t v) {
              channels[tid].SyncStateOnOuterVertex<fragment_t, double>(
                  frag, v, ctx.partial_result[v]);
            });

    if (!ctx.next_modified.PartialEmpty(
            frag.Vertices().begin_value(),
            frag.Vertices().begin_value() + frag.GetInnerVerticesNum())) {
      messages.ForceContinue();
    }

    ctx.next_modified.Swap(ctx.curr_modified);
#ifdef PROFILING
    ctx.postprocess_time += GetCurrentTime();
#endif
  }
};

}  // namespace test

#endif  // EXAMPLES_ANALYTICAL_APPS_SSSP_SSSP_H_
