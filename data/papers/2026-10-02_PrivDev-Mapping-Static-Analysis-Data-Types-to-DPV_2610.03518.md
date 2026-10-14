# PrivDev: Mapping Static-Analysis Data Types to DPV

- arXiv ID: `2610.03518v1`
- Authors: Simon Bernbeck, Ricardo Ramalho, Matheus Amendoeira, Juliana Alves Pereira
- Published: 2026-10-02
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.03518v1) | [pdf](https://arxiv.org/pdf/2610.03518v1)

## Abstract

Static-analysis scanners can identify personal-data types in source code, but they lack mechanisms to connect these findings to standardized privacy vocabularies. PrivDev maps 122 Bearer CLI data types to Data Privacy Vocabulary Personal Data (DPV-PD) categories and links them to potentially relevant GDPR provisions. Our approach combines deterministic mapping for 43 exact-label matches with a retrieval-grounded Large Language Model (LLM) to resolve the remaining 79 non-trivial mappings. The resulting RDF knowledge graph contains 118 ODRL policy resources that were structurally validated using SHACL. The artifact passed five complementary validation gates that cover structural correctness, query consistency, retrieval quality, LLM-based assessment, and human evaluation. In human evaluation, nine annotators produced 711 judgments, yielding a raw agreement of 0.72, Gwet's AC1 of 0.68, and Gwet's AC2 of 0.88. Our results indicate that the proposed mappings are plausible and reproducible, while also revealing ambiguities in scanner-defined data-type labels and coverage gaps in DPV-PD.
