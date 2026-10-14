# Software Supply Chains are Dead: Use-Case-Oriented Regeneration

- arXiv ID: `2607.13021v1`
- Authors: Tanmay Singla, James C. Davis
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.13021v1) | [pdf](https://arxiv.org/pdf/2607.13021v1)

## Abstract

Modern software development relies on an increasingly doubtful premise: that the up-front implementation savings from adopting a dependency outweighs the maintenance costs. Two changes are reshaping the build-vs.-reuse calculus: software supply chain attacks have raised the cost of external reliance, while generative AI has lowered the cost of local implementation. We envision use-case-oriented regeneration as a new software sourcing paradigm that shifts the supply chain from external trust to local verification. We evaluate an agentic workflow that synthesizes only the specific slice of dependency functionality that a repository exercises. Our measurements across 180 repository-dependency pairs suggest that this approach is feasible: the replacements preserve 99.8% of repository-observed behavior across baseline validation checks and reduce the exported API surface by 93%. Software sourcing may evolve toward verifiable repository-specific code synthesis, especially when the required functionality is narrow, stable, and well tested.
