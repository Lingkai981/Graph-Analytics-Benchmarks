# Graph-Analytics-Benchmarks
The source code of the paper "Revisiting Graph Analytics Benchmarks"

The appendix content is in file “Benchmark_appendix.pdf”.


## Data Generator

We provide a light cpp program `FFT-DG.cpp` to generate data, which requires three parameters:
>
Scale: The scale of the dataset choosen from $8, 9, 10$. You can also set your preferred scale with a specific size.
Platform: The platform of the dataset to control the output format. You can also set your preferred format.
Feature: The feature of the dataset (*Standard*, *Density* with a higer density, *Diameter* with a larger diameter).

```shell
Scale=8
Platform="graphx"
Feature="Standard"
g++ generator.cpp -o generator -O3
./generator $Scale $Platform $Feature
```

We also provide a LDBC-version of our generator consists of only a few modification.

To easy startup, here is the datasets used in our evalution. The format of these datasets are edge list, i.e., each line is a single edge.

[S8-Std](
https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-8-Standard.txt), 
[S8-Denisty](
https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-8-Density.txt),
[S8-Diameter](
https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-8-Diameter.txt),
[S9-Std](
https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-9-Standard.txt), 
[S9-Denisty](
https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-9-Density.txt),
[S9-Diameter](
https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-9-Diameter.txt),
[S10-Std](
https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-10-Standard.txt),

## LLM-based usability evaluation

### Overview
This project is a LLM-based usability evaluation framework including an automated code generator and a code evaluator based on large language models (LLMs), supporting multiple graph analysis platforms and common algorithm implementations. The framework uses Retrieval-Augmented Generation (RAG) technology combined with platform API specifications to generate algorithm implementation code that meets specific platform requirements, and provides multi-dimensional code quality evaluation.

### Quick Start

#### Environment Setup
```shell
pip install langchain openai faiss-cpu langchain-openai pydantic
```
#### Set the OpenAI API key as an environment variable:
Open your terminal and add the following line to your shell configuration file (.bashrc, .zshrc, etc.):
```shell
export OPENAI_API_KEY="your-api-key-here"
```
Reload the shell configuration:
```shell
source ~/.bashrc   # If you use bash
source ~/.zshrc    # If you use zsh
```
#### Running the Program
```shell
cd LLM-based_usability_evaluation  
python3 main.py
```
## Performance Evaluation

We provide all algorithm codes used in our paper.

### GraphX

#### Platform Source Code

[Spark]

#### ALgorithms

1. run `pack.sh` locally to compile the `.scala` file and pack up as a `.jar`
2. copy and run the `.jar` file with Spark

Algorithms

### PowerGraph

#### Platform Source Code

