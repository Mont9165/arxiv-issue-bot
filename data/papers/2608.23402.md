# EXPLAIN Yourself! Finding Query Planner Stalls Across DBMSes

- arXiv ID: `2608.23402v1`
- Authors: Geoffrey X. Yu, Ryan Marcus, Tim Kraska
- Published: 2026-08-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.23402v1) | [pdf](https://arxiv.org/pdf/2608.23402v1)

## Abstract

Query planners are typically expected to produce optimized plans quickly, leading many researchers (including the authors of this paper) and practitioners to design systems that assume query planning is a low-cost operation. Using a lightweight agentic search, we show that this assumption does not always hold. Across seven DBMSes, including four commercial systems, we find at least one query per system that takes more than three minutes to plan. In addition to being slow to plan, such queries risk tying up database resources without performing useful work, creating a potential denial-of-service vector. We analyze the queries our search uncovers and compare how the seven systems respond to each pattern. We find that although the queries triggering slow planning are largely DBMS-specific, recurring pathologies involving correlated subqueries, CTE expansion, repeated subquery expressions, disjunctive joins, and constant folding affect multiple systems. We release our uncovered queries along with a curated suite of parameterized query pathologies that researchers and database engineers can use to test planner robustness. Overall, our results show that query planning cannot always be treated as a predictably inexpensive operation and that its latency and robustness deserve further attention from both database researchers and engineers.
