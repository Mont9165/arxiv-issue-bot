# Investigating Software Aging in LLM-Generated Software Systems across Generation-and-Execution Environments

- arXiv ID: `2608.26391v1`
- Authors: Cesar Santos, Michele Vitagliano, Roberto Natella, Ermeson Andrade
- Published: 2026-08-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.26391v1) | [pdf](https://arxiv.org/pdf/2608.26391v1)

## Abstract

Large Language Models (LLMs) are increasingly used to generate executable software systems from natural language specifications, accelerating development and reducing manual implementation effort. Although recent studies have investigated the functional correctness, security, maintainability, and robustness of LLM-generated code, little is known about the long-term reliability of such systems under sustained execution. In this paper, we experimentally investigate software aging symptoms in LLM-generated service-based applications across different programming languages. Using backend scenarios derived from BaxBench, we generated applications targeting JavaScript, Python, and Rust through LLM-based generation platforms, validated them with BaxBench-derived tests, and subjected them to 48-hour workload executions. We monitored memory usage, response time, and throughput and analyzed them using the Mann--Kendall test and Sen's slope estimator. We further complemented the runtime evaluation with static analysis of the generated source code and an exploratory comparison with human-written implementations of related backend scenarios. The results show that memory usage is the most consistent indicator of potential software aging, with statistically significant upward trends in most application-language combinations, while response time and throughput exhibit more heterogeneous behavior. Static analysis identified plausible code-level aging mechanisms, and the comparison with human-written systems showed that aging trends can also emerge in manually developed implementations. These findings indicate that functional correctness alone is insufficient to assess the operational reliability of LLM-generated software before deployment in continuously running environments.
