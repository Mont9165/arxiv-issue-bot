# [Experiment, Analysis, and Benchmark] How well do LLMs comprehend and design relational database schemata?

- arXiv ID: `2611.17044v1`
- Authors: Sriom Chakrabarti, Sean Bin Yang, Arijit Khan, Sebastian Link
- Published: 2026-11-12
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.17044v1) | [pdf](https://arxiv.org/pdf/2611.17044v1)

## Abstract

Large Language Models (LLMs) are increasingly used for database tasks, yet most work, such as Text2SQL, assumes that the relational schema already exists. We ask whether LLMs can design a schema from natural language requirements (Text2Schema), verbalize an existing schema (Schema2Text), and preserve its structure through a Schema-to-Text-to-Schema round trip. We present SchemaBridge, a benchmark of 902 schemata from three collections, stratified by size and constraint complexity, that scores fidelity separately for tables, attributes, domain (data types and nullability), entity, and referential integrity. Evaluating six open-weight and proprietary LLMs, we find that: (i) human-written requirements under-specify schemata, with no model exceeding 0.27 referential integrity F1; (ii) LLM-generated descriptions carry far more structure when explicitly asked to be complete, raising GPT-5.4-mini's referential F1 on SchemaBench from 0.228 to 0.909, even as BLEU, ROUGE-L, and BERTScore decrease; (iii) controlled experiments show that both constructor and describer choices influence round-trip fidelity under fixed settings; and (iv) masked schema experiments show that structural cues support recovery of keys and relationships, while joint data-type and nullability information is poorly retained through verbalization.
  Code and data are available at https://github.com/iamsriom/SchemaBridge
