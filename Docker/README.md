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

We also provide a [LDBC-version of our generator](https://github.com/Lingkai981/Graph-Analytics-Benchmarks/tree/e2377e5a5a1e752ed3db44c58b8c95afc80ae030/renewal_datagen) consists of only a few modification.

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
This project is a LLM-based usability evaluation framework including an automated code generator and a code evaluator based on large language models (LLMs), supporting multiple graph analysis platforms and common algorithm implementations. The framework generates algorithm implementation code that meets specific platform requirements, and provides multi-dimensional code quality evaluation.

### Quick Start

#### Environment Setup
Download Docker image file [llm-eval.tar]()
```shell
docker load -i llm-eval.tar
```
#### Running the Program
```shell
docker run --rm \
  -e OPENAI_API_KEY=<your OPENAI_API_KEY> \
  -e PLATFORM=<your platform> \
  -e ALGORITHM=<your algorithm> \
  llm-eval
```
or

```shell
docker run -it --rm -e OPENAI_API_KEY=<your OPENAI_API_KEY> llm-eval
```

## Performance Evaluation
Our performance evaluation setup utilizes 7 graph analysis platforms, both deployed on a Kubernetes cluster using Docker containers. This configuration ensures consistent and reproducible experiments across various scales and configurations.

### Evaluation Environment

- **Cluster**: Kubernetes cluster
- **Containerization**: Docker
- **Job Orchestration**: Kubeflow MPIJob for distributed runs

### Usage

```bash
./run.sh <ALGORITHM> <PATH_TO_DATASET_DIRECTORY>
```
### Platforms and Configurations

1. **FLASH**
   - Docker image: [flash-mpi:v0.3]()
   - Dataset format: Edge list file named `flash-sssp-edges-{SCALE}-{FEATURE}` for the sssp algorithm, such as `flash-sssp-edges-8-Standard`, and named `flash-edges-{SCALE}-{FEATURE}` for the other algorithms, such as `flash-edges-8-Standard`.
   - Supported algorithms: `pagerank`, `sssp`, `triangle`, `lpa`, `k-core-search`, `clique`, `cc`, `bc`.

