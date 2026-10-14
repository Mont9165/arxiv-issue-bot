# EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming

- arXiv ID: `2608.01763v1`
- Authors: Kaustuv Mukherji, Jaikrishna Manojkumar Patil, Colton Payne, Paulo Shakarian, Dana Warmsley, Nigel Stepp, Evelyn Kim
- Published: 2026-08-03
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.LO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.01763v1) | [pdf](https://arxiv.org/pdf/2608.01763v1)

## Abstract

Large language models are increasingly used to reason about software vulnerabilities, but their outputs can silently violate domain knowledge, limiting their reliability in safety-critical settings such as medical devices. Prior work either treats that output as a prediction to be scored or constrains it to walks within a single knowledge graph; neither checks whether reasoning over a binary is consistent with an independent body of domain knowledge. We present EntailLLM, which validates each LLM-proposed analyst path by entailment: the path is a traversal of the binary's function call graph, the domain knowledge is represented in a separate graph, and verification aligns the two under temporal annotated logic. Across three CWE classes, four LLMs, three prompting strategies, and seven binaries varying in size from 405 to 12,696 function call-graph nodes, domain knowledge raises pooled entailment from 78% to 98%, with entailment decreasing in only 3% of the experiments. EntailLLM is deployed end-to-end on real medical-device binaries, reaching 98% pooled entailment without per-device tuning. Our system inherits the formal guarantees of generalized annotated logic, providing logical verification of LLM output that is both explainable and grounded in well-defined semantics.
