# One Index for Subsumption and Roll-up across Time, Geography, and Ontology

- arXiv ID: `2606.24677v1`
- Authors: Madhulatha Mandarapu, Sandeep Kunkunuru
- Published: 2026-06-23
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.24677v1) | [pdf](https://arxiv.org/pdf/2606.24677v1)

## Abstract

Time-series, geospatial, and ontology systems each maintain a hierarchy -- day <= month <= year, zip <= city, is-a / part-of -- and each indexes it in a separate silo. We observe these are all subsumption posets, with one recurring workload: order testing (is x under y?) and hierarchical roll-up (aggregate a measure over everything under y). We present OEH, a single declarable index that, by a cheap structural probe, encodes a hierarchy as a nested-set order-embedding (trees) or a chain decomposition (low-width DAGs), and answers both subsumption and index-resident monoid roll-up from one structure. On five real hierarchies -- Gene Ontology, NCBI Taxonomy (1.3M), GeoNames (330k), a 2.6M-node calendar, and git commit DAGs -- OEH on trees matches a 2-hop index on query latency using about half the space and building 6--7x faster, and adds roll-up that 2-hop cannot. Its roll-up matches TimescaleDB's continuous aggregates exactly and in the same latency regime, while also answering subsumption. On high-width DAGs the chain index is declined and 2-hop dominates. Order-embedding is classical; our contribution is the unification and the structure-selected index over subsumption and index-resident roll-up.
