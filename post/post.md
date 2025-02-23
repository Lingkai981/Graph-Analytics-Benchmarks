# Revisiting Graph Analytics Benchmark：再探图计算基准测试

## 背景

图计算平台通过分布式和多线程的架构，实现了图计算的并行能力。不同于传统的单线程算法，图计算平台将任务拆解到点、边或子图上，大大提高了图计算的可扩展性。为了比较不同的图计算平台的性能，需要一个基准测试对图计算平台进行评估。

由于图结构本身的随机性，不同的平台对于不同的图算法支持能力有很大差异，也有一些图计算平台针对特定任务进行优化。目前，最主流的图计算聚准测试为LDBC Graphalytics，它使用LDBC-DG生成数据集，并使用六个算法对计算平台进行评估。

然而，LDBC Graphalytics依然存在一些不足之处：
* 使用的算法不够广泛，缺少子图匹配类型的算法；
* 使用的数据集比较单一，没有充分评测到不同算法和不同平台的瓶颈；
* 使用的评测流程局限于客观的性能指标，缺少对平台本身上手难度的评估。

基于这些问题，我们在LDBC Graphalytics的基础上做了大量的更新和补充。

## 基准算法集
LDBC Graphalytics共选取了六个算法，分别是PageRank、Label Propagation Algorithm、Single Source Shortest Path，Weakly Connected Component、Breadth First Search、Local clustering coefficient，集中于社区发现算法和遍历算法，缺少子图分析和匹配算法。

作为补充，我们额外增加了Betweenness Centrality、Core Decomposition、Triangle Counting、K-Clique，全部八个算法在分类上更加平均。

<div align=center>
<img src=fig1.png width=50% />
</div>

此外，我们还进一步将算法分成三大类：
* 迭代算法（Iterative Algorithms），例如PageRank和LPA，在每一轮中对所有点或边都需要进行更新，经过一定轮数或结果收敛后中止，以点或边为中心的计算模型（vertex- and edge-centric）擅长迭代算法。
* 顺序算法（Sequential Algorithms），例如SSSP、WCC、BC和CD，存在特定的执行顺序，执行轮数和图的属性相关，比如最短路径SSSP所需要的轮数就是图的直径。如果图的直径很大，会严重影响算法的收敛速度。以分块为中心的计算模型（block-centric）可以显著顺序算法的提升效率。
* 子图算法（Subgraph Algorithms），例如TC和KC，需要从图中挖掘特定类型的子图。子图算法一般不需要很多的轮数，但是计算量和通讯量往往很大，而基于子图的计算模型（subgraph-centric）从底层设计上就对子图算法做了优化。

可以看到这八个算法同样均匀的覆盖了常见的计算模型，能更公平地评估计算平台的能力。


## 基准数据集

LDBC Graphalytics使用LDBC-DG作为数据生成器，能够仿造社交网络生成任意规模的数据。然而，LDBC-DG存在两个问题：
* 生成图的属性比较固定，无法自由设置图的一些参数，例如直径和密度，而这两个参数对图计算的任务负载有直接的影响；
* 生成过程中的采样效率较低，且无法生成稀疏图。

根据这些问题，我们提出了新的图数据生成器，称为Failure-Free Trial Data Generator（FFT-DG）。

### Failure-Free Trial Data Generator

LDBC-DG的运行流程如下图所示，将所有的点根据生成属性值的相似度排序，然后采样连边，连边概率根据幂律衰减。在LDBC-DG中，采样是依次进行的，即对于点 $i$，不断以 $p^{k}$ 的概率尝试是否与点 $i+k$ 连边，直至达到度的上限。
<div align=center>
<img src=fig2.png width=50% />
</div>

而FFT-DG采用了反比例函数作为采样概率，通过公式计算后即可快速确定下一条被采样的边，无需继续依次采样。
<div align=center>
<img src=fig3.png width=50% />
</div>

<!-- 具体来说，边 $(i, j)$ 是下一条被采样的边的概率是：
$$
\begin{aligned}
	\Pr[e(i, j)] &= \left(1 - \frac{1}{c + 1}\right) \cdot \left(1 - \frac{1}{c + 2}\right) ... \frac{1}{c + (j - i)} \\
	&= \frac{c}{c + (j-i-1)} - \frac{c}{c + (j-i)}
\end{aligned}
$$

