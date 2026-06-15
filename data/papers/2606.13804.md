# An Empirical Study of Gemini 3 for Detecting Natural Language Test Smells in Manual Test Cases

- arXiv ID: `2606.13804v1`
- Authors: Keila Lucas, Rohit Gheyi, Márcio Ribeiro, Fabio Palomba, Luana Martins, Elvys Soares
- Published: 2026-06-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.13804v1) | [pdf](https://arxiv.org/pdf/2606.13804v1)

## Abstract

Manual testing, in which testers follow natural language instructions to validate system behavior, remains essential for uncovering issues that are difficult to capture with automation. However, manual test cases often contain test smells, quality issues such as ambiguity, redundancy, or missing checks that reduce reliability, maintainability, and reproducibility. Existing detection approaches largely depend on manually engineered rules and thus struggle to generalize and scale across heterogeneous test suites. In our previous work, we assessed the feasibility of using Small Language Models (SLMs) for test smell detection by evaluating GEMMA-3-4B, LLAMA-3.2-3B, and PHI-4-14B on test steps from 143 real-world Ubuntu test cases, covering seven smell types. PHI-4-14B achieved the best performance. In this article, we investigate whether a contemporary Large Language Model (GEMINI-3-PRO-PREVIEW) available at the time of the study can identify test smells in natural language manual test cases using a prompt-based, whole-test-case analysis strategy. Unlike approaches that analyze individual test steps in isolation, our approach evaluates complete test cases, enabling the model to consider relationships and dependencies among test steps. We evaluate the approach on 100 Ubuntu test cases covering seven test smell types and compare its performance against previously evaluated SLMs, including GEMMA-3-4B, LLAMA-3.2-3B, and PHI-4-14B. Our results show that GEMINI-3-PRO-PREVIEW outperforms the SLMs, while producing actionable explanations that can help practitioners revise manual test cases for greater clarity and consistency. We also find that test smells are pervasive in practice, with nearly one detected test smell per step on average, highlighting the need for scalable and automated quality support for manual testing artifacts.
