# A Set-Theoretic Approach to Detecting Logic Bugs in DBMS Inner Join Optimizations

- arXiv ID: `2606.23294v1`
- Authors: Ce Lyu, Changzheng Wei, Yanhao Wang, Jie Liang, Li Lin, Hanghang Wu, Minghao Zhao, Ying Yan, Aoying Zho
- Published: 2026-06-22
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.23294v1) | [pdf](https://arxiv.org/pdf/2606.23294v1)

## Abstract

The query optimizer is a fundamental component of database management systems that determines the most efficient execution strategy for a given query by evaluating alternative query plans. Among its tasks, join optimization plays a central role, as the order of joins in multi-table queries can significantly affect execution performance. However, due to the inherent complexity of join optimization, logical bugs are inevitable and often difficult to detect. While existing fuzzing tools have shown notable success in uncovering crash- and performance-related errors, effectively identifying logical bugs -- cases in which the system produces incorrect query results -- remains largely unresolved.
  In this paper, we propose a metamorphic testing approach to detect DBMS bugs related to INNER JOIN optimization through the lens of set theory. For each testing case, equivalent queries are generated based on a basic set operation -- intersection -- and three semantics-preserving transformation rules, i.e., symmetric join transformation, asymmetric difference transformation, and symmetric difference transformation, are introduced. These rules rewrite a simple NATURAL/INNER JOIN query into a more complex, yet semantically equivalent, form. We implement this design in JoinEquiv, which serves as a testing oracle to systematically uncover logical inconsistencies in DBMS query processing by comparing the results of original and transformed queries. Using JoinEquiv, we uncovered 29 previously unknown issues in mainstream DBMSs (MySQL, TiDB, DuckDB, and Percona), and 27 of them were officially confirmed. JoinEquiv reveals deep logical flaws in DBMS optimizers and executors, underscoring its value in enhancing DBMS robustness.
