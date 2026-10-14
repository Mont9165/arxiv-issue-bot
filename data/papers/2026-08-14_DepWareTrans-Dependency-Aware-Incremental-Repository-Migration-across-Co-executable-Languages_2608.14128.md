# DepWareTrans: Dependency-Aware Incremental Repository Migration across Co-executable Languages

- arXiv ID: `2608.14128v1`
- Authors: Sivajeet Chand, Alexander Pretschner, Steve Haupt, Derui Zhu, Sushant Kumar Pandey
- Published: 2026-08-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.14128v1) | [pdf](https://arxiv.org/pdf/2608.14128v1)

## Abstract

Repository-level code translation is critical for modernizing legacy systems, yet existing approaches based on large language models (LLMs) operate at the file level and fail to scale to codebases with complex inter-file dependencies. This limitation is evident in our industrial setting, where we aim to migrate a production repository (STAR) from Java to Kotlin, but file-level approaches produce fragmented results and fail to achieve end-to-end correctness. In this paper, we show that the primary cause of failure at the repository level is dependency inconsistency. Through an empirical study on open-source and industrial systems, we find that most errors arise from unresolved cross-file dependencies that cannot be effectively addressed by iterative feedback alone. We propose a dependency-aware incremental migration framework that elevates the unit of translation from individual files to dependency-consistent batches. Our approach constructs a dependency graph, groups interdependent files, and performs batched translation with iterative compile- and test-driven validation. We evaluate our method on a 51K line of code (LOC) industrial system and multiple repositories across interoperable language pairs (Java-Kotlin, Java-Scala, and C#-F#). On the STAR repository, file-level approaches achieve 38.16% compilation and 9.39% test success, whereas our approach achieves 100% compilation and test success across the evaluated settings, converging within a small number of iterations. These results show that dependency-aware batching improves scalability and reliability in repository-level code translation.
