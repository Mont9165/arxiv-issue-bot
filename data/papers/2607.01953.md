# Underspecification does not imply Incoherence: The Risks of Semantic Collapse in Coding Models

- arXiv ID: `2607.01953v1`
- Authors: Cedric Richter, Mike Papadakis
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01953v1) | [pdf](https://arxiv.org/pdf/2607.01953v1)

## Abstract

Large Language Models (LLMs) have become increasingly effective at generating code when task descriptions are clear and precise. Yet, in practice, user-provided task descriptions are often ambiguous, incomplete, or contradictory, leaving critical aspects of the intended program behavior underspecified. In such cases, multiple behaviorally distinct interpretations may satisfy the description equally well, yet semantically differ in ways that matter/affect the user intent. A natural expectation, often assumed by researchers, is that prompt underspecification manifests as incoherence: When asked multiple times, an LLM produces multiple semantically distinct implementations reflecting the ambiguity of the task description. In this paper, we challenge this assumption. We find that LLMs frequently collapse onto a single incorrect interpretation of the task description, consistently generating coherent but behaviorally misaligned code. We term this failure mode detrimental semantic collapse and find that it affects over 10% of tasks in MBPP, 3% in HumanEval, and 32% of LiveCodeBench, all benchmarks assumed to be well-specified. By deliberately injecting underspecification issues in the benchmark prompts, the rate rises to over 5 times, exposing a fundamental blind spot in disambiguation and correctness estimation techniques that rely on incoherence as a proxy for prompt underspecification.
