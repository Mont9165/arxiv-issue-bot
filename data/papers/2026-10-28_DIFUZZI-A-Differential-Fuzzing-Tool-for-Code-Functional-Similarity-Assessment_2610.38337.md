# DIFUZZI: A Differential Fuzzing Tool for Code Functional Similarity Assessment

- arXiv ID: `2610.38337v1`
- Authors: Simantika Bhattacharjee Dristi, Matthew B. Dwyer
- Published: 2026-10-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.38337v1) | [pdf](https://arxiv.org/pdf/2610.38337v1)

## Abstract

A range of software engineering tasks, such as optimization and refactoring, seek to preserve the behavior of software components and require methods to assess functional similarity. Research has explored formal approaches to prove functional equivalence and used machine learning methods to approximate it, but the former does not scale and does not quantify the extent of similarity and the latter struggles when subtle semantic differences are present. Differential fuzzing offers a scalable approach for differencing programs semantically, but applying it often requires substantial manual effort to construct input generators that are well-suited to a target pair of programs. To address this challenge, we introduce DIFUZZI, which incorporates an LLM-based generator synthesis step that is iteratively validated and repaired. By automating this step, DIFUZZI paves the way for broader applicability of differential fuzzing. We release DIFUZZI at https://github.com/Dristi123/difuzzi_tool, with a demonstration video at https://youtu.be/FlHNOHuo9WE
