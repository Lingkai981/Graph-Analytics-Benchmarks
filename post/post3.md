# 让你的算法再快一点：隐藏在分布式图计算背后的挑战 —— 全新分布式图计算基准测试被SIGMOD 2025接收

>  近日，GraphScope 团队与上海交通大学林学民教授团队合作的论文《Revisiting Graph Analytics Benchmarks》成功被SIGMOD 2025（2025 ACM International Conference on Management of Data）接收！
SIGMOD作为数据库领域最为优秀的学术会议之一，每年吸引着众多来自学术界和工业界的顶尖研究成果。  

图计算平台通过分布式和多线程的架构，实现了图计算的并行能力。为了评估不同的图计算平台的表现，亟需构建系统化的基准测试体系。现有的主流图基准测试工具，LDBC Graphalytics，使用LDBC-DG生成数据集，并使用六个算法对计算平台进行性能评估。然而，LDBC Graphalytics依然存在一些不足之处：
* 使用的算法不够广泛，缺少子图匹配类型的算法；
* 使用的数据集比较单一，没有充分评测到不同算法和不同平台的瓶颈；
* 使用的评测流程局限于客观的性能指标，缺少对平台本身上手难度的评估。

面对这么多问题，我们如何提供一套尽可能全面且包含主客观评测的新基准评测框架呢？我们的工作在基准算法集的选择，基准数据集以及API易用性的主观评测三个方面实现了突破性的创新。在本文中，我们先介绍在基准算法集和基准数据集中所做的突破性创新。

## 基准算法集：覆盖三大计算模型

分布式计算，其目的是将大规模的数据拆分成若干子数据，交由多台机器并行执行计算任务。一般来说，分布式计算需要有较好的局部特性，来保证较高的计算利用率和较低的通讯消耗。然而，由于图结构本身的随机性，即使最简单的宽度优先遍历算法都很难直接实现分布式计算。因此，目前主流的分布式图计算都依赖于特定的计算模型。

目前，主流的计算模型包括以点为中心（Vertex-Centric）、以边为中心（Edge-Centric）、以块为中心（Block-Centric）和以子图为中心（Subgraph-Centric）等等，他们各自也都擅长不同的算法，大致可以分为三类：
* 迭代算法（Iterative Algorithms），例如PageRank和Label Propagation Algorithm，在每一轮中对所有点或边都需要进行更新，经过一定轮数或结果收敛后中止，以点或边为中心的计算模型（Vertex- and Edge-Centric）擅长迭代算法。
* 顺序算法（Sequential Algorithms），例如Single Source Shortest Path、Weakly Connected Component、Betweenness Centrality和Core Decomposition，存在特定的执行顺序，执行轮数和图的属性相关，比如最短路径SSSP所需要的轮数就是图的直径。如果图的直径很大，会严重影响算法的收敛速度。以分块为中心的计算模型（Block-Centric）可以显著顺序算法的提升效率。
* 子图算法（Subgraph Algorithms），例如Triangle Counting和K-Clique，需要从图中挖掘特定类型的子图。子图算法一般不需要很多的轮数，但是计算量和通讯量往往很大，而基于子图的计算模型（Subgraph-Centric）从底层设计上就对子图算法做了优化。

由于各个计算模式在不同的算法上表现不尽相同，因此基准算法集的选择就显得尤为重要。LDBC Graphalytics共选取了六个算法，但主要集中于社区发现算法和遍历算法，缺少子图分析和匹配算法。作为补充，我们额外增加了Betweenness Centrality、Core Decomposition、Triangle Counting、K-Clique，使得全部八个算法在分类上更加平均。

<div align=center>
<img src=fig1.png width=50% />
</div>

## 基准数据集：精准匹配计算模型的瓶颈

在单机环境下，衡量一个计算平台效率最直接的方法就是实现相同的算法，并测试执行时间。然而在分布式环境下，各个平台都有其对应的实现方式。

以最常见的单源最短路径算法（SSSP）为例，在单机环境中，Dijkstra是最常见也是最高效的算法之一，在采用堆优化之后，复杂度为 $O(m+n\log n)$。然而，Dijkstra算法却很难直接移植到以点为中心和以边为中心的计算平台上，反而只能采用类似于Bellman-Ford的迭代松弛，总计算量最坏可达 $O(nm)$，且同步计算的轮数为 $O(d)$，其中 $d$ 表示图的直径。

可以发现，大量顺序算法在分布式环境中都会引入一个全新的衡量参数——直径。当一个图的直径过大时，即使图本身的规模不变，所花费的时间也会快速增长。同样的，子图算法的执行时间受到子图数量的影响，这一数量可以通过图的密度进行控制。

因此，除了传统意义上的点边数量，在分布式计算中，直径和密度同样是衡量一个图计算困难度的重要指标。然而，目前的主流图生成算法（例如LDBC-DG）却没有考虑到这一点。根据这些问题，我们提出了新的图数据生成器，称为Failure-Free Trial Data Generator（FFT-DG）。

<!-- LDBC-DG的运行流程如下图所示，将所有的点根据生成属性值的相似度排序，然后采样连边，连边概率根据幂律衰减。在LDBC-DG中，采样是依次进行的，即对于点 $i$，不断以 $p^{k}$ 的概率尝试是否与点 $i+k$ 连边，直至达到度的上限。
<div align=center>
<img src=fig2.png width=50% />
</div> -->

### 数据生成器：Failure-Free Trial Data Generator（FFT-DG）

FFT-DG的运行流程如下图所示，将所有的点根据生成属性值的相似度排序，然后采样连边，连边概率根据采样函数衰减。FFT-DG的第一个贡献是采用了反比例函数作为采样函数，点 $i$ 与 $j$ 的连边概率为 $1/[c+(j-i)]$。这一定义有助于快速找到被采样的边。另外，通过缩放参数 $c$ 的比例，可以实现对密度的控制。

<div align=center>
<img src=fig3.png width=50% />
</div>

FFT-DG的第二个贡献是提出了group的概念，将一部分生成边的范围控制在group内部。注意到每个group都会独立地生成边，因此单个group的直径可以认为是固定的且不随group的大小变动，通过调整group的数量即可自由地控制整张图的直径。

<div align=center>
<img src=fig4.png width=50% />
</div>

### 基准数据集及其质量

我们生成如下数据集用于后续评测：

<div align=center>
<img src=fig6.png width=50% />
</div>

另外，我们还使用社区分析算法对真实数据集、FFT-DG生成数据集和LDBC-DG生成数据集进行分析，将图划分成若干社区后统计它们的局部聚类系数、直径和大小，绘制密度分布图。可以看到FFT-DG生成数据集具有更好的相似度，使用JS散度量化后表明，相比于LDBC-DG，FFT-DG和真实数据集的偏移程度减少一倍以上。
<div align=center>
<img src=fig7.png width=50% />
</div>



