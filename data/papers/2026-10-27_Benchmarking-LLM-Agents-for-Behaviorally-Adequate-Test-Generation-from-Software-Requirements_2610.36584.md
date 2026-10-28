# Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements

- arXiv ID: `2610.36584v1`
- Authors: Binhang Qi, Yiming Liu, Yun Lin, Yangjie Zhou, Hailong Sun, Jin Song Dong
- Published: 2026-10-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.36584v1) | [pdf](https://arxiv.org/pdf/2610.36584v1)

## Abstract

As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents can generate tests that validate the required behavior when the implementation of that behavior is withheld. Existing test-generation benchmarks mostly focus on white-box testing, whereas the requirement--test-related study usually requires evaluation on semantic alignment between the given documents and the generated tests.
  We introduce Req2Test-Bench, a benchmark containing 5,086 execution-validated instances recovered from developer-authored behavior-driven development (BDD) artifacts in 8 open-source projects, spanning 5 programming languages and 4 BDD frameworks. Each instance pairs a natural-language requirement in Gherkin with its developer-written Test Implementation. Given the requirement, target interfaces of the required behavior, an agent must generate a complete, potentially multi-file Test Implementation. Evaluation of 8 agent--model--reasoning configurations reveals a substantial gap between execution success and behavioral adequacy, which is measured strictly as kill-completeness: a kill-complete test kills every mutant that the ground-truth test kills. The best-performing configuration, Codex with DeepSeek-V4.1-Flash, produces passing tests for 82.8% of instances, yet only 33.8% are behaviorally adequate. We find that (1) scaling up agents yields sharply diminishing returns in behavioral adequacy relative to generation cost; (2) under-specified requirements cause the information gap, including ambiguous setup and implicit expected outcomes; and (3) requirement-grounded harnesses that steer agent non-determinism offer a promising direction for improvement.
