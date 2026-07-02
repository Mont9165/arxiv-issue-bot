# Auditing Empirical Comparisons in Quantum Software

- arXiv ID: `2607.00516v1`
- Authors: Boshuai Ye, Peng Liang, Maryam Tavassoli Sabzevari, Arif Ali Khan
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00516v1) | [pdf](https://arxiv.org/pdf/2607.00516v1)

## Abstract

Empirical quantum-software papers often report that one compiler, optimizer, backend, or ansatz outperforms another. Such comparisons are not properties of a tool alone: they can change with benchmark scope, circuit construction, compilation, sampling, backend or noise assumptions, optimizer choices, and resource budgets. Existing testing, benchmarking, and reproducibility methods help assess programs, tools, executions, and platforms, but they do not directly audit whether the reported comparison itself is supported by the evidence exposed in the source paper or accompanying materials.
  We present CLAIMSTAB-QC, a source-bounded framework for auditing empirical comparisons in quantum software. Given a reported comparison, the framework records the baselines, metric, relation, and admissible evidence; locks the comparison design before outcomes are computed; and reports either a scoped relation outcome or an explicit evidence boundary. For strict scalar-directional comparisons, the reported direction is classified as Sustained, Unresolved, or Reversed within the locked audit scope.
  We evaluate CLAIMSTAB-QC on 455 comparative claims from 119 quantum-software papers. The central finding is a materialization gap: 175 claims can be represented for audit planning, 79 become scalar-directional planning records, 53 yield lockable audit or diagnostic designs, and only 8 expose enough matched evidence to audit the original comparison without proxy reconstruction. These 8 records yield 2 Sustained, 4 Unresolved, and 2 Reversed outcomes. Controlled diagnostics over 24 benchmark-relevant comparisons further show that simpler checks can preserve apparent directions whose support weakens under locked audit designs.
