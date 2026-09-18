# A Policy Profile for Croissant: Refusal as a Property of the Dataset

- arXiv ID: `2609.19640v1`
- Authors: Alexander Chernov
- Published: 2026-09-17
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.19640v1) | [pdf](https://arxiv.org/pdf/2609.19640v1)

## Abstract

Croissant is the de facto machine-readable descriptor for ML datasets: JSON-LD over schema.org. Since version 1.1 it also carries data use conditions, recommending DUO and ODRL for them. What no version specifies is how any of them is evaluated: no decision procedure, no bound on evaluation cost, no outcome for a condition an implementation cannot evaluate, no record of what was checked, and nothing on composition with caller-side authority. We supply that half. An additive profile lets a dataset declare the operations it admits and the conditions under which it admits them, over a closed set of five operators whose decision procedure is given in full, so a gate decides from the descriptor alone and records what it checked. Two corpora evaluate it and their evidence is kept apart. Three descriptors that gated a real nf-core pipeline give the deployment result: decisions from a profile document match the gate's native descriptor record for record, stripping the layer leaves a valid Croissant document, and the added cost is 11.7 $μ$s against a 119 $μ$s decision. A corpus generated from the profile's grammar gives the breadth, covering every operator, refusal class and conformance clause. Across its valid cases, 552 complete decision records agree three ways -- native descriptor, profile terms, and the same policy as ODRL in usageInfo. The carrier is therefore not the contribution; the evaluation semantics is. Finally, caller-bound and data-bound policies range over non-overlapping state spaces, so neither permit set contains the other.
