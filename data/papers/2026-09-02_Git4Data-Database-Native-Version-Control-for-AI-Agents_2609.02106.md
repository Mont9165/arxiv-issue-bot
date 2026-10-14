# Git4Data: Database-Native Version Control for AI Agents

- arXiv ID: `2609.02106v1`
- Authors: Hongshen Gou, Zuyu Zhang, Yuze Sun, Peng Xu, Feng Tian, Long Wang, Jianguo Wang
- Published: 2026-09-02
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.02106v1) | [pdf](https://arxiv.org/pdf/2609.02106v1)

## Abstract

Large Language Model (LLM) agents increasingly explore many candidate states of relational data in parallel, each of which should remain isolated, reproducible, and auditable, preferably through the same SQL interface used for ordinary data work. Existing tools support this requirement only partially: source-code version control does not scale to large datasets, whereas relational databases manage large data efficiently but rarely expose native branching, comparison, and merging. We present Git4Data, a database-native version-control layer for agentic workflows. Git4Data treats a database as a repository and a table as a versioned object, exposing Git-style operations (snapshot/tag, branch, diff, and merge with explicit conflict-resolution policies) through SQL extensions. Implemented in MatrixOne, a cloud-native relational database, Git4Data leverages immutable object storage and MVCC to make the cost of these operations proportional to the size of the change rather than the size of the data. On the BranchBench agentic branching workloads, Git4Data outperforms DoltDB by up to an order of magnitude. Overall, we believe this work sheds light on how relational databases can better support AI agents through efficient versioning.
