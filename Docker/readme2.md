# Revisiting Graph Analytics Benchmarks – Open-Source Artifact

> Code and reproducible assets for the paper *“Revisiting Graph Analytics Benchmark”* (J. ACM, 2025).  
> This repo provides: (1) an efficient **Failure‑Free Trial Data Generator (FFT‑DG)**, (2) scripts and assets to **reproduce performance benchmarks** on multiple graph platforms, and (3) an **LLM‑based API usability evaluation** framework.

---

## Table of Contents
- [Overview](#overview)
- [Quick Start](#quick-start)
  - [1) Generate Synthetic Graphs (FFT‑DG)](#1-generate-synthetic-graphs-fft-dg)
  - [2) Run LLM‑based API Usability Evaluation](#2-run-llm-based-api-usability-evaluation)
  - [3) Reproduce Performance Benchmarks](#3-reproduce-performance-benchmarks)
- [Datasets Used in the Paper](#datasets-used-in-the-paper)
- [Supported Algorithms & Platforms](#supported-algorithms--platforms)
- [Project Layout](#project-layout)
- [Cite This Work](#cite-this-work)
- [License](#license)

---

## Overview

This artifact implements the benchmark described in the paper. In short:

- **Core algorithms (8)**: PR, SSSP, LPA, WCC, **BC**, **CD**, **TC**, **KC**.  
- **FFT‑DG**: a flexible, **failure‑free** data generator that lets you control **scale, density, and diameter**.
- **Usability evaluation**: a **multi‑level LLM** framework that scores **compliance**, **correctness**, and **readability** of code produced for each platform.
- **Performance evaluation**: scripts to measure **timing, throughput (edges/s), scalability, and robustness** on 7 platforms.

> The artifact mirrors the paper’s design and terminology for easy cross‑reference.

---

## Quick Start

### 1) Generate Synthetic Graphs (FFT‑DG)

We provide a lightweight C++ program to generate datasets with tunable characteristics:

- `Scale`: dataset size (`8`, `9`, `10` … or a custom size).
- `Platform`: target platform (controls output format).
- `Feature`: `{Standard | Density | Diameter}`.

```bash
cd Data_Generator
g++ FFT-DG.cpp -O3 -o generator

# Example
scale=8
platform="graphx"
./generator $scale $platform Standard
```

> We also provide an [LDBC‑style variant of the generator](https://github.com/Lingkai981/Graph-Analytics-Benchmarks/tree/e2377e5a5a1e752ed3db44c58b8c95afc80ae030/renewal_datagen) with minimal modifications.

### 2) Run LLM‑based API Usability Evaluation

This framework generates platform‑specific implementations and scores them.

**Prerequisites**
- Docker
- `OPENAI_API_KEY` (environment variable)

**Load the image and run:**

```bash
docker load -i llm-eval.tar

# One‑shot run
docker run --rm   -e OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>   -e PLATFORM=<platform>   -e ALGORITHM=<algorithm>   llm-eval

# Interactive
docker run -it --rm -e OPENAI_API_KEY=<YOUR_OPENAI_API_KEY> llm-eval
```

### 3) Reproduce Performance Benchmarks

Our experiments use Dockerized jobs (e.g., via Kubernetes/Kubeflow for distributed runs) to ensure reproducibility across scales and configurations. See platform‑specific instructions in the corresponding subfolders (e.g., `Flash/`, `Grape/`, `Ligra/`).

---

## Datasets Used in the Paper

All datasets are **edge lists** unless otherwise noted.

| Name | Link |
| --- | --- |
| S8‑Std | https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-8-Standard.txt |
| S8‑Density | https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-8-Density.txt |
| S8‑Diameter | https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-8-Diameter.txt |
| S9‑Std | https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-9-Standard.txt |
| S9‑Density | https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-9-Density.txt |
| S9‑Diameter | https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-9-Diameter.txt |
| S10‑Std | https://graphscope.oss-cn-beijing.aliyuncs.com/benchmark_datasets/graphx-edges-10-Standard.txt |

> Notes  
> • “Density” has higher edge density; “Diameter” produces larger graph diameters.  
> • Platform‑specific formats (e.g., Flash/Grape/Ligra) and zipped bundles are listed in each platform’s README under its folder.

---

## Supported Algorithms & Platforms

**Algorithms (8):**
- `pagerank`, `sssp`, `lpa`, `wcc`, `bc`, `core_decomposition`, `triangle` (TC), `kclique` (KC)

**Platforms (7):**
- GraphX, PowerGraph, Flash, Grape, Pregel+, Ligra, G‑thinker

See platform subfolders for inputs, supported algorithms, and run scripts.

---

## Project Layout

```
.
├── Data_Generator/
│   └── FFT-DG.cpp             # Failure-Free Trial Data Generator
├── Flash/                     # Flash platform configs & run scripts
├── Grape/                     # Grape platform configs & run scripts
├── Ligra/                     # Ligra platform configs & run scripts
├── ... (other platforms)
├── llm-eval.tar               # Docker image for usability evaluation (downloaded)
├── Benchmark_appendix.pdf     # Appendix referenced by the paper
└── README.md                  # This file
```

---

## Cite This Work

If you use this artifact, please cite the paper:

```bibtex
@article{meng2025revisiting_graph_analytics_benchmark,
  title   = {Revisiting Graph Analytics Benchmark},
  author  = {Lingkai Meng and Yu Shao and Long Yuan and Longbin Lai and Peng Cheng and Xue Li and Wenyuan Yu and Wenjie Zhang and Xuemin Lin and Jingren Zhou},
  journal = {Journal of the ACM},
  year    = {2025},
  volume  = {37},
  number  = {4},
  pages   = {Article 111},
  note    = {Artifact: Graph-Analytics-Benchmarks}
}
```

---

## License

TBD (add your license here, e.g., Apache-2.0 or MIT).
