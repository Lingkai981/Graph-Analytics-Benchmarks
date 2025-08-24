# Graph-Analytics-Benchmarks
The source code of the paper "Revisiting Graph Analytics Benchmarks"

The appendix content is in file “Benchmark_appendix.pdf”.


## Data Generator

We provide a light cpp program [FFT-DG.cpp](Data_Generator/FFT-DG.cpp) to generate data, which requires three parameters:
>
Scale: The scale of the dataset choosen from $8, 9, 10$. You can also set your preferred scale with a specific size.
Platform: The platform of the dataset to control the output format. You can also set your preferred format.
Feature: The feature of the dataset (*Standard*, *Density* with a higer density, *Diameter* with a larger diameter).

```shell
scale=8
framework="graphx"
g++ FFT-DG.cpp -o generator -O3
./generator $scale $framework Standard
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

### Platforms and Configurations

#### FLASH

- **Docker Image**: [flash-mpi:v0.3]()
- **Dataset Format**: The dataset is organized in folders named according to the following patterns:
  - For the **SSSP** algorithm: `flash-sssp-edges-{SCALE}-{FEATURE}` (e.g., `flash-sssp-edges-8-Standard`)
  - For other algorithms: `flash-edges-{SCALE}-{FEATURE}` (e.g., `flash-edges-8-Standard`)
  
  Each folder contains the following files:
  - `graph.txt`: The graph data in text format.
  - `graph.idx`: The index file for the graph data.
  - `graph.dat`: The data file for the graph.

- **Supported Algorithms**: 
  - `pagerank`
  - `sssp`
  - `triangle`
  - `lpa`
  - `k-core-search`
  - `clique`
  - `cc`
  - `bc`

- **Download Datasets**:  
   Download the relevant dataset folder to every machine where you want to run the algorithms. Ensure the datasets are stored in the **same location** on all machines.
  - [flash-edges-8-Standard]()
  - [flash-edges-9-Standard]()
  - [flash-edges-8-Density]()
  - [flash-edges-9-Density]()
  - [flash-edges-8-Diameter]()
  - [flash-edges-9-Diameter]()
  - [flash-edges-sssp-8-Standard]()
  - [flash-edges-sssp-9-Standard]()
  - [flash-edges-sssp-8-Density]()
  - [flash-edges-sssp-9-Density]()
  - [flash-edges-sssp-8-Diameter]()
  - [flash-edges-sssp-9-Diameter]()

- **Run Flash**:  
   After downloading the datasets, follow these steps to run the algorithm:

   - Go to the Flash directory on the machine.
   - Execute the following command to run the desired algorithm:

     ```bash
     cd Flash
     ./run.sh <ALGORITHM> <PATH_TO_DATASET_DIRECTORY>
     ```

     - `<ALGORITHM>`: Replace with the name of the algorithm you want to run (e.g., `sssp`, `pagerank`, etc.).
     - `<PATH_TO_DATASET_DIRECTORY>`: Provide the path to the directory where the dataset is stored (e.g., `/path/to/flash-sssp-edges-8-Standard`).


