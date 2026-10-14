# When Does q-error Predict Plan Regret? Three Regimes of Cardinality-Estimation Error

- arXiv ID: `2606.15600v1`
- Authors: Madhulatha Mandarapu, Sandeep Kunkunuru
- Published: 2026-06-14
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.15600v1) | [pdf](https://arxiv.org/pdf/2606.15600v1)

## Abstract

Cardinality-estimation (CE) research ranks estimators by q-error, yet it is well known that q-error is an imperfect proxy for query-plan quality. We give a measurement-driven account of when it is a good proxy and when it is not, and why. Modeling plan selection as an argmin over a piecewise-linear cost landscape, we find that plan regret (the cost of the chosen plan relative to the optimal, under true cardinalities) is governed by plan-cost geometry in a regime-dependent way. (i) For small errors, a true-point condition number kappa predicts regret and out-predicts q-error; its predictive power decays to zero as error grows, as a local linearization must. (ii) For large errors -- where deployed learned estimators operate -- an estimator-independent average-case sub-optimality measure ACS-infinity predicts which queries are regret-prone (Spearman rho ~ 0.54 on STATS-CEB), while q-error is nearly uninformative at the query level (rho ~ 0.05). (iii) The worst case is Haritsa's maximum sub-optimality (MSO). The three are one cost-ratio spectrum under three weightings. We prove a limit law ACS-infinity = sum_k r_k pi_k with cardinality-independent combinatorial weights, and validate every claim on STATS-CEB and JOB-light with four released estimators under pre-registered decision rules, and confirm on real PostgreSQL runtime that ACS-infinity predicts regret where q-error does not. The contribution is conceptual and empirical -- an average-case companion to worst-case robust query optimization, and a characterization of when an accuracy metric tracks plan quality -- rather than a new estimator. Code and the full pre-registration are public.
