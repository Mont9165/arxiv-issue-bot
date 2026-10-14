# GS-QA: A Benchmark for Geospatial Question Answering

- arXiv ID: `2605.22811v1`
- Authors: Majid Saeedan, Muhammad Shihab Rashid, Ahmed Eldawy, Vagelis Hristidis
- Published: 2026-05-21
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.22811v1) | [pdf](https://arxiv.org/pdf/2605.22811v1)

## Abstract

Recent advances in Large Language Models (LLMs) have led to dramatic improvements in question answering (QA). To address the challenge of evaluating QA systems, standardized benchmarks have been introduced. This work focuses on the problem of geospatial QA, where a large collection of geospatial data is available in the form of a spatial database or other forms. Existing work on geospatial QA benchmarks has various limitations, including a small number of questions, limited spatial predicates, narrow output types, and no multi-source reasoning. We present GS-QA, an extensible geospatial QA benchmark with 2,800 question-answer pairs across 28 templates on top of OpenStreetMap and Wikipedia data, covering a wide range of spatial objects, predicates (including directional and towards filtering), and answer types (entity names, locations, distances, directions, counts, and aggregated areas/lengths). A key feature of GS-QA is that some questions require combining information from multiple sources, e.g., geospatial information from OSM and factual information from Wikipedia. GS-QA includes a comprehensive evaluation methodology that combines text-based QA measures with geospatial-specific measures such as distance error and angular error. We implemented nine LLM-based geospatial QA baselines using three LLMs (GPT-4o, Claude Sonnet 4.6, and Ministral-3) with combinations of direct prompting, retrieval-augmented generation, and text-to-SQL. Our results show that existing solutions perform reasonably well on simple spatial predicates with entity name outputs, but accuracy degrades significantly for questions involving complex spatial predicates, numeric output types, and multi-source reasoning, demonstrating that geospatial QA remains a challenging open problem warranting further research.
