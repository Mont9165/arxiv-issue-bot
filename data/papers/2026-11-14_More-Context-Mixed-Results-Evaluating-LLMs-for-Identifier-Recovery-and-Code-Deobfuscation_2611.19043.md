# More Context, Mixed Results: Evaluating LLMs for Identifier Recovery and Code Deobfuscation

- arXiv ID: `2611.19043v1`
- Authors: Simon Queyrut, Valerio Schiavoni, Giuseppe Antonio Di Luna, Daniele Cono D'Elia, Leonardo Querzoni, Pascal Felber
- Published: 2026-11-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.19043v1) | [pdf](https://arxiv.org/pdf/2611.19043v1)

## Abstract

Source code is often obfuscated through identifier renaming, incentivizing reverse engineers to develop techniques for recovering meaningful names. To assess how LLMs compare with these techniques, we evaluate 4 traditional baselines and 3 LLMs (Qwen, OLMo and DeepSeek) on identifier detection and semantic recovery across 51 recent Java projects, 3 obfuscators, and 6 context/retrieval settings. LLMs generally outperform traditional techniques on both tasks, but benefit from different forms of context and settings: agentic retrieval yields the strongest detection results, reaching 91.56% $F_1$, while enclosing-class context generally improves semantic recovery at a higher token cost. Despite these gains, exact recovery peaks at 16.42% overall (under one-hop context) and 32.93% for field names (under repository retrieval), which are the easiest to recover. Class identifiers are the hardest to detect, with a mean detection $F_1$ of 48.48% across models, settings and obfuscators. More context is not always beneficial: larger methods hinder semantic recovery. Beyond identifier renaming, our experiments show that control-flow obfuscation degrades both tasks more than string encryption. Our findings provide useful ad hoc insights for reverse engineers choosing models and context strategies to deobfuscate code snippets.