注意到所有边的概率都可以首尾相接地映射到0~1的区间上，因此只需要随机生成一个浮点数 $f$ 即可代表采样的边：
$$
j = i + \left\lfloor \left(\frac{1}{f} - 1 \right) \cdot c \right\rfloor + 1
$$
对于后续的采样同理，假设已经得到了边 $(i,j)$，只需令 $c'=c + (j-i)$，就可以得到相同的形式：
$$
\begin{aligned}
	\Pr[e(i, k)] &= \left(1 - \frac{1}{c + (j - i) + 1}\right) \cdot \left(1 - \frac{1}{c + (j - i) + 2}\right) ... \frac{1}{c + (k - i)} \\
	&= \frac{c + j - i}{c + (k-i-1)} - \frac{c + j - i}{c + (k-i)} \\
    &= \frac{c'}{c' + (k-j-1)} - \frac{c'}{c' + (k-j)}
\end{aligned}
$$
同样可以映射到0~1的区间的上。 -->


接着，为了控制图的密度，可以在采样时按比例缩小 $c$ 使得边的生成更加密集。也可以在采样时通过将边的范围控制在某个范围内（称为group）来控制图的直径。
<div align=center>
<img src=fig4.png width=50% />
</div>

我们使用社区分析算法对真实数据集、FFT-DG生成数据集和LDBC-DG生成数据集进行分析，将图划分成若干社区后统计它们的局部聚类系数、直径和大小，绘制密度分布图。可以看到FFT-DG生成数据集具有更好的相似度，使用JS散度量化后表明，相比于LDBC-DG，FFT-DG和真实数据集的偏移程度减少一倍以上。
<div align=center>
<img src=fig7.png width=50% />
</div>



最后我们生成如下数据集用于后续评测：
<div align=center>
<img src=fig6.png width=50% />
</div>


## 易用性评测
<div align=center>
<img src=fig11.png width=100% />
</div>
在现代图计算平台的开发中，API易用性一直是影响开发者体验和平台广泛应用的重要因素。API的设计决定了开发者的学习曲线、工作效率及代码的可维护性。然而，现有的API易用性基准测试方法存在诸多局限，尤其是在图计算平台的API评估中，往往忽视了这一重要维度。为此，我们提出了一种全新的基于大语言模型（LLM）的API易用性基准测试框架，旨在通过自动化评估，解决现有方法中的成本高、可扩展性差等问题。

### 基于大语言模型的API易用性评估框架
我们提出的多级LLM可用性评估框架，模拟不同水平的程序员（初级、中级、高级、专家），通过分析生成的代码质量来评估不同平台API的可用性。具体步骤包括：


## 实验设置

我们选取七个常用的图计算平台进行测试，包括：
* GraphX（GX）
* PowerGraph（PG）
* Flash（FL）
* Grape（GR）
* Pregel+（PP）
* Ligra（LI）
* G-Thinker（GT）

实验集群由16台物理机组成，每台机器包括4张Intel Xeon Platinum 8163 CPU，512GB内存，3TB的硬盘存储。所有机器通过局域网通讯，带宽为15Gbps。

## 实验结果

首先我们对八个算法进行评测。这里采用单机多线程模式，减少由于多机通讯所带来的误差。除了这些平台原始提供的算法，我们尽量寻找可用的第三方代码或自行实现。剩余算法无法实现的原因包括，G-Thinker仅支持子图算法，Pregel+不支持多次执行任务（Core Decomposition）。此外，红框部分算法由于效率较差，采用16机运行作为替代。

可以看到，即使三个数据集拥有接近的大小，其不同的数据分布也会在一些算法上呈现出不同的结果。因此，针对不同的算法使用不同分布的数据集进行测试是有意义的。

<div align=center>
<img src=fig8.png width=100% />
</div>

可扩展性的测试也体现出不同数据集的特点。稠密图相对稀疏图有更好的扩展性，而直径对扩展性的影响则随算法和平台而异。此外，图算法整体在多机多线程模式上的扩展性远不如单机多线程，一方面是由于图计算本身的困难性，导致很快达到扩展性上限，另一方面多机带来的额外通讯开销也使得效率大大降低，也更难以优化。

<div align=center>
<img src=fig9.png width=100% />
</div>





最后，我们利用雷达图来完整地可视化整体评测结果：
<div align=center>
<img src=fig10.png width=75% />
</div>
