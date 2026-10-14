# How do Execution Features Improve Statistical Fault Localization? An Empirical Study

- arXiv ID: `2606.30324v1`
- Authors: Marius Smytzek, Andreas Zeller
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.30324v1) | [pdf](https://arxiv.org/pdf/2606.30324v1)

## Abstract

Automated fault localization helps developers find faults in large code bases. Statistical fault localization (SFL) ranks suspicious lines from pass/fail spectra, but line execution alone misses information like data-flow, values, or branch conditions that explain why a failure occurs.
  This study evaluates whether augmenting SFL with execution features improves localization accuracy and developer-oriented inspection effort. We extract execution features with EFDD for all Tests4Py subjects, train per-subject random forests, map importances to source lines, and combine the resulting weights with established SFL formulas. The evaluation measures reference-patch accuracy, line- and function-level effort, robustness, and feasibility using a confounder-adjusted mixed-effects model, corroborated by paired statistical tests and outcome-neutral quality checks.
