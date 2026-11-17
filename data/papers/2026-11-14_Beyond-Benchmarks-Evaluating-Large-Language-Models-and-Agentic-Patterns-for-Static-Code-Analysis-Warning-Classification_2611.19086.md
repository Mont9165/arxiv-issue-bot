# Beyond Benchmarks: Evaluating Large Language Models and Agentic Patterns for Static Code Analysis Warning Classification

- arXiv ID: `2611.19086v1`
- Authors: Lakmal Deshapriya, Sherlock A. Licorish, Brendon J. Woodford, Grant Dick
- Published: 2026-11-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.19086v1) | [pdf](https://arxiv.org/pdf/2611.19086v1)

## Abstract

Context: Static Code Analysis (SCA) tools support software verification and validation, reducing the time and cost of code reviews. However, the best SCA tools in the practitioner community generate a high volume of false positives, which developers tend to ignore, leading to genuine warnings being overlooked. Accordingly, studies increasingly adopt Large Language Models (LLMs) to identify and reduce false positives. Existing studies have produced promising results on public datasets, but underperformed on unseen datasets. Moreover, researchers do not leverage the full potential of Agentic patterns in LLMs or incorporate established code quality standards for warning classification. Objectives: This study utilises four manually annotated datasets to evaluate the performance of three contemporary LLMs for SCA warning classification in real-world applications, and incorporates Agentic patterns and established coding standards to enhance models' performance, addressing gaps identified in existing studies. Method: Three LLMs were selected using the LiveCodeBench benchmark, and the Structured Chain-of-Thought (SCoT) prompting technique was used to evaluate these LLMs. Furthermore, we incorporated Agentic patterns, such as Debating and Self-Consistency, to potentially improve performance in SCA warning classification. Results: Our results show that the performance of different LLMs varies with the characteristics of the dataset, ranging from 0.52 to 0.96 F1-Score for the best models. Additionally, the use of Agentic patterns does not improve LLMs' performance in most scenarios. Conclusions: SCA warning classification using LLMs works best only with certain warning types. We recommend evaluating LLMs in real-world applications rather than using publicly available datasets/benchmarks to understand their full utility.
