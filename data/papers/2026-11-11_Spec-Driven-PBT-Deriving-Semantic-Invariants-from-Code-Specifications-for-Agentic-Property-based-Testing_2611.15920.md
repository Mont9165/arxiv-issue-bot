# Spec-Driven PBT: Deriving Semantic Invariants from Code Specifications for Agentic Property-based Testing

- arXiv ID: `2611.15920v1`
- Authors: Aditya Shukla, Kartik Gupta, Ali Alavi, Pashootan Vaezipoor
- Published: 2026-11-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.15920v1) | [pdf](https://arxiv.org/pdf/2611.15920v1)

## Abstract

Software is increasingly written by AI agents that produce an implementation from a natural language specification, a practice known as agentic coding. Code is now produced faster than it can be reviewed, and has been shown to exhibit its own characteristic failure patterns. Property-based testing (PBT), a long-standing technique in which invariant properties of a program are checked against many generated inputs, has recently been revisited with LLM agents authoring the properties, thereby removing the high-effort derivation of invariants that has long hindered its adoption. Existing methods, however, derive these properties from the implementation alone (Code-driven PBT). At the same time, a thorough specification such as a product requirements document has become routine within agentic coding, yet its role in testing the resulting code remains underexplored. We study the value of the specification as a source of properties for testing agent-written code. Our key insight is that the specification, unlike the implementation, records what the code was meant to do, and invariants derived from it are not biased by particular implementation choices. We propose Spec-Driven PBT, an agent that first expresses invariants in natural language from the specification and only then inspects the implementation to translate them into concrete tests. Across 25 applications from ViBench, Spec-Driven PBT finds a novel set of bugs that Code-driven PBT misses, while writing 2.4x fewer property tests. Though the two approaches surface a roughly equivalent number of bugs, there is little overlap: nearly 60% of the 169 total bugs are found by only one. Qualitatively, we find that the bugs unique to Spec-Driven PBT tend to violate documented product workflows whereas those to Code-driven PBT instead concentrate on implementation robustness, offering complementary value for bug discovery in agent-written code.
