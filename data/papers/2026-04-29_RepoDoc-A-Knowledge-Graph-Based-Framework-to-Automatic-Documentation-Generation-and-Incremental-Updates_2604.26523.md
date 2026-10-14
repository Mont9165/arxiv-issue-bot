# RepoDoc: A Knowledge Graph-Based Framework to Automatic Documentation Generation and Incremental Updates

- arXiv ID: `2604.26523v1`
- Authors: Dong Xu, Mingwei Liu, Xiwen Wang, Jianfeng Zhong, Zibin Zheng
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26523v1) | [pdf](https://arxiv.org/pdf/2604.26523v1)

## Abstract

Maintaining up-to-date, comprehensive documentation for large codebases is a persistent challenge. Recent progress in automated documentation has moved from template-based rules to large language models (LLMs), yet existing tools still process source code as flat fragments, producing isolated documents that lack semantic structure. This design also leads to excessive token consumption and slow generation, while failing to capture how code changes propagate across dependencies.
  We propose RepoDoc, a system that uses a repository knowledge graph (RepoKG) as the semantic foundation for the entire documentation lifecycle. Our framework consists of three stages: (1) RepoKG construction, which extracts code entities and their relationships; (2) module clustering, which groups code into functionally cohesive, hierarchical units; and (3) skillful agent-based generation, which queries the graph to create modular, cross-referenced documentation with auto-generated Mermaid diagrams. For incremental maintenance, a semantic impact propagation mechanism navigates the RepoKG bidirectionally to pinpoint all affected parts, allowing selective, targeted regeneration.
  Evaluated on 24 repositories across 8 programming languages, RepoDoc substantially outperforms state-of-the-art alternatives. It improves API coverage by 32.5% and completeness by 10.4%, while generating documentation 3x faster with 85% fewer tokens. For incremental updates, it cuts update time by 73% and token usage by 77%, and achieves 10.2% higher update recall, more accurately reflecting code changes in the regenerated documentation.
  The source code and experimental artifacts are available at https://github.com/SYSUSELab/RepoDoc.
