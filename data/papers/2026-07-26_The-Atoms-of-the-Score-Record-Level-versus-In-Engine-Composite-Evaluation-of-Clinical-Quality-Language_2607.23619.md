# The Atoms of the Score: Record-Level versus In-Engine Composite Evaluation of Clinical Quality Language

- arXiv ID: `2607.23619v1`
- Authors: Angelo Kastroulis
- Published: 2026-07-26
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CE`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2607.23619v1) | [pdf](https://arxiv.org/pdf/2607.23619v1)

## Abstract

Clinical Quality Language (CQL) engines serve two axes: decision support (evaluate one patient, now) and quality measurement (score a population). The composite score is rarely the end product, because the individual determinations behind it are what let a score be inspected, attributed, and acted on. Two architectures follow from where aggregation happens: one computes the composite inside the engine over the whole store (no data movement); the other evaluates individual records and lets the composite be totaled externally, keeping every intermediate available.
  Mercury is a purpose-built CQL database engine of the second kind. It treats CQL evaluation as a database problem -- FHIR stored in a compact binary encoding keyed patient-first, indexes derived from what CQL retrieves filter on, a planner selecting access paths, CQL as the query language -- rather than as in-memory interpretation over a generic FHIR store. We evaluate Mercury 2.0.1 against Blaze 1.10.1, among the fastest CQL evaluators, using Blaze's own published benchmark suite on identical AWS hardware over a 100,000-patient Synthea corpus (112.3M resources).
