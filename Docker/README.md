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

#### Flash

- **Dataset Format**: The dataset is organized in folders named according to the following patterns:
  - For the **sssp** algorithm: `flash-sssp-edges-{SCALE}-{FEATURE}` (e.g., `flash-sssp-edges-8-Standard`)
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

- **Run Flash**:  
   After downloading the datasets, follow these steps to run the algorithm:

   1. Download and load the Docker image [flash-mpi-v0.4.tar]() on all machines.
     ```bash
     sudo docker load -i flash-mpi-v0.4.tar
     ```
   2. On all machines, create identical folders to store datasets. Then, download the following datasets and place them into these folders:
      - [flash-edges-8-Standard]()
      - [flash-edges-9-Standard]()
      - [flash-edges-8-Density]()
      - [flash-edges-9-Density]()
      - [flash-edges-8-Diameter]()
      - [flash-edges-9-Diameter]()
      - [flash-sssp-edges-8-Standard]()
      - [flash-sssp-edges-9-Standard]()
      - [flash-sssp-edges-8-Density]()
      - [flash-sssp-edges-9-Density]()
      - [flash-sssp-edges-8-Diameter]()
      - [flash-sssp-edges-9-Diameter]()

   3. Execute the following command to run the desired algorithm:

     ```bash
     cd Flash
     ./run.sh <ALGORITHM> <PATH_TO_DATASET_FOLDER>
     ```

     - `<ALGORITHM>`: Replace with the name of the algorithm you want to run (e.g., `sssp`, `pagerank`, etc.).
     - `<PATH_TO_DATASET_DIRECTORY>`: Provide the path to the folder where the dataset is stored.
     - The output logs will be generated in the `Flash/output/` folder, with the following naming format:  
       ```
       ${ALGORITHM}-${DATASET_NAME}-n${machines}-p${SLOTS_PER_WORKER}.log
       ```



#### Ligra

- **Dataset Format**:  
  The dataset for Ligra is provided as the `.txt` format.
    - For the **sssp** algorithm: `ligra-sssp-adj-{SCALE}-{FEATURE}.txt` (e.g., `ligra-sssp-adj-8-Diameter.txt`)
    - For other algorithms: `ligra-adj-{SCALE}-{FEATURE}` (e.g., `ligra-adj-8-Diameter.txt`)

- **Supported Algorithms**:  
  - `PageRank`
  - `BellmanFord`
  - `BC`
  - `KCLIQUE`
  - `KCore`
  - `LPA`
  - `Components`
  - `Triangle`

- **Run Ligra**:  
   After downloading the datasets, follow these steps to run the algorithm:

   1. Download and load the Docker image [ligra-mpi-v0.1.tar]() on all machines.
    ```bash
     sudo docker load -i ligra-mpi-v0.1.tar
     ```
   2. On all machines, create identical folders to store datasets. Then, download the following datasets and place them into these folders:
      - [ligra-adj-8-Standard.txt]()
      - [ligra-adj-9-Standard.txt]()
      - [ligra-adj-8-Density.txt]()
      - [ligra-adj-9-Density.txt]()
      - [ligra-adj-8-Diameter.txt]()
      - [ligra-adj-9-Diameter.txt]()
      - [ligra-sssp-adj-8-Standard.txt]()
      - [ligra-sssp-adj-9-Standard.txt]()
      - [ligra-sssp-adj-8-Density.txt]()
      - [ligra-sssp-adj-9-Density.txt]()
      - [ligra-sssp-adj-8-Diameter.txt]()
      - [ligra-sssp-adj-9-Diameter.txt]()
        
   3. Execute the following command to run the desired algorithm:

      ```bash
      cd Ligra
      ./run.sh <ALGORITHM> <PATH_TO_DATASET_FOLDER>
      ```

      - `<ALGORITHM>`: Replace with the name of the algorithm you want to run (e.g., `BellmanFord`, `PageRank`, etc.).
      - `<PATH_TO_DATASET_FOLDER>`: Provide the path to the dataset folder.
      - The output logs will be generated in the `Ligra/output/` folder, with the following naming format:  
       ```
       ${ALGORITHM}-${DATASET_NAME}-n${machines}-p${SLOTS_PER_WORKER}.log
       ```
#### Grape

- **Dataset Format**:  
  Grape uses a simple vertex/edge list format, typically stored in two separate files.
    - Vertex File: A file with a .v extension, where each line represents a vertex ID.
      - Format: for the **sssp** algorithm: `grape-sssp-edges-{SCALE}-{FEATURE}.v` (e.g., `grape-sssp-edges-8-Standard.v`); and for other algorithm: `grape-edges-{SCALE}-{FEATURE}.v` (e.g., `grape-edges-8-Standard.v`).
    - Edge File: A file with a .e extension, where each line represents a directed edge (and optionally, a weight).
      - Format: for the **sssp** algorithm: `grape-sssp-edges-{SCALE}-{FEATURE}.e` (e.g., `grape-sssp-edges-8-Standard.e`); and for other algorithm: `grape-edges-{SCALE}-{FEATURE}.e` (e.g., `grape-edges-8-Standard.e`).
      
