# CypherGuard: Database-Grounded Correction for Reliable Text-to-Cypher

- arXiv ID: `2610.41755v1`
- Authors: Zebin Chen, Dong Wen, Makbule Gulcin Ozsoy, Wenjie Zhang
- Published: 2026-10-30
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.41755v1) | [pdf](https://arxiv.org/pdf/2610.41755v1)

## Abstract

Text-to-Cypher translates natural-language questions into Cypher queries over property graphs. Graph database systems increasingly adopt this translation as a native query interface. Large language models generate fluent Cypher but stay unreliable. On Cypher-Bench a small model answers only 31.4% of questions correctly, and even a strong model plateaus at 71.76%. The dominant failure modes are structural rather than linguistic. For example, a generated query may parse correctly and follow the schema, yet still return zero rows because it traverses a relationship against the stored graph direction. To address this issue, we present CypherGuard, a training-free framework that detects and corrects these structural faults. Our approach uses two core components: a graph-native error taxonomy to guide repair, and a mined rule library to guide query generation. At inference time, CypherGuard first rewrites schema-detectable faults, then re-executes each draft and repairs it only when the query errors or returns nothing. On CypherBench test questions, across seven graphs, CypherGuard reaches 88.50% overall execution accuracy, +25.08% over the same-backbone zero-shot floor, surpassing an RL-fine-tuned 7B specialist and the strongest training-based system that we compare against.
