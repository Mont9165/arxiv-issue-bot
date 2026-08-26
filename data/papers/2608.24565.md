# MGQL: An Executable, Small-Step Semantics of GQL

- arXiv ID: `2608.24565v1`
- Authors: Aditya Thimmaiah, Tong-Nong Lin, Milos Gligoric
- Published: 2026-08-25
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.24565v1) | [pdf](https://arxiv.org/pdf/2608.24565v1)

## Abstract

ISO Graph Query Language (GQL) is the first international standard for property graph-based graph query languages, standardized as ISO/IEC 39075 in 2024. However, ISO/IEC 39075 codifies its semantics informally across 600+ pages of prose, making it difficult to formally reason about the standard or for a standard-faithful implementation. Existing formalizations are not adequate because they either: (1) significantly reduce the semantic complexity by omitting bag semantics, schemas, and composite queries on multiple graphs; (2) or significantly reduce the syntactic complexity by only considering isolated fragments such as pattern-matching, leaving the full query pipeline unformalized. Yet it is these semantic-syntactic features that make formalizing GQL non-trivial. We present MGQL, the first mechanized, small-step operational semantics for a substantial read-only fragment of GQL that is grounded in the ISO/IEC 39075 standard. Our formalization models multi-graph property graphs with mixed edge directionality and supports a large fraction of GQL pattern constructs: quantified paths and edges, directional and undirected matching, label expressions, pattern lists, and composite queries. The semantics is supported by a schema-aware type system that refines variable types via closed-graph schemas, tracks nullability, supports multiple composite query operators, and models quantified-path bindings with list types. We prove that our type system is sound, ensuring an end-to-end guarantee of well-formed queries yielding results that conform to their declared schemas. MGQL provides the first bridge between GQL's informal specification and a mechanized implementation, enabling formal reasoning about correctness.
