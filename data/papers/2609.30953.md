# CoCoRerank: Towards Conventional Commit Message Generation by Component and Candidate Consistency Reranking

- arXiv ID: `2609.30953v1`
- Authors: Shaopeng Jia, Yali Du, Ming Li
- Published: 2026-09-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.30953v1) | [pdf](https://arxiv.org/pdf/2609.30953v1)

## Abstract

Commit messages are essential for understanding software changes, yet automatic commit message generation typically treats a message as an unstructured text sequence. This limits its ability to support standardized development workflows, where commit messages are often expected to follow the Conventional Commits Specification (CCS) in the form type (scope): subject. In this paper, we study conventional commit message generation under the complete CCS format. We construct a new benchmark of 86,688 high-quality commits collected from open-source GitHub repositories, with each message normalized into type, scope, and subject through structural normalization and semantic quality filtering. Based on this benchmark, we propose a two-dimensional consistency-based reranking framework named CoCoRerank for LLM-based generation. CoCoRerank exploits horizontal consistency among the code change, type, scope, and subject, as well as vertical consensus across multiple generated candidates. Experiments with representative CMG baselines, LLM generators, reranking strategies, and ablation variants show that CoCoRerank improves both structural component prediction and subject generation quality. The results demonstrate that complete CCS supervision and multidimensional consistency modeling provide an effective foundation for accurate and standardized commit message generation. The artifact is publicly released at https://github.com/bluewhalebug/CoCoRerank.
