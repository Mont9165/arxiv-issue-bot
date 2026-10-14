# From Reading Code to Reading Spec: A Verified Layer for LLM-Driven Codebase Maintenance

- arXiv ID: `2609.06383v1`
- Authors: Xinhao Zhang, Jingjie Lu, Kunpeng Liu, Fei Xie
- Published: 2026-09-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2609.06383v1) | [pdf](https://arxiv.org/pdf/2609.06383v1)

## Abstract

The rapid growth of LLM-generated code increases software complexity and the maintenance burden on engineers. While LLMs offer a potential automated alternative, this structural complexity hinders their ability to manage codebases directly. We introduce the Provable Representation Of Original Functionality (PROOF), which manages codebases indirectly via structured specifications. To enable full-lifecycle codebase management strictly through these specifications, PROOF abstracts codebase topology into a hierarchical natural-language representation. To establish absolute trust, the system proves semantic equivalence by reconstructing source code exclusively from this specification. This verified foundation drives maintenance requests, executing code modifications while synchronously updating itself to prevent semantic drift. Experiments on real-world repositories confirm the effectiveness of these specifications.
