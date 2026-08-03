# Repository-Aware Metamorphic Relation Generation for Augmented Reality Applications using Large Language Models

- arXiv ID: `2607.28775v1`
- Authors: Dibyendu Brinto Bose, Jiawei Qin, Chris Brown
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.28775v1) | [pdf](https://arxiv.org/pdf/2607.28775v1)

## Abstract

Metamorphic Testing (MT) provides a promising approach for testing software without defined test oracles by specifying expected relations between inputs and outputs, instead of relying on exact outputs. For example, testing Augmented Reality (AR) applications is challenging due to dynamic interactions between virtual content, physical environments, and code, which make traditional test oracles difficult to define. However, formulating metamorphic relations (MRs) is time-consuming and burdensome. We introduce a context-aware pipeline that generates and refines MRs using repository-level context and reasoning orchestration, evaluated on a dataset of 142 mobile AR system repositories. Across three context configurations generating 14,916 candidate MRs, hierarchical context yielded the broadest coverage (7,004 MRs across 142 repositories and 5,167 class--method pairs) and lower redundancy. An agentic deliberation process then reconciled conflicting candidates---observed in 79.0% of cases---reducing duplication and selecting context-aware relations in 88.2% of outcomes. A manual oracle study shows refined relations (n = 141) are both logically valid and sufficiently concrete to be directly translated into test assertions, and a preliminary case study reveals converting generated MRs (n = 5) into executable tests can detect non-equivalent mutations in real-world code. Overall, our results show that combining repository-aware MR generation with reasoning-based refinement enables scalable construction of reliable, domain-relevant test oracles.
