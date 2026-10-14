# Supporting System Testing with a Multi-Agent LLM-based Framework for Knowledge Graph Extraction: A Case Study with Ethernet Switch Systems

- arXiv ID: `2605.19180v1`
- Authors: Rongqi Pan, Mahboubeh Dadkhah, Jean Baptiste Minani, Hussein Al Osman, Lionel Briand, Haiwei Dong
- Published: 2026-05-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.19180v1) | [pdf](https://arxiv.org/pdf/2605.19180v1)

## Abstract

Technical documents contain rich domain knowledge for automating downstream tasks such as system testing. While this paper focuses on Ethernet switch configuration manuals (ESCMs), we propose a general framework that can be adapted to different industrial contexts. ESCMs provide valuable domain knowledge for Ethernet switch testing, but their semi-structured format, implicit step attributes, and complex section dependencies make them difficult to directly leverage for test automation. To address this, we generate knowledge graphs (KGs) that capture configuration knowledge from ESCM in a structured form. We propose a multi-agent LLM-based framework that extracts, evaluates, and improves KGs from ESCMs using a fine-grained KG schema and an iterative Extract-Evaluate-Improve (EEI) loop. Our evaluation on 50 real-world ESCMs shows that our framework achieves high extraction correctness using the original prompts, with average correctness scores ranging from 0.97 to 0.99 across three extraction tasks. For challenging ESCMs, the EEI loop further improves correctness through manual-specific prompt refinement. Moreover, the LLM judgments and human evaluations show substantial agreement, with Cohen's kappa of at least 0.72 across all extraction tasks. Finally, feedback from industry testers indicates that the generated KGs can support the generation of useful and correct test case specifications (TCSs) for downstream testing.
