# GPTKB 2.0: Direct Construction of Disambiguated Knowledge Bases from Large Language Models

- arXiv ID: `2608.03729v1`
- Authors: Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski
- Published: 2026-08-04
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.03729v1) | [pdf](https://arxiv.org/pdf/2608.03729v1)

## Abstract

Automated Knowledge Base Construction (AKBC) is a core NLP task, and recent work proposes generating knowledge bases directly from large language models (LLMs), treating the model itself as the knowledge source. However, LLMs natively possess no representation of entities, leading to duplicate entries as well as conflations. We propose GPTKB 2.0, a methodology for constructing disambiguated KBs directly from LLMs. GPTKB 2.0 incorporates on-the-fly disambiguation of entities, relations and classes, and is meticulously designed to satisfy both scalability and disambiguation accuracy. We analyze the central design decisions and characterize the trade-offs between accuracy, scale, and cost. We execute GPTKB 2.0 at scale, obtaining a materialized KB containing over 1M disambiguated entities and 38.4M triples. This represents the first million-scale LLM-native KB with explicit internal canonicalization of entities, relations, and classes, a significant departure from prior Wikimedia-centric works. GPTKB 2.0 is available at https://gptkb.org/.
