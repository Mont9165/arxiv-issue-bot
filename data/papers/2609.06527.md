# ProcArena: A Multi-Scenario Benchmark for LLMs on Direct and Interactive PL/SQL Development from Natural Language

- arXiv ID: `2609.06527v1`
- Authors: Hang Zhang, Chaokun Wang, Yuzhi Pan, Ziyao Zhong, Shuo Cao, Yue Xue, Zeyu Huang, Xingwei Zhou, Fang Niu, Bofan Xie, Guanchen Ge, Leqi Zheng, Ziyang Liu, Xiannian Cao, Pengcheng Ge
- Published: 2026-09-06
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.06527v1) | [pdf](https://arxiv.org/pdf/2609.06527v1)

## Abstract

Large language models (LLMs) have shown strong potential for translating natural-language (NL) requirements into PL/SQL programs, attracting increasing attention from the database community. However, existing NL-to-PL/SQL efforts primarily focus on directly generating PL/SQL from complete NL requirements. In practice, PL/SQL development involves diverse scenarios, such as from-scratch development, code modification, debugging, and optimization, and may require either direct generation or multi-turn interaction. Yet, no comprehensive benchmark evaluates multi-scenario, direct and interactive, and multi-dialect NL-to-PL/SQL development. In this paper, we present ProcArena, an execution-based benchmark covering both Direct and Interactive modes. ProcArena comprises 3,998 executable tasks over 157 databases, spanning nine development subscenarios in PostgreSQL and Oracle. We construct challenging Direct tasks through Iterative Logic Enhancement and scenario-specific adapters, and derive paired Interactive tasks through Knowledge Integration and Requirement Perturbation while preserving executable targets. We further design a controlled Solver-User Simulator protocol that allows models to clarify user intent and inspect the database environment without exposing hidden execution feedback. Evaluating seven language models, we find that the best average scores are only 62.2% and 57.8% in Direct and Interactive, respectively, demonstrating that realistic NL-to-PL/SQL development remains challenging, particularly in interactive settings.
