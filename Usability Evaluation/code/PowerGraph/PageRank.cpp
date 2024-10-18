#include <vector>
#include <string>
#include <fstream>

#include <test.hpp>
double RESET_PROB = 0.15;

double TOLERANCE = 1.0E-2;

size_t ITERATIONS = 0;

bool USE_DELTA_CACHE = false;

// The vertex data is just the pagerank value (a double)
typedef double vertex_data_type;

// There is no edge data in the pagerank application
typedef test::empty edge_data_type;

typedef test::distributed_graph<vertex_data_type, edge_data_type> graph_type;

void init_vertex(graph_type::vertex_type& vertex) { vertex.data() = 1; }

class pagerank :
  public test::ivertex_program<graph_type, double> {

  double last_change;
public:

  edge_dir_type gather_edges(icontext_type& context,
                              const vertex_type& vertex) const {
    return test::IN_EDGES;
  } // end of Gather edges


  /* Gather the weighted rank of the adjacent page   */
  double gather(icontext_type& context, const vertex_type& vertex,
               edge_type& edge) const {
    return (edge.source().data() / edge.source().num_out_edges());
  }

  /* Use the total rank of adjacent pages to update this page */
  void apply(icontext_type& context, vertex_type& vertex,
             const gather_type& total) {

    const double newval = (1.0 - RESET_PROB) * total + RESET_PROB;
    last_change = (newval - vertex.data());
    vertex.data() = newval;
    if (ITERATIONS) context.signal(vertex);
  }

  /* The scatter edges depend on whether the pagerank has converged */
  edge_dir_type scatter_edges(icontext_type& context,
                              const vertex_type& vertex) const {
    // If an iteration counter is set then
    if (ITERATIONS) return test::NO_EDGES;

    if(USE_DELTA_CACHE || std::fabs(last_change) > TOLERANCE ) {
      return test::OUT_EDGES;
    } else {
      return test::NO_EDGES;
    }
  }

  /* The scatter function just signal adjacent pages */
  void scatter(icontext_type& context, const vertex_type& vertex,
               edge_type& edge) const {
    if(USE_DELTA_CACHE) {
      context.post_delta(edge.target(), last_change);
    }

    if(last_change > TOLERANCE || last_change < -TOLERANCE) {
        context.signal(edge.target());
    } else {
      context.signal(edge.target()); //, std::fabs(last_change));
    }
  }

  void save(test::oarchive& oarc) const {

    if (ITERATIONS == 0) oarc << last_change;
  }

  void load(test::iarchive& iarc) {
    if (ITERATIONS == 0) iarc >> last_change;
  }

}; // end of factorized_pagerank update functor

struct pagerank_writer {
  std::string save_vertex(graph_type::vertex_type v) {
    std::stringstream strm;
    strm << v.id() << "\t" << v.data() << "\n";
    return strm.str();
  }
  std::string save_edge(graph_type::edge_type e) { return ""; }
}; // end of pagerank writer


double map_rank(const graph_type::vertex_type& v) { return v.data(); }


double pagerank_sum(graph_type::vertex_type v) {
  return v.data();
}

int main(int argc, char** argv) {
  // Initialize control plain using mpi
  test::mpi_tools::init(argc, argv);
  test::distributed_control dc;
  global_logger().set_log_level(LOG_INFO);

  // Parse command line options -----------------------------------------------
  test::command_line_options clopts("PageRank algorithm.");
  std::string graph_dir;
  std::string format = "adj";
  std::string exec_type = "synchronous";
  clopts.attach_option("graph", graph_dir,
                       "The graph file.  If none is provided "
                       "then a toy graph will be created");
  clopts.add_positional("graph");
  clopts.attach_option("engine", exec_type,
                       "The engine type synchronous or asynchronous");
  clopts.attach_option("tol", TOLERANCE,
                       "The permissible change at convergence.");
  clopts.attach_option("format", format,
                       "The graph file format");
  size_t powerlaw = 0;
  clopts.attach_option("powerlaw", powerlaw,
                       "Generate a synthetic powerlaw out-degree graph. ");
  clopts.attach_option("iterations", ITERATIONS,
                       "If set, will force the use of the synchronous engine"
                       "overriding any engine option set by the --engine parameter. "
                       "Runs complete (non-dynamic) PageRank for a fixed "
                       "number of iterations. Also overrides the iterations "
                       "option in the engine");
  clopts.attach_option("use_delta", USE_DELTA_CACHE,
                       "Use the delta cache to reduce time in gather.");
  std::string saveprefix;
  clopts.attach_option("saveprefix", saveprefix,
                       "If set, will save the resultant pagerank to a "
                       "sequence of files with prefix saveprefix");

  if(!clopts.parse(argc, argv)) {
    dc.cout() << "Error in parsing command line arguments." << std::endl;
    return EXIT_FAILURE;
  }


  // Enable gather caching in the engine
  clopts.get_engine_args().set_option("use_cache", USE_DELTA_CACHE);

  if (ITERATIONS) {
    // make sure this is the synchronous engine
    dc.cout() << "--iterations set. Forcing Synchronous engine, and running "
              << "for " << ITERATIONS << " iterations." << std::endl;
    clopts.get_engine_args().set_option("type", "synchronous");
    clopts.get_engine_args().set_option("max_iterations", ITERATIONS);
    clopts.get_engine_args().set_option("sched_allv", true);
  }

  // Build the graph ----------------------------------------------------------
  graph_type graph(dc, clopts);
  if(powerlaw > 0) { // make a synthetic graph
    dc.cout() << "Loading synthetic Powerlaw graph." << std::endl;
    graph.load_synthetic_powerlaw(powerlaw, false, 2.1, 100000000);
  }
  else if (graph_dir.length() > 0) { // Load the graph from a file
    dc.cout() << "Loading graph in format: "<< format << std::endl;
    graph.load_format(graph_dir, format);
  }
  else {
    dc.cout() << "graph or powerlaw option must be specified" << std::endl;
    clopts.print_description();
    return 0;
  }
  // must call finalize before querying the graph
  graph.finalize();
  dc.cout() << "#vertices: " << graph.num_vertices()
            << " #edges:" << graph.num_edges() << std::endl;

  // Initialize the vertex data
  graph.transform_vertices(init_vertex);

  // Running The Engine -------------------------------------------------------
  test::omni_engine<pagerank> engine(dc, graph, exec_type, clopts);
  engine.signal_all();
  engine.start();
  const double runtime = engine.elapsed_seconds();
  dc.cout() << "Finished Running engine in " << runtime
            << " seconds." << std::endl;


  const double total_rank = graph.map_reduce_vertices<double>(map_rank);
  std::cout << "Total rank: " << total_rank << std::endl;

  // Save the final graph -----------------------------------------------------
  if (saveprefix != "") {
    graph.save(saveprefix, pagerank_writer(),
               false,    // do not gzip
               true,     // save vertices
               false);   // do not save edges
  }

  double totalpr = graph.map_reduce_vertices<double>(pagerank_sum);
  std::cout << "Totalpr = " << totalpr << "\n";

  // Tear-down communication layer and quit -----------------------------------
  test::mpi_tools::finalize();
  return EXIT_SUCCESS;
} // End of main
