# KG-Commit: A Dynamic Knowledge Graph for Online Just-in-Time Software Defect Prediction

- arXiv ID: `2609.06272v1`
- Authors: Mohsen Hesamolhokama, Mohammad Sina Beyrami Aghbash, Behnam Rohani, Mohammadamin Fazli, Jafar Habibi
- Published: 2026-09-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.06272v1) | [pdf](https://arxiv.org/pdf/2609.06272v1)

## Abstract

Just-in-time software defect prediction (JIT-SDP) aims to identify risky commits as they arrive and provide developers with timely feedback. This need for low latency has led most approaches to rely on commit-level information and overlook the broader project context in which a change occurs. Incorporating this context is challenging because it requires both efficient retrieval for incoming commits and continual maintenance as the repository evolves. We introduce KG-Commit, a dynamic knowledge graph that incrementally maintains repository history, within-file code structure, and commit semantics as the project evolves. It also uses an AST-delta mechanism to track structural changes between file edits and relies on lightweight graph inference running entirely on CPU. Our evaluation on 11 Apache software projects against six baselines shows that KG-Commit achieves the highest aggregate Macro-F1 (0.704), G-Mean (0.706), and AUC (0.809) using our selected inference pipeline. Under a realistic online protocol, it outperforms LR, HGB, RF, and DeepJIT on all 11 projects, LApredict on 10, and JITLine on 9 projects in Macro-F1, with the aggregate paired difference significant in every case. KG-Commit processes each commit in approximately 1.33~s, with a cost that remains stable as the graph grows and is compatible with commit rates observed in real-world projects. These findings show that rich project context can be efficiently maintained and exploited for online JIT-SDP.
