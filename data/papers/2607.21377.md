# A Logic-based Temporal Cohort Discovery Engine: Algorithms, Indices, and Experimental Results on the National Sleep Research Resource

- arXiv ID: `2607.21377v1`
- Authors: Yan Huang, Xiaojin Li, Licong Cui, Guo-Qiang Zhang
- Published: 2026-07-23
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2607.21377v1) | [pdf](https://arxiv.org/pdf/2607.21377v1)

## Abstract

Large sleep-study repositories contain rich time-stamped physiological annotations, but cohort discovery is still commonly implemented as ad hoc scripts or scalar-index filters. We present a logic-based temporal cohort discovery engine that brings formal semantics, model checking, specialized indexing, and empirical evaluation into a unified biomedical informatics framework. We adopt Rational Ensemble Logic (QEL) as a dense-time formal foundation for sleep-data querying and represent each annotated polysomnogram as a Biomedical Event Structure Temporal Model (BEST), a finite mapping from event labels to non-overlapping rational interval ensembles. Cohort discovery is formulated as model checking of QEL formulas over BEST databases. We organize common sleep-research requirements into three reusable temporal query patterns: single-event retrieval, dual-event temporal pattern matching, and event data extraction. The prototype cohort discovery engine was implemented in Python with in-memory and MongoDB-backed execution modes and evaluated on synthetic interval datasets containing up to 90 million intervals and on real-world National Sleep Research Resource annotations from the Cleveland Children's Sleep and Health Study (CCSHS) containing 515 subjects, 202,587 intervals, 23 event labels. 2DFC constructs indexes in linear space and linear build time, reducing build time at 90 million intervals from 11,549 s with RTFC and 23,902 seconds with 2DRT to 3,655 seconds. On CCSHS, cohort-selection queries executed at sub-second latency at native scale and under 45 seconds at 1,000 times scale. This work is a part of the Symbolic Biomedicine program championed by the corresponding author.
