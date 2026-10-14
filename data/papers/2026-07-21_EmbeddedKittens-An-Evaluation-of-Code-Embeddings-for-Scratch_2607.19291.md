# EmbeddedKittens: An Evaluation of Code Embeddings for Scratch

- arXiv ID: `2607.19291v1`
- Authors: Benedikt Fein, Gordon Fraser
- Published: 2026-07-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.19291v1) | [pdf](https://arxiv.org/pdf/2607.19291v1)

## Abstract

The trend of embedding source code for machine learning applications also enables new opportunities in learning analytics in programming education, but which code embedding approach is most suitable for learning analytics remains an open question. A common approach to embedding source code lies in treating the code as a token sequence similar to natural language when training large language models~(LLMs). However, in case of visual block-based programming languages like Scratch, this approach cannot be applied directly. While text-based representations of block-based code can be created to apply LLMs to this problem, other dedicated embedding models could potentially exhibit improved performance by capturing additional structural information. In this paper, we therefore instantiate four LLMs and five different popular embedding approaches for Scratch programs, create a token-prediction and two different classification tasks with corresponding datasets, and empirically evaluate the models on them. Our experiments demonstrate that a transfer of code embeddings to the educational environment of Scratch is feasible. The embedding models trained on large open Scratch datasets capture relevant structural and semantic information about the code to enable learning analytics like predicting functional correctness of student programs, in the typically small classroom setting without requiring further task-specific model fine-tuning.
