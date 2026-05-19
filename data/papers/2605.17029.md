# Task Abstention for Large Language Models in Code Generation

- arXiv ID: `2605.17029v1`
- Authors: Yanke Zhou, Yuhao Tan, Senrong Xu, Zenan Li, Yuan Yao, Taolue Chen, Xiaoxing Ma
- Published: 2026-05-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.17029v1) | [pdf](https://arxiv.org/pdf/2605.17029v1)

## Abstract

Large language models (LLMs) have revolutionized automated code generation. One serious concern, however, is the so-called ``hallucination'', i.e., LLMs may generate seemingly plausible but functionally incorrect code. In this paper, we study the task abstention problem, i.e., determining whether a given LLM should abstain from performing a specific code generation task to avoid likely hallucination. Our approach features a calibrated abstention rule, grounded in the principles of multiple hypothesis testing. The rule assesses generation consistency through code execution outcomes, allowing it to handle syntactic diversity of semantically equivalent code without reliance on oracle test cases or external databases. We prove that our approach provides a rigorous, distribution-free theoretical guarantee on its abstention decisions. We evaluate our method on benchmark datasets using several open-source code LLMs. Results show that our method allows generative models to more accurately and efficiently identify and abstain from tasks that induce hallucination compared to existing techniques, providing a reliable mechanism for safer and more robust code generation.
