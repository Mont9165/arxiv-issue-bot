# Operationalizing Property-Based Testing for Data-Intensive Scalable Computing Systems

- arXiv ID: `2606.11132v1`
- Authors: Yaoxuan Wu, Ingrid Lee, Ahmad Humayun, Muhammad Ali Gulzar, Miryung Kim
- Published: 2026-06-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.11132v1) | [pdf](https://arxiv.org/pdf/2606.11132v1)

## Abstract

While fuzzing effectively catches crashes, its shallow oracles often miss semantic drifts and optimization-related errors in data-intensive scalable computing (DISC) frameworks. Property-based testing (PBT) addresses this limitation by checking general semantic invariants across diverse workloads and inputs, rather than relying on specific expected outputs. However, systematically operationalizing PBT for DISC systems remains difficult because it requires both reusable property definitions and effective instantiation into valid workloads and data.
  We present DiscPBT, a property-based testing engine for Apache Spark. DiscPBT introduces eight reusable meta-properties for DISC semantic testing, spanning equivalence rewriting, data decomposition, computation decomposition, and operator-local semantic relations. To operationalize these meta-properties, DiscPBT provides reusable generators for synthesizing valid workload skeletons and input data, together with an instantiation framework that realizes each meta-property in schema-compatible contexts through compatible operators, expressions, and UDFs.
  Our evaluation on PySpark shows that DiscPBT achieves 1.2$\times$ higher branch coverage and 1153$\times$ greater plan diversity than CometFuzz. Across 66 concrete properties, DiscPBT reveals cross-version semantic drift as well as subtle corner-case pitfalls involving NaN and empty inputs, that are not captured by crash-based fuzzing alone. These results demonstrate the value of systematic PBT for uncovering semantic issues in DISC frameworks.
