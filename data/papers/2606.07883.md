# DP4SQL: Differentially Private SQL with Flexible Privacy Policies

- arXiv ID: `2606.07883v1`
- Authors: Andrew Cascio, KinChin Tong, Daniel Kifer, Zeyu Ding, Danfeng Zhang
- Published: 2026-06-05
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.07883v1) | [pdf](https://arxiv.org/pdf/2606.07883v1)

## Abstract

The plausible deniability model of differential privacy for single-table datasets is well-understood. However, applying differential privacy to relational databases is much trickier: each application needs flexibility in specifying the pieces of information about an entity, spread across multiple relations, that require plausible deniability guarantees. Existing differentially private SQL systems only support rigid privacy policies. Even seemingly small changes, such as specifying that some tables need to protect the existence of records while others only need to protect the record contents, require significant manual effort in updating their privacy accountants and proving their correctness.
  One example of a challenge is the presence of partially public data. Public columns in a table (e.g., faculty names in a university dataset and partial course enrollment information) can cause some queries to require more noise (compared to fully private data), while others require less noise. This kind of reasoning is not supported in existing systems. Another example is when different parts of records (e.g., demographics, financial data) require different levels of privacy protection. Again, existing differentially private SQL systems need to rewrite their rules for calculating query stability in order to support such a feature. This paper presents DP4SQL, a differentially private SQL system that allows data curators to better customize the plausible deniability requirements for their relational databases. This avoids the drawbacks of the "one-size-fits-all" systems that would either underprotect the data or inject too much noise into query answers.
