# LLM-based usability evaluation

## Overview
This project is a LLM-based usability evaluation framework including an automated code generator and a code evaluator based on large language models (LLMs), supporting multiple graph analysis platforms and common algorithm implementations. The framework uses Retrieval-Augmented Generation (RAG) technology combined with platform API specifications to generate algorithm implementation code that meets specific platform requirements, and provides multi-dimensional code quality evaluation.

## Quick Start

### Environment Setup
```shell
pip install langchain openai faiss-cpu langchain-openai pydantic
```
### Configure the API key in config.py
```shell
def get_api_key(self):
    return "YOUR_API_KEY"  # Replace with your actual API key
```
### Running the Program
```shell
python3 main.py
```
