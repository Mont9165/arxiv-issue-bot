# AuthentiCity: A Multi-Source Provenance-Aware Knowledge Graph and Benchmark for 3D City Models

- arXiv ID: `2607.25243v1`
- Authors: Huynh Duc An Son Nguyen, Lukas Arzoumanidis, Youness Dehbi
- Published: 2026-07-28
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.25243v1) | [pdf](https://arxiv.org/pdf/2607.25243v1)

## Abstract

Urban digital twins increasingly combine authoritative, crowd-sourced, machine-learned, and reconstructed data with differing reliability, coverage, and semantics. Yet few urban datasets provide a unified representation supporting multi-source integration, provenance tracking, spatial reasoning, and machine learning. We present AuthentiCity, a multi-source, provenance-aware 3D city knowledge graph spanning five cities across three continents (Hamburg, Helsinki, Zurich, New York, and Tokyo) and comprising 180 GiB, 180M nodes, 220M edges, 1.2B properties, and 3.6M buildings. The labeled property graphs integrate authoritative CityGML and OpenStreetMap data for all cities, adding roof-material predictions and reconstructed LoD3 geometry for Hamburg, under a provenance model in which derived information never replaces authoritative data. Confidence-weighted edges resolve cross-source correspondences, constructing canonical urban entities while preserving traceable links to contributing evidence. AuthentiCity is primarily a data contribution. We introduce two benchmark families that demonstrate the tasks enabled by the representation. The first evaluates natural-language-to-query translation beyond conventional text-to-SQL and text-to-Cypher benchmarks, including 3D spatial reasoning, provenance-aware filtering, cross-source agreement and disagreement, coverage-aware aggregation, and infeasible-query detection. The second evaluates graph representation learning through multi-source attribute prediction, node classification, and cross-source matching prediction, enabling comparison of provenance-agnostic and provenance-aware embeddings. Even a strong commercial LLM reaches only 54-69 % execution accuracy and a 7B open-weight model 6-19 %, while the open-weight model never abstains on unanswerable questions.
