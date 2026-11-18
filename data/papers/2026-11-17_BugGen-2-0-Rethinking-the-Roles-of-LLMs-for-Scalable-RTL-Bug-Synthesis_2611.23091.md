# BugGen 2.0: Rethinking the Roles of LLMs for Scalable RTL Bug Synthesis

- arXiv ID: `2611.23091v1`
- Authors: Minh Luu, Michael Quinn, Aakash Tyagi, David Houngninou, Jiang Hu
- Published: 2026-11-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.23091v1) | [pdf](https://arxiv.org/pdf/2611.23091v1)

## Abstract

AI-assisted RTL localization and debugging need ground-truth bug datasets with known locations and observable failures, while testbench grading uses injected bugs to measure detection capability. Creating such datasets at scale remains a major EDA challenge. BugGen 1.0 shows that Large Language Models (LLMs) can generate context-aware RTL mutations. Still, it relies on the model for both choosing where to mutate and generating the edit, which increases inference costs and can lead to invalid choices. BugGen 2.0 changes this division of labor. Deterministic algorithms handle structural analysis, target selection, and validation, while the LLM focuses on localized semantic rewriting. Across four OpenTitan IP blocks and FabScalar with three LLMs, BugGen 2.0 reaches every requested quota of compilable bug scenarios that cause at least two test failures, with 14-16 of 16 configured mutation types represented. In completed same-model comparisons, it reduces token use by 6.8x-15.4x relative to BugGen 1.0 and 1.5x-7.9x relative to Firefly. BugGen 2.0 also expands the dataset without simulating every new bug. After finding accepted scenarios with observable failures, it generates alternative mutations at the same locations, simulates only a subset, and estimates acceptance for the rest. This skips 63.6% of AES and 33.9% of FabScalar variant simulations. Full simulation finds that 77.7% of AES variants and 95.2% of FabScalar variants are accepted, with a 1.09% estimation error on the directly comparable FabScalar set. These results show that focusing LLMs on semantic rewriting lowers inference and simulation cost while improving consistency across models and designs.
