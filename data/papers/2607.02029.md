# Benchmarking Quantum Software Testing with Scalable Quantum Programs

- arXiv ID: `2607.02029v1`
- Authors: Yuechen Li, Minqi Shao, Xiyuan Li, Jianjun Zhao, Kai-Yuan Cai
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2607.02029v1) | [pdf](https://arxiv.org/pdf/2607.02029v1)

## Abstract

Quantum software testing (QST) checks whether quantum programs behave according to their intended specifications. A key requirement for QST research is a benchmark that supports rigorous empirical evaluation on programs that are testable and better reflect current software development practices. However, existing studies heavily rely on small hard-coded or circuit-level benchmarks, while available quantum programs are scattered across repositories without clear selection criteria, which limits fair comparison and systematic reproducibility. To this end, we present Qolumbina, a benchmark infrastructure for controlled QST experiments on scalable quantum programs. Qolumbina curates 40 programs from open-source repositories, turns them into test-ready subjects through systematic selection, refactoring, specifications, test case examples, unit tests, and standardized interfaces. We also propose QST-oriented criteria to characterize quantum programs along functionality, output behavior, development complexity, and quantum-specific execution complexity. Using these criteria, our empirical study shows that Qolumbina covers diverse testing-relevant properties and supports scalability analysis beyond fixed-size circuit benchmarks. Through controlled experiments with two recent QST approaches, we demonstrate the feasibility of using Qolumbina for execution-cost and fault-detection studies, and highlight backend-dependent effects that can influence QST result interpretation.
