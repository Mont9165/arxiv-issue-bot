# DryRUN: On the Role of Public Tests in LLM-Driven Code Generation

- arXiv ID: `2604.21598v1`
- Authors: Kaushitha Silva, Srinath Perera
- Published: 2026-04-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.21598v1) | [pdf](https://arxiv.org/pdf/2604.21598v1)

## Abstract

Multi-agent frameworks are widely used in autonomous code generation and have applications in complex algorithmic problem-solving. Recent work has addressed the challenge of generating functionally correct code by incorporating simulation-driven planning and debugging, where language models trace execution steps to verify logic. However, these approaches depend on human-provided public test cases to ground the debugging and simulation loop. Manually authoring comprehensive input-output examples is a labor-intensive bottleneck in the software development lifecycle. Because ground-truth input-output examples are rarely available prior to implementation in real-world software engineering, this dependency restricts methods to curated competitive programming benchmarks. Furthermore, we identify that reliance on these public tests induces an ``overconfidence gap,'' causing frameworks to overfit to simplistic examples and fail on hidden evaluations. In contrast, we observe that external sample inputs are not strictly necessary for code generation. We demonstrate that large language models can autonomously generate valid inputs and simulate execution traces to self-correct. Consequently, we develop DryRUN, a framework that eliminates the need for ground-truth samples by allowing the LLM to iteratively plan, autonomously generate its own inputs and simulate execution, mitigating algorithmic overconfidence. Evaluations on the LiveCodeBench v6 dataset (post-March 2025) demonstrate that DryRUN matches performance against CodeSIM, a state-of-the-art and public-test-dependent framework, while operating entirely without public test cases or external execution feedback while reducing output token consumption.
