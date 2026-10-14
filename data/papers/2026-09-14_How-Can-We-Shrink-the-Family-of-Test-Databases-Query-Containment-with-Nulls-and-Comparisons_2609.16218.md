# How Can We Shrink the Family of Test Databases? Query Containment with Nulls and Comparisons

- arXiv ID: `2609.16218v1`
- Authors: Helen Sternbach, Sara Cohen
- Published: 2026-09-14
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.16218v1) | [pdf](https://arxiv.org/pdf/2609.16218v1)

## Abstract

Query containment and equivalence drive database query optimization and rewriting. For plain conjunctive queries, both are decided by evaluating one query over a single canonical database of the other. This classical test breaks down in two settings that pervade real queries: databases with null values under SQL's three-valued semantics, and queries with order comparisons. In both, deciding containment is $Π_2^p$-complete, and the known characterizations replace it by an exponential family of test databases, leaving no practical route to certifying equivalence.
  We ask how the family of test databases can be shrunk. For conjunctive queries over databases with nulls, we shrink the family to one that is exponential only in a special set of variables, and place containment in NP when that set has constant size. For queries with comparisons, we construct canonical values that decide containment, and then shrink the family by decomposing the test into independent components and by splitting it along the order conflicts. Finally, we combine the two features, and prove that the number of test databases is fixed-parameter tractable in three local parameters of the two queries, with the null-only and comparison-only tests as special cases. Each test evaluates the containing query over a family of databases, an operation native to any database system.
