# LLM-based Mockless Unit Test Generation for Java

- arXiv ID: `2605.26851v1`
- Authors: Qinghua Xu, Guancheng Wang, Lionel Briand, Zhaoqiang Guo, Kui Liu
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.26851v1) | [pdf](https://arxiv.org/pdf/2605.26851v1)

## Abstract

Large language models (LLMs) have shown strong potential for automated test generation, yet most approaches to generating Java unit tests still rely on mocking frameworks to handle dependencies. Mockless test generation could exercise more real low-level code, but it faces challenges such as invalid test code generation due to hallucination, strict language constraints, and inadequate dependency awareness. We identify two causes behind these hallucinations: not knowing, where the LLM lacks sufficient context, and not following, where the LLM fails to comply with constraints even when they are provided.
  We present MocklessTester, a mockless unit test generation approach built around two strategies: context-enriched generation and constraint-enforced fixing. To mitigate not knowing, context-enriched generation mines real usage patterns from existing code to generate tests. To mitigate not following, constraint-enforced fixing performs two-stage repair under symbol-, protocol-, and iteration-level constraints, using a ClassIndex, a Markov typestate model, and experience memory.
  We evaluate MocklessTester against the state-of-the-art baseline on Defects4J and Deps4J. Results show that MocklessTester improves line coverage by 19.99% and 22.69% and branch coverage by 24.90% and 15.78% on the two benchmarks, respectively, and improves mutation score by 13.67% and 0.17%. Beyond the class under test, MocklessTester also exercises more real dependency code, covering 378 and 55 additional lines in dependency classes, respectively. The improvement in test quality comes with higher total token and time costs than the baseline. Nevertheless, the cost per method remains practical, averaging 108.97 seconds and 26.59k tokens on Defects4J, and 69.85 seconds and 25.46k tokens on Deps4J. Ablation results confirm that all major components contribute positively to the final performance.
