# Security Incentivization: An Empirical Study of how Micropayments Impact Code Security

- arXiv ID: `2605.13100v1`
- Authors: Stefan Rass, Martin Pinzger, Rainer W. Alexandrowicz, Georg Sengstbratl, Johann Glock, Alexander Lercher, Fabian Oraze, Christoph Wedenig
- Published: 2026-05-13
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.13100v1) | [pdf](https://arxiv.org/pdf/2605.13100v1)

## Abstract

Security often receives insufficient developer attention because it does not directly generate visible value, leading to underinvestment in practice. We evaluate a countermeasure by team-level incentives tied to measurable security improvements over time. Our semi-automated mechanism aggregates static analysis findings from Bearer, Detekt, and mobsfscan, computes security issue density, and rewards teams based on the relative improvement ratio across sprints, enabling repeatable, scriptable reporting at scale.
  In a controlled course experiment with 84 students across 14 teams, we compared a security-incentivized condition, in which bonus points were linked to security scanner results, against a control condition with an otherwise identical grading scheme. The treatment group achieved significantly lower security issue density overall (beta regression: $β= -0.396, p = 0.0342$), indicating improved measurable security under incentivization. After controlling for platform, we observed a marked front-end/back-end disparity, with back-ends showing fewer issues and higher improvement ratios under incentives, highlighting heterogeneous effects across stack layers. Notably, these gains were not the byproduct of inflated code volume, as lines of code increased similarly across groups over time. The measurement pipeline and toolchain proved feasible for scripting and automation, supporting scalable adoption in practice.
  Our results suggest that aligning rewards with automated security metrics can measurably improve code security and merit follow-up in professional contexts and longer development lifecycles.
