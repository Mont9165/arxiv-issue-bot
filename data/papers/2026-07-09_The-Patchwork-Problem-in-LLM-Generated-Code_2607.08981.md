# The Patchwork Problem in LLM-Generated Code

- arXiv ID: `2607.08981v1`
- Authors: Viraaji Mothukuri, Reza M. Parizi
- Published: 2026-07-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.08981v1) | [pdf](https://arxiv.org/pdf/2607.08981v1)

## Abstract

LLM-generated code often compiles, passes tests, and appears correct, yet breaks once deployed. The root cause is frequently structural rather than logical. A generated endpoint references configuration keys never declared in the project, an import targets a package that does not exist in any registry, or a new route omits the authentication guard applied to every sibling endpoint. Each patch is locally valid but globally incoherent, and standard CI toolchains rarely surface these failures. As LLM-powered coding tools see widespread adoption, this blind spot poses a growing risk to software quality. We call this the \textbf{patchwork problem}. This paper formalizes structural coherence as consistency invariants over graph representations of repository artifacts, including import, call, dependency, configuration, schema, resource, control-flow, and routing graphs, and introduces an eight-category failure taxonomy distinguishing defects specific to LLM generation from those merely amplified by it. We present a hybrid verification framework that delegates to mature static analysis tools where they already excel and deploys purpose-built detectors for cross-cutting invariants underserved by existing toolchains, targeting provable constraint violations rather than heuristic pattern matching. Empirical evaluation across two frontier models under four prompting strategies reveals that the vast majority of structural failures evade type checking, testing, and SAST entirely, and that failure patterns diverge qualitatively between models in ways that challenge model-agnostic mitigation strategies. External validation on real-world AI-generated repositories confirms that these failures are not artifacts of controlled experimentation but are prevalent wherever LLMs write code with minimal human oversight.
