# Benchmark Engineering as a Design Instrument for Heterogeneous Information Systems

- arXiv ID: `2607.07175v1`
- Authors: Jáchym Bártík, Alžběta Šrůtková, Irena Holubová
- Published: 2026-07-08
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.07175v1) | [pdf](https://arxiv.org/pdf/2607.07175v1)

## Abstract

Contemporary information systems operate in heterogeneous and continuously evolving data environments, where representation choices and structural redesign decisions strongly influence system behavior. Existing benchmarking approaches, however, rely mostly on static datasets and fixed schemas, providing limited support for analyzing architectural trade-offs or guiding evolution in multi-model settings.
  This paper introduces TransforMMer, a framework for evolution-aware and representation-aware benchmark engineering in heterogeneous information systems. The approach treats benchmark construction as a systematic design process: starting from raw data, inferring structure, refining it conceptually, and generating comparable dataset variants across relational, document, and graph systems. The framework is grounded in a unified representation that enables explicit modeling of schemas and cross-model mappings and supports reproducible transformations across alternative representations.
  We position benchmarking as a system-design tool for evaluating architectural and representation-level decisions in evolving information systems, rather than as a static comparison of database engines. Through controlled benchmark construction scenarios on real-world datasets, we demonstrate how structural redesign steps -- such as embedding, enrichment, and hybrid partitioning -- affect observed query costs across systems. The results show that performance differences emerge primarily from the interaction between workload and representation design.
  By enabling systematic generation of structurally distinct yet semantically aligned dataset variants, the proposed approach connects conceptual data modeling with empirical system evaluation and supports reproducible, evolution-aware analysis of heterogeneous information systems.
