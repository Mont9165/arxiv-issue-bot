# Code Lifespan Survival Analysis (CLSA): Predicting the Survival of Source Code Lines Using AST-Aware Mining

- arXiv ID: `2606.04993v1`
- Authors: Pavel Gurov
- Published: 2026-06-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.04993v1) | [pdf](https://arxiv.org/pdf/2606.04993v1)

## Abstract

Context: Predicting which source lines will be deleted - and when - matters for maintenance, technical debt, and review prioritization. Existing MSR approaches work at file or method granularity, masking individual-statement risk. Objective: We introduce Code Lifespan Survival Analysis (CLSA), the first framework to model code survival at individual-line granularity. CLSA treats each line as a right-censored subject and estimates deletion risk from structural, contextual, and temporal covariates; its strongest predictors are computable statically from one file (AST structure plus line entropy), without version history or bug data. Method: We mine 32.5 million line birth events from 120 open-source TypeScript repositories. A 5-stage bipartite matching pipeline separates true deletions from refactoring noise (migrations and rewrites), preventing 8.3 million false deaths. We fit a Cox Proportional Hazards model with 15 covariates and check robustness via Weibull/Log-Logistic AFT, gamma frailty, and time-stratified landmark models. Results: More than half of all lines are never deleted (Kaplan-Meier median not reached); among deleted lines the median lifespan is 95.7 days. Covariate effects are strongly time-varying, forming three regimes. Line Shannon entropy is moderately protective for new code (HR=0.84, 0-90 days) and strongly protective for mature code (HR=0.36, 365+ days), explaining its proportional-hazards violation. Lines in conditional branches reverse: protective at birth (HR=0.97), a risk factor after 90 days (HR=1.21). Repository identity is the largest factor: a gamma frailty model (variance theta=1.449) raises concordance from 0.586 to 0.666, outweighing every structural covariate. Conclusion: Line-level survival modeling is tractable, yielding interpretable, mostly static risk signals and a calibration recipe for time-conditional risk scoring in IDEs and code review.
