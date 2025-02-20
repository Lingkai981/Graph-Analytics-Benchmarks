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
pip install langchain openai faiss-cpu langchain-openai pydantic

#### Configure the API key
Modify the OpenAI API key in [config.py](LLM-based_usability_evaluation/config.py)
```shell
def get_api_key(self):  
    return "YOUR_API_KEY"  # Replace with your actual API key
```
#### Running the Program
```shell
cd LLM-based_usability_evaluation  
python3 main.py
```
## Performance Evaluation

We provide all algorithm codes used in our paper.

### PowerGraph

PageRank: [PowerGraph/PageRank.sh](Performance%20Evaluation/PowerGraph/PageRank.sh)

SSSP: [PowerGraph/SSSP.sh](Performance%20Evaluation/PowerGraph/SSSP.sh)

Triangle Counting: [PowerGraph/TriangleCounting.sh](Performance%20Evaluation/PowerGraph/TriangleCounting.sh)

Connected Component: [PowerGraph/ConnectedComponent.sh](Performance%20Evaluation/PowerGraph/ConnectedComponent.sh)

Betweenness: [PowerGraph/Betweenness.sh](Performance%20Evaluation/PowerGraph/Betweenness.sh)

LPA: [PowerGraph/LPA.sh](Performance%20Evaluation/PowerGraph/LPA.sh)

K-Core: [PowerGraph/K-Core.sh](Performance%20Evaluation/PowerGraph/K-Core.sh)

K-Clique: [PowerGraph/K-Clique.sh](Performance%20Evaluation/PowerGraph/K-Clique.sh)
