# VISTA Architect: A graph database-oriented health AI system demonstrated in multidisciplinary tumor boards

- arXiv ID: `2606.22692v1`
- Authors: Tuomo Kiiskinen, Jason Fries, Philip Adamson, David Wu, Timothy John Ellis-Caleo, Aaron Fanous, Balasubramanian Narasimhan, Joel Neal, Sylvia Plevritis, Manuel A. Rivas
- Published: 2026-06-21
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2606.22692v1) | [pdf](https://arxiv.org/pdf/2606.22692v1)

## Abstract

We introduce VISTA Architect, a database-oriented AI architecture for integrating large language models (LLMs) with longitudinal electronic health records (EHRs). At ingestion, it transforms complex clinical documentation into a persistent, provenance-linked knowledge graph, eliminating repeated reprocessing of raw records at query time. The architecture has two layers: a source-faithful MEDS Graph preserving granular EHR structure with full provenance, and a clinically abstracted Timeline Object Architecture (TOA) that uses graph-guided LLM extraction to synthesize a concise timeline of deduplicated, temporally coherent clinical events. This addresses key limitations of direct long-context prompting and retrieval-augmented generation (RAG), which often miss temporal relationships and incur high cost and latency from repeated raw-text processing. By precomputing clinical synthesis once, downstream queries access an organized patient state and traverse to source documentation only when detailed verification is needed.
  We demonstrate the system in multidisciplinary thoracic oncology tumor boards at Stanford Medicine, where precise reconstruction of patient histories is critical. Across 1,180 patients, VISTA Architect achieved 96.4% accuracy (mean 9.75/10) on 15 tumor board-salient variables (17,700 evaluations; 95% CI 96.1-96.7%), surpassing a matched BM25 RAG baseline and recent benchmarks for LLM-based clinical extraction. An agentic interface reduced preparation for a 30-patient held-out cohort to about 2.2 minutes without sacrificing accuracy. While configured here for thoracic oncology, the modular design adapts to other specialties through customizable event definitions, episode structures, and agentic tools; validation beyond thoracic oncology remains future work.
