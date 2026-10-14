# Chiral Analysis of Smart Contracts: Detecting Vulnerabilities from Relational Inconsistencies Across Business Paths

- arXiv ID: `2607.17987v1`
- Authors: Yue Xue
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17987v1) | [pdf](https://arxiv.org/pdf/2607.17987v1)

## Abstract

Smart-contract vulnerabilities often arise from inconsistencies between business paths that should correspond to one another, such as single and batch entry points, direct and adapter-based flows, quote and execution paths, or inverse operations such as buy and sell. Existing analyzers are effective for many local syntactic and data-flow patterns, but they provide limited support for bugs whose oracle is relational: whether two semantically paired paths preserve compatible guards, state transitions, value flows, and failure behavior.
  This paper introduces chiral analysis, a relational model that treats paired business paths as implicit specifications for each other. We formalize chiral relations as static analogues of metamorphic relations, derive obligations over guards, actors, state, value, ordering, failure behavior, and external interactions, and report a vulnerability when a violated obligation has security impact. We implement this idea in ChiralDetector, a Solidity prototype that extracts business paths, ranks candidate pairs with static facts, applies LLM-based semantic filtering and detection, and validates and deduplicates findings.
  In a preliminary evaluation on the Phi protocol, ChiralDetector reduced 3,217 statically ranked path pairs to 1,643 semantic candidates, produced 101 deduplicated finding groups, and retained 44 strict-validator positives that manually collapsed to 13 effective unique issues. These include cross-art Merkle proof reuse, fee unit mismatches, public state-tracking helpers, and refund propagation gaps. The results suggest that chiral analysis can expose business-logic bug classes that are difficult to express as single-function rules while providing a structured way to control LLM cost and validator precision.
