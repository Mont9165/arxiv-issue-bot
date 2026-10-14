# ImproBR: Bug Report Improver Using LLMs

- arXiv ID: `2604.26142v1`
- Authors: Emre Furkan Akyol, Mehmet Dedeler, Eray Tüzün
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.26142v1) | [pdf](https://arxiv.org/pdf/2604.26142v1)

## Abstract

Bug tracking systems play a crucial role in software maintenance, yet developers frequently struggle with low-quality user-submitted reports that omit essential details such as Steps to Reproduce (S2R), Observed Behavior (OB), and Expected Behavior (EB). We propose ImproBR, an LLM-based pipeline that automatically detects and improves bug reports by addressing missing, incomplete, and ambiguous S2R, OB, and EB sections. ImproBR employs a hybrid detector combining fine-tuned DistilBERT, heuristic analysis, and an LLM analyzer, guided by GPT-4o mini with section-specific few-shot prompts and a Retrieval-Augmented Generation (RAG) pipeline grounded in Minecraft Wiki domain knowledge. Evaluated on Mojira, ImproBR improved structural completeness from 7.9% to 96.4%, more than doubled the proportion of executable S2R from 28.8% to 67.6%, and raised fully reproducible bug reports from 1 to 13 across 139 challenging real-world reports.
