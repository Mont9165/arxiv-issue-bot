# Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware

- arXiv ID: `2606.19725v1`
- Authors: Ma Toan Bach, Yuchi Zheng, Haingo Razafindranto, Tanvir Alam, Aric Leather, Ranveer Sandhu, Jitesh Arora
- Published: 2026-06-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2606.19725v1) | [pdf](https://arxiv.org/pdf/2606.19725v1)

## Abstract

Validating changes in low-level C firmware is expensive because unit tests (UTs) are fragile under strict build constraints, where missing headers, unresolved symbols, and dependency mismatches frequently prevent compilation and linking. This study introduces an automated UT authoring workflow for the Open-Source Silicon Initialization Library (openSIL) firmware codebase maintained by Advanced Micro Devices (AMD) that reduces manual effort through a large language model (LLM) guided multi-agent pipeline. The workflow combines automated generation of test scaffolds, library-aware creation or reuse of stubs, mocks, and fakes, and an iterative compile-dispatch repair loop driven by build logs and line-coverage feedback. We evaluate the approach using compilation success, repair iterations, dispatch success, and line coverage, with time, cost, and token usage as secondary measures. Across 76 functions under test, the workflow generated compilable UTs for 73 functions. In a configuration without line coverage guidance or retrieval augmentation, mean line coverage reached 73.9%. On a 48-function subset evaluated under both configurations, mean line coverage reached 98.8% with line-coverage guidance alone and reached 94.7% when combined with vector-database retrieval. Results show that automated generation-and-repair pipelines can substantially improve UT creation efficiency and coverage for constrained firmware environments while reducing manual debugging effort.
