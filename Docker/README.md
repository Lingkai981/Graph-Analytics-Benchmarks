# LLM-based usability evaluation

## Overview
This project is a LLM-based usability evaluation framework including an automated code generator and a code evaluator based on large language models (LLMs), supporting multiple graph analysis platforms and common algorithm implementations. The framework generates algorithm implementation code that meets specific platform requirements, and provides multi-dimensional code quality evaluation.

## Quick Start

#### Environment Setup
Download Docker image file [llm-eval.tar]()
```shell
docker load -i llm-eval.tar
```
### Running the Program
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