[PowerGraph](https://github.com/jegonzal/PowerGraph)

#### Algorithms

1. add the `.cpp` file to PowerGraph/toolkits/graph_analytics (some are already existed)
2. add commands in PowerGraph/toolkits/graph_analytics/CMakeLists.txt
3. compile and run by the platform guidance

PageRank: [[Code]](Performance%20Evaluation/PowerGraph/PageRank.cpp) [[Command]](Performance%20Evaluation/PowerGraph/PageRank.sh)

SSSP: [[Code]](Performance%20Evaluation/PowerGraph/SSSP.cpp) [[Command]](Performance%20Evaluation/PowerGraph/SSSP.sh)

Triangle Counting: [[Code]](Performance%20Evaluation/PowerGraph/TriangleCounting.cpp) [[Command]](Performance%20Evaluation/PowerGraph/TriangleCounting.sh)

Connected Component: [[Code]](Performance%20Evaluation/PowerGraph/ConnectedComponent.cpp) [[Command]](Performance%20Evaluation/PowerGraph/ConnectedComponent.sh)

Betweenness: [[Code]](Performance%20Evaluation/PowerGraph/Betweenness.cpp) [[Command]](Performance%20Evaluation/PowerGraph/Betweenness.sh)

LPA: [[Code]](Performance%20Evaluation/PowerGraph/LPA.cpp) [[Command]](Performance%20Evaluation/PowerGraph/LPA.sh)

K-Core: [[Code]](Performance%20Evaluation/PowerGraph/K-Core.cpp)
[[Command]](Performance%20Evaluation/PowerGraph/K-Core.sh)

K-Clique: [[Code]](Performance%20Evaluation/PowerGraph/K-Clique.cpp) [[Command]](Performance%20Evaluation/PowerGraph/K-Clique.sh)

### Ligra

#### Platform Source Code

[Ligra](https://github.com/jshun/ligra)

#### Algorithms

1. add the `.C` file to ligra/apps/ (some are already existed)
2. update the file name in ligra/apps/Makefile
```shell
ALL= <file name>
```
3. update the number of threads in the algorithm file
```shell
setWorkers(Number_of_Threads);
```
4. add `.sh` file in ligra/apps/
5. compile and run by the platform guidance

PageRank: [[Code]](Performance%20Evaluation/Ligra/PageRank.C) [[Command]](Performance%20Evaluation/Ligra/PageRank.sh)

SSSP: [[Code]](Performance%20Evaluation/Ligra/SSSP.C) [[Command]](Performance%20Evaluation/Ligra/SSSP.sh)

Triangle Counting: [[Code]](Performance%20Evaluation/Ligra/TriangleCounting.C) [[Command]](Performance%20Evaluation/Ligra/TriangleCounting.sh)

Connected Component: [[Code]](Performance%20Evaluation/Ligra/ConnectedComponent.C) [[Command]](Performance%20Evaluation/Ligra/ConnectedComponent.sh)

Betweenness: [[Code]](Performance%20Evaluation/Ligra/Betweenness.C) [[Command]](Performance%20Evaluation/Ligra/Betweenness.sh)

LPA: [[Code]](Performance%20Evaluation/Ligra/LPA.C) [[Command]](Performance%20Evaluation/Ligra/LPA.sh)

K-Core: [[Code]](Performance%20Evaluation/Ligra/K-Core.C)
[[Command]](Performance%20Evaluation/Ligra/K-Core.sh)

K-Clique: [[Code]](Performance%20Evaluation/Ligra/K-Clique.C) [[Command]](Performance%20Evaluation/Ligra/K-Clique.sh)

### Flash

#### Platform Source Code

[Flash](https://github.com/alibaba/libgrape-lite/tree/flash)

#### Algorithms

1. add the `.cpp` file to flash/src/apps/ (some are already existed)
2. add `flash2.h` file to flash/src/core/
3. add `.sh` file in flash/run/
4. compile and run by the platform guidance

PageRank: [[Code]](Performance%20Evaluation/Flash/PageRank.cpp) [[Command]](Performance%20Evaluation/Flash/PageRank.sh)

SSSP: [[Code]](Performance%20Evaluation/Flash/SSSP.cpp) [[Command]](Performance%20Evaluation/Flash/SSSP.sh)

Triangle Counting: [[Code]](Performance%20Evaluation/Flash/TriangleCounting.cpp) [[Command]](Performance%20Evaluation/Flash/TriangleCounting.sh)

Connected Component: [[Code]](Performance%20Evaluation/Flash/ConnectedComponent.cpp) [[Command]](Performance%20Evaluation/Flash/ConnectedComponent.sh)

Betweenness: [[Code]](Performance%20Evaluation/Flash/Betweenness.cpp) [[Command]](Performance%20Evaluation/Flash/Betweenness.sh)

LPA: [[Code]](Performance%20Evaluation/Flash/LPA.cpp) [[Command]](Performance%20Evaluation/Flash/LPA.sh)

K-Core: [[Code]](Performance%20Evaluation/Flash/K-Core.cpp)
[[Command]](Performance%20Evaluation/Flash/K-Core.sh)

K-Clique: [[Code]](Performance%20Evaluation/Flash/K-Clique.cpp) [[Command]](Performance%20Evaluation/Flash/K-Clique.sh)

### Grape

#### Platform Source Code

[Grape](https://github.com/alibaba/libgrape-lite)

#### Algorithms

1. add the algorithm file to libgrape-lite/examples/analytical_apps/ (some are already existed)
2. add `.sh` file in libgrape-lite/build/
3. update `libgrape-lite/CMakeLists.txt` file
4. compile and run by the platform guidance

PageRank: [[Code]](Performance%20Evaluation/Grape/pagerank/) [[Command]](Performance%20Evaluation/Grape/PageRank.sh)

SSSP: [[Code]](Performance%20Evaluation/Grape/sssp/) [[Command]](Performance%20Evaluation/Grape/SSSP.sh)

Triangle Counting: [[Code]](Performance%20Evaluation/Grape/lcc/) [[Command]](Performance%20Evaluation/Grape/TriangleCounting.sh)

Connected Component: [[Code]](Performance%20Evaluation/Grape/wcc/) [[Command]](Performance%20Evaluation/Grape/ConnectedComponent.sh)

Betweenness: [[Code]](Performance%20Evaluation/Grape/bc/) [[Command]](Performance%20Evaluation/Grape/Betweenness.sh)

LPA: [[Code]](Performance%20Evaluation/Grape/cdlp/) [[Command]](Performance%20Evaluation/Grape/LPA.sh)

K-Core: [[Code]](Performance%20Evaluation/Grape/core_decomposition/)
[[Command]](Performance%20Evaluation/Grape/K-Core.sh)

K-Clique: [[Code]](Performance%20Evaluation/Grape/kclique/) [[Command]](Performance%20Evaluation/Grape/K-Clique.sh)


### Pregel+

#### Platform Source Code

[Pregel+](https://github.com/yaobaiwei/PregelPlus)

#### Algorithms


2. add `.sh` file in the algorithm folder provided
3. update the input file path in `run.cpp`
4. compile and run by the platform guidance

PageRank: [[Code]](Performance%20Evaluation/Pregel+/pagerank/) [[Command]](Performance%20Evaluation/Pregel+/PageRank.sh)

SSSP: [[Code]](Performance%20Evaluation/Pregel+/sssp/) [[Command]](Performance%20Evaluation/Pregel+/SSSP.sh)

Triangle Counting: [[Code]](Performance%20Evaluation/Pregel+/triangle/) [[Command]](Performance%20Evaluation/Pregel+/TriangleCounting.sh)

Connected Component: [[Code]](Performance%20Evaluation/Pregel+/cc/) [[Command]](Performance%20Evaluation/Pregel+/ConnectedComponent.sh)

Betweenness: [[Code]](Performance%20Evaluation/Pregel+/betweenness/) [[Command]](Performance%20Evaluation/Pregel+/Betweenness.sh)

LPA: [[Code]](Performance%20Evaluation/Pregel+/lpa/) [[Command]](Performance%20Evaluation/Pregel+/LPA.sh)

K-Clique: [[Code]](Performance%20Evaluation/Pregel+/clique/) [[Command]](Performance%20Evaluation/Pregel+/K-Clique.sh)
