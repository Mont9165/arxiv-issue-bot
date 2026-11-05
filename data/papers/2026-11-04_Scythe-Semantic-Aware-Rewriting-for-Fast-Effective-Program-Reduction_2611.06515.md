# Scythe: Semantic-Aware Rewriting for Fast,Effective Program Reduction

- arXiv ID: `2611.06515v1`
- Authors: Ioanna Moraiti, Charalambos Mitropoulos, Artem Anchikov, Sotirios Ioannidis, Dimitris Mitropoulos, Thodoris Sotiropoulos
- Published: 2026-11-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.06515v1) | [pdf](https://arxiv.org/pdf/2611.06515v1)

## Abstract

Automated program reduction shrinks a program into a smaller one that preserves a property of interest. Language-agnostic grammar-based reducers are easy to retarget across languages, but because they reason only about syntax, they cannot perform the coupled edits needed to remove whole declarations, e.g., a method cannot be deleted while it is still called. As a result, they waste oracle calls on edits that cannot succeed and often leave irrelevant declarations behind. We present SCYTHE, a fast, semantic-aware pre-processing step that runs in front of any grammar-based reducer without modifying it. SCYTHE encodes the program as a typed declaration dependency graph and applies a set of semantic-aware operators that decouple declarations from their use sites, making them removable while keeping the program well-typed. Fine-grained token-level minimization is then left to the downstream reducer. On 73 benchmarks across C, Java, and Solidity, combining SCYTHE with PERSES never yields a larger result than PERSES alone, and a strictly smaller one on 70 of 73 cases. On average, the combination produces programs 55.6% smaller (up to 95.5%) and is 2.3$\times$ faster (up to 7.4$\times$). SCYTHE also boosts LATRA, a reducer that, unlike the purely syntactic PERSES, also applies language-specific transformations: the combination produces programs 10.6% smaller (up to 61.8%) and is 2.4$\times$ faster on average. Video: https://youtu.be/uEq_YYU0zZw
