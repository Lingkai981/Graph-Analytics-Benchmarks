# LLM-based usability evaluation

## Overview
This project is a LLM-based usability evaluation framework including an automated code generator and a code evaluator based on large language models (LLMs), supporting multiple graph analysis platforms and common algorithm implementations. The framework uses Retrieval-Augmented Generation (RAG) technology combined with platform API specifications to generate algorithm implementation code that meets specific platform requirements, and provides multi-dimensional code quality evaluation.

## Quick Start

#### Environment Setup
Download Docker image file [llm-eval.tar]()
```shell
# docker pull python:3.10-slim
# docker build -t llm-eval .
docker load -i llm-eval.tar
```
### Running the Program
```shell
docker run --rm \
  -e OPENAI_API_KEY=sk-xxx \
  -e PLATFORM=Ligra \
  -e ALGORITHM=PageRank \
  llm-eval
```

```shell
docker run --rm \
  -e OPENAI_API_KEY=sk-xxx \
  llm-eval Ligra PageRank
```

```shell
docker run -it --rm -e OPENAI_API_KEY=sk-xxx llm-eval
```
