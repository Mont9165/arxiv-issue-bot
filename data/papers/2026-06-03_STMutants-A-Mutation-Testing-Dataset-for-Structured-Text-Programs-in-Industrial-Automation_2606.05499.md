# STMutants: A Mutation Testing Dataset for Structured Text Programs in Industrial Automation

- arXiv ID: `2606.05499v1`
- Authors: Md Humaun Kabir, Md Rakibul Islam, Helen H. Lou
- Published: 2026-06-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.05499v1) | [pdf](https://arxiv.org/pdf/2606.05499v1)

## Abstract

Mutation testing is widely used to evaluate test-suite effectiveness, yet IEC 61131-3 Structured Text (ST) programs still lack a publicly available benchmark that supports reproducible mutation-based research. This gap is especially important because ST is extensively used in Programmable Logic Controllers (PLCs) that operate in real-time, safety-critical industrial environments, where software faults may cause equipment damage, production loss, or unsafe system behavior. To address this need, we present STMutants, a curated mutation testing dataset for industrial automation software. STMutants contains 110 generated first-order mutants derived from 11 ST programs collected from the OSCAT basic library and industrially relevant sources, of which 108 are retained after observability and equivalence screening. The dataset covers seven mutation operator categories adapted from classical taxonomies for the PLC domain, including value, relational, arithmetic, logical, negation, operation insertion/omission, and initialization faults. Each mutant is constructed through a four-phase methodology: fault-type profiling and operator selection, syntactic transformation, compilability verification, and manual equivalence screening with strong inter-rater agreement (kappa = 0.87). To demonstrate the usefulness of the dataset, we evaluate three large language models (LLMs) in a two-phase setting: test-suite generation followed by mutation kill/survive prediction. Across 108 retained mutants, the models achieve mutation detection accuracies of 86.1%, 94.4%, and 86.1%, respectively, with statistical analysis confirming significant performance differences. By providing the first publicly available mutation benchmark for ST programs, STMutants enables reproducible research on automated test generation, mutation analysis, fault localization, and AI-assisted quality assurance for PLC software.
