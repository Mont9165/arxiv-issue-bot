# On the risk of coding before testing: An empirical study on LLM-based test generation workflow

- arXiv ID: `2607.05139v1`
- Authors: Michael Konstantinou, Florian Tambon, Mike Papadakis
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05139v1) | [pdf](https://arxiv.org/pdf/2607.05139v1)

## Abstract

Large Language Models (LLMs) are increasingly used in software engineering workflows to generate both source code and test suites. This dual capability has enabled emerging development paradigms, including test-first and agentic workflows, where a single model is producing and validating implementations. However, these approaches assume that generated tests act as independent and reliable oracles - a fundamental requirement for effective software testing. In this paper, we challenge this assumption and investigate whether LLM-generated code biases the generation of subsequent tests. We introduce and empirically study the phenomenon of error propagation, where faults in generated code are systematically replicated in associated test artifacts. This leads to cases where incorrect implementations and tests are mutually consistent, masking defects rather than revealing them. We evaluate this effect across a range of programming tasks and agentic workflows, analyzing the consistency between generated code and test assertions, with particular focus on scenarios of aligned failures. Our study examines (i) whether erroneous code artifacts bias test generation, (ii) whether such bias persists under different prompting strategies, including chain-of-thought reasoning, and (iii) how errors propagate across multi-step workflows in which intermediate outputs are reused as context. The results show that error propagation is prevalent and impactful: generating tests after faulty code significantly reduces fault detection effectiveness compared to generating tests independently (14% vs. 25%). These findings highlight a fundamental limitation of current workflows, where lack of independence between generated artifacts undermines the reliability of automated testing. Furthermore, our results expose a previously underexplored threat to validity in empirical studies relying on coupled generation pipelines.
