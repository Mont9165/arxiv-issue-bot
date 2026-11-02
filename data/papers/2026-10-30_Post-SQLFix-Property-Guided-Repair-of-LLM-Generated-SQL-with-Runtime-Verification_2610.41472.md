# Post-SQLFix: Property-Guided Repair of LLM-Generated SQL with Runtime Verification

- arXiv ID: `2610.41472v1`
- Authors: Zhihao Guo, Zonghan Wu, Yilei Shao, Haizhou Du, Nan Tang, Xiao Cheng, Huan Huo
- Published: 2026-10-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.41472v1) | [pdf](https://arxiv.org/pdf/2610.41472v1)

## Abstract

Large Language Models (LLMs) for Text-to-SQL frequently generate queries with syntax errors, invalid identifier references, or violations of SQL scoping and typing rules. Repairing these errors is a program correctness problem, yet existing approaches rely on Execution Feedback (EF), whose symptom-level, dialect-specific error messages force the LLM to speculate on root causes. We identify an Arbitration Paradox in this paradigm: the system relies on unverified models both to propose repairs and to make the final judgment on whether those repairs satisfy the required properties. We resolve this paradox by reformulating Text-to-SQL repair as property-guided program repair. Our framework, Post-SQLFix, canonicalizes SQL into a dialect-aware Canonical Query Structure (CQS) and validates it through a hierarchical static analyzer with three stratified property layers (Syntactic, Context-Free Structural, Context-Sensitive Semantic). The analyzer produces precise, schema-aware violation diagnostics to guide the LLM's repair proposals. A Verify-Before-Apply Temporal Monitor then accepts only repairs that reduce the violation count, do not reintroduce resolved violations, and satisfy the operator contracts. These runtime invariants are bounded by the declared rule family and operator contracts, while a finite retry budget ensures halting. On three established benchmarks (BIRD, Spider, Mini-Dev) spanning over 3,000 evaluation instances, three SQL dialects (SQLite, MySQL, PostgreSQL), and six model configurations, Post-SQLFix resolves 77.8% of the execution errors that EF leaves unrepaired, while requiring less than half as many repair iterations and 30% fewer tokens. Crucially, accepted transitions under the monitor introduce no statically detectable structural regressions in our evaluation, translating checked repair fidelity into absolute accuracy improvements of up to +11.6 percentage points.