- **Supported Algorithms**:  
  - `pagerank`
  - `sssp`
  - `bc`
  - `kclique`
  - `core_decomposition`
  - `cdlp`
  - `wcc`
  - `lcc`

- **Run Grape**:  
   After downloading the datasets, follow these steps to run the algorithm:

   1. Download and load the Docker image [grape-mpi-v0.1.tar]() on all machines.
    ```bash
     sudo docker load -i grape-mpi-v0.1.tar
     ```
   2. On all machines, create identical folders to store datasets. Then, download the following datasets and place them into these folders:
      - [grape-edges-8-Standard.v]()
      - [grape-edges-9-Standard.v]()
      - [grape-edges-8-Density.v]()
      - [grape-edges-9-Density.v]()
      - [grape-edges-8-Diameter.v]()
      - [grape-edges-9-Diameter.v]()
      - [grape-sssp-edges-8-Standard.v]()
      - [grape-sssp-edges-9-Standard.v]()
      - [grape-sssp-edges-8-Density.v]()
      - [grape-sssp-edges-9-Density.v]()
      - [grape-sssp-edges-8-Diameter.v]()
      - [grape-sssp-edges-9-Diameter.v]()
      - [grape-edges-8-Standard.e]()
      - [grape-edges-9-Standard.e]()
      - [grape-edges-8-Density.e]()
      - [grape-edges-9-Density.e]()
      - [grape-edges-8-Diameter.e]()
      - [grape-edges-9-Diameter.e]()
      - [grape-sssp-edges-8-Standard.e]()
      - [grape-sssp-edges-9-Standard.e]()
      - [grape-sssp-edges-8-Density.e]()
      - [grape-sssp-edges-9-Density.e]()
      - [grape-sssp-edges-8-Diameter.e]()
      - [grape-sssp-edges-9-Diameter.e]()
        
   3. Execute the following command to run the desired algorithm:

      ```bash
      cd Ligra
      ./run.sh <ALGORITHM> <PATH_TO_DATASET_FOLDER>
      ```

      - `<ALGORITHM>`: Replace with the name of the algorithm you want to run (e.g., `sssp`, `pagerank`, etc.).
      - `<PATH_TO_DATASET_FOLDER>`: Provide the path to the dataset folder.
      - The output logs will be generated in the `Grape/output/` folder, with the following naming format:  
       ```
       ${ALGORITHM}-${DATASET_NAME}-n${machines}-p${SLOTS_PER_WORKER}.log
       ```
#### Pregel+

- **Dataset Format**:  
  The dataset for Ligra is provided as the `.txt` format.
    - Format: `pregel+-adj-{SCALE}-{FEATURE}.v` (e.g., `pregel+-adj-8-Standard.txt`)
    
- **Supported Algorithms**:  
  - `pagerank`
  - `sssp`
  - `betweenness`
  - `lpa`
  - `clique`
  - `triangle`
  - `cc`

- **Run Grape**:  
   After downloading the datasets, follow these steps to run the algorithm:

   1. Download and load the Docker image [pregel-mpi-v0.1.tar]() on all machines.
    ```bash
     sudo docker load -i pregel-mpi-v0.1.tar
     ```
   2. On all machines, create identical folders to store datasets. Then, download the following datasets and place them into these folders:
      - [pregel+-adj-8-Standard.txt]()
      - [pregel+-adj-9-Standard.txt]()
      - [pregel+-adj-8-Density.txt]()
      - [pregel+-adj-9-Density.txt]()
      - [pregel+-adj-8-Diameter.txt]()
      - [pregel+-adj-9-Diameter.txt]()
        
   3. Execute the following command to run the desired algorithm:
      - **Important**: In file `pregel-mpijob-template.yaml`, `my-hadoop-cluster-hadoop` **must match** the name of the `ConfigMap` you create or reference in your Kubernetes YAML configurations. If the `ConfigMap` is named differently, you will need to update the name in the `volumes` section of the pod definition.

      ```bash
      cd Pregel+
      ./run.sh <ALGORITHM> <PATH_TO_DATASET_FOLDER>
      ```

      - `<ALGORITHM>`: Replace with the name of the algorithm you want to run (e.g., `sssp`, `pagerank`, etc.).
      - `<PATH_TO_DATASET_FOLDER>`: Provide the path to the dataset folder.
      - The output logs will be generated in the `Pregel+/output/` folder, with the following naming format:  
       ```
       ${ALGORITHM}-${DATASET_NAME}-n${machines}-p${SLOTS_PER_WORKER}.log
       ```
