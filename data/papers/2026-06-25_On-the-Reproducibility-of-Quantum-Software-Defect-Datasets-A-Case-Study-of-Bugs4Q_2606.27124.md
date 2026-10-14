# On the Reproducibility of Quantum Software Defect Datasets: A Case Study of Bugs4Q

- arXiv ID: `2606.27124v1`
- Authors: Haruto Ohto, Yuta Ishimoto, Shinsuke Matsumoto, Shinji Kusumoto
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.27124v1) | [pdf](https://arxiv.org/pdf/2606.27124v1)

## Abstract

The reproducibility of software defect datasets is essential for obtaining reliable and comparable research results. Zhu et al. have shown that defect datasets such as Defects4J suffer from reproduction failures (i.e., reported bugs become non-reproducible) as time passes since their creation. However, it remains unclear whether these findings generalize to quantum software defect datasets. We therefore conduct a replication study of the prior work using Bugs4Q, a widely used dataset of real-world bugs in quantum programs. Our analysis includes 77,700 quantum program executions of 37 Bugs4Q artifacts across 21 core-library versions. The experimental results showed that the reproducibility of Bugs4Q dropped from 62.2% on Qiskit v0.20.1 to 16.2% on v2.3.1, the latest version as of April 1, 2026. A manual inspection of the root causes further indicated that 93.6% of the failures were dependency-related. While these findings are consistent with those of the prior work, we also observed differences. In particular, most reproduction failures in Bugs4Q cannot be resolved merely by adjusting dependency versions; instead, they require source-code modifications such as migrating import paths and API invocations. Based on this observation, we curated Bugs4Q-Robust, a patched version of Bugs4Q to restore reproducibility. Bugs4Q-Robust increases reproducibility from 16.2% to 78.4% on Qiskit v2.3.1. Our findings highlight the importance of continuous dataset maintenance in the rapidly evolving quantum software ecosystem.
