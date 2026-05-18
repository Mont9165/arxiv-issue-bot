# The Dangers of Non-Self-Fixed Architecture Technical Debt and Its Impact on Time-to-Fix

- arXiv ID: `2605.16133v1`
- Authors: Edi Sutoyo, Paris Avgeriou, Andrea Capiluppi
- Published: 2026-05-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.16133v1) | [pdf](https://arxiv.org/pdf/2605.16133v1)

## Abstract

Technical Debt (TD) refers to the long-term costs incurred when developers prioritize short-term delivery over quality-improving work. Architectural Technical Debt (ATD) arises when architectural decisions (e.g., technology choices, patterns, or decomposition) prioritize near-term progress over future maintainability and evolvability. Because ATD affects a system's core structure and propagates through architectural dependencies, it is often more expensive and disruptive to remediate than localized code-level debt. Although ATD has been widely studied, an important but underexplored aspect of repayment is who performs it. Prior work provides limited empirical evidence on repayment responsibility in ATD and its relationship to time-to-fix.
  We empirically study self-fixed ATD, where the introducer also repays the debt, and contrast it with non-self-fixed ATD in large Apache open-source projects. We reconstruct ATD lifecycles by tracing Jira artifacts to version-control history to identify introduction and repayment points and attribute developer roles. We address three research questions on the prevalence of self-fixed ATD, time-to-fix differences between self-fixed and non--self-fixed items, and how factors related to code change and collaboration metrics relate to repayment speed. Using descriptive statistics, non-parametric tests, and survival analysis, we show that self-fixed and non--self-fixed ATD exhibit distinct repayment dynamics and differences in how changes are shared on ATD-affected files. In particular, non--self-fixed ATD is more likely to remain unresolved longer when changes are spread across many developers. These results provide actionable guidance for maintainers to identify high-risk ATD items and to reduce handoff costs by increasing introducer involvement when possible and documenting the design rationale during repayment.
