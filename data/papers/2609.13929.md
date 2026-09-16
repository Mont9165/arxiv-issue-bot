# Specification-Driven Data Architecture Reconstruction: From Physical Code to Logical and Conceptual Specifications

- arXiv ID: `2609.13929v1`
- Authors: Oleg Grynets, Olena Pochernina, Vasyl Lyashkevych
- Published: 2026-09-12
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.13929v1) | [pdf](https://arxiv.org/pdf/2609.13929v1)

## Abstract

Legacy database migrations often begin with incomplete or outdated documentation, leaving physical data definition language (DDL) as the principal evidence of data architecture. However, DDL does not fully encode conceptual intent, and model-generated completions can be plausible without being correct. This study proposes and evaluates a provenance-aware, deterministic-first pipeline for reconstructing logical and conceptual data specifications from Oracle-oriented DDL while explicitly separating observed facts, deterministic derivations, and large language model (LLM) suggestions. The pipeline performs DDL investigation, parsing, consolidation, primary-key backfilling, type normalization, and declared relationship-graph construction before optional LLM-assisted enrichment. It preserves source provenance in the deterministic catalog and declared relationship graph, and records inferred primary-key and foreign-key candidates in a separate reviewable overlay. We evaluated the implementation on 249 artifactized schema samples comprising 1,225 SQL files. The pipeline completed 244 samples (97.99%); 52 completed samples contained no extractable DDL. Across completed samples, the deterministic path reconstructed 208 tables and recovered 278 declared foreign-key records; 168 of the reconstructed tables lacked an explicitly parsed primary key before backfilling. LLM enrichment generated 100 foreign-key candidates in 36 samples, but the parent-table admissibility rate was only 17.9% for logical-specification candidates and 17.5% for conceptual-specification candidates. These findings show that the proposed deterministic-first architecture can preserve an auditable structural baseline, quantify observed primary-key and relationship gaps, and prevent model-generated hypotheses from being silently promoted to source-grounded architectural facts.
