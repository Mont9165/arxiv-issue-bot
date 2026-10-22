# Code Comprehensor: Hierarchical Documentation and Cross-Modal Retrieval for Large Repositories

- arXiv ID: `2610.30016v1`
- Authors: Sujoy Roychowdhury, Joseph H. R. Isaac, Jiangning Gao, Martin Klitte, Diarmuid Corcoran
- Published: 2026-10-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.30016v1) | [pdf](https://arxiv.org/pdf/2610.30016v1)

## Abstract

Understanding large, complex, and rapidly evolving code bases remains a core challenge for software engineering at scale, hindering onboarding, maintenance, refactoring, and impact analysis. Providing this information to a Large-Language Model (LLM) is another hurdle, as the LLM must understand not only the required code method but also its associated methods in the grand scheme of the repository. We propose Code Comprehensor, a hybrid retrieval-reasoning framework combining (i) a code dependency callgraph, (ii) CodeScribe, which uses code-aware LLMs to generate hierarchical documentation across repository call graphs, and (iii) CodeContrast, a CLIP-style dual-encoder model trained on CodeScribe output to learn aligned text-code embeddings. CodeContrast enables fast, semantically precise retrieval of relevant code-context neighborhoods, which serve as grounded evidence for an MCP-based LLM orchestrator answering domain-specific queries. Evaluation on OpenCV and a proprietary 5M-LOC repository shows that CodeScribe-derived supervision significantly improves cross-modal retrieval in text-to-code accuracy over baseline approaches. Richer textual supervision (hierarchical documentation, parent/sibling context, and LLM-generated synthetic questions) consistently enhances performance across both repositories. LLM-as-a-judge evaluation using the popular RAGAS of the Code Comprehensor output yields above 90% faithfulness scores.
