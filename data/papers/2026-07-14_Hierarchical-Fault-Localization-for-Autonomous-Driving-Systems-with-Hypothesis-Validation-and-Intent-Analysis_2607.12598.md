# Hierarchical Fault Localization for Autonomous Driving Systems with Hypothesis Validation and Intent Analysis

- arXiv ID: `2607.12598v1`
- Authors: Rui Zheng, Changwen Li, Yi Ji, Rongjie Yan
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12598v1) | [pdf](https://arxiv.org/pdf/2607.12598v1)

## Abstract

Comprehensive testing is essential for the safety and reliability of Autonomous Driving Systems (ADS). Existing techniques can detect system-level failures or attribute them to coarse-grained modules, but they often fall short of localizing the root cause in source code. As a result, debugging remains labor-intensive, requiring developers to connect behavioral violations with complex implementation logic. To address this gap, we present HINT, a two-phase framework for hierarchical ADS fault localization based on hypothesis validation and intent analysis. In Phase I, HINT transforms failure-triggering execution recordings into multi-modal abstractions and uses causal reasoning to identify the responsible module. In Phase II, it reconstructs design-side intent and implementation-side behavior, then localizes suspicious code through reliability-aware consistency checking, without costly re-simulation. We evaluate HINT on Apollo across diverse failure modes and modules. The results show that HINT achieves the strongest overall performance across module-level diagnosis and code-level localization metrics, with 77.8% end-to-end Class@5 accuracy on real-world bugs.
