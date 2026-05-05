# Conventional Commit Classification using Large Language Models and Prompt Engineering

- arXiv ID: `2605.02033v1`
- Authors: H. M. Sazzad Quadir, Sakib Al Hasan, Md. Nurul Ahad Tawhid
- Published: 2026-05-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.02033v1) | [pdf](https://arxiv.org/pdf/2605.02033v1)

## Abstract

Conventional commits provide a structured format for writing commit messages, which improves readability, software maintenance, and enables automation tools such as changelog generators and semantic versioning systems. Existing approaches to conventional commit classification typically rely on ML/DL models trained on large labeled datasets. In this paper, we investigated a training-free alternative by leveraging large language models (LLMs) through prompt engineering. Rather than building a task-specific classifier, we evaluate three prompting strategies, such as zero-shot, few-shot, and chain-of-thought, across three open-source LLMs of varying scale: Mistral-7B-Instruct, LLaMA-3-8B, and DeepSeek-R1-32B. Classification is performed directly on code diffs extracted from a balanced dataset of 3,200 commits mined from the InfluxDB repository, without any model fine-tuning. Our results show that few-shot prompting consistently achieves the highest accuracy, while chain-of-thought prompting does not yield additional gains for this classification task. Among the evaluated models, DeepSeek-R1-32B achieves the strongest overall performance, suggesting that model scale plays a meaningful role in conventional commit classification. These findings provide practical guidance for researchers and practitioners seeking to automate commit classification without the overhead of curating and maintaining labeled training data.
