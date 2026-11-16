# MEM-SQL: Memory-Empowered Text-to-SQL

- arXiv ID: `2611.18338v1`
- Authors: Xiaoqi Wang, Wenqi Pei, Shizheng Hou, Yilai Liu, Han Chen, Boyan Li, Yuyu Luo, Hongyang Du
- Published: 2026-11-13
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.18338v1) | [pdf](https://arxiv.org/pdf/2611.18338v1)

## Abstract

Text-to-SQL systems translate natural language questions into SQL queries over increasingly complex databases. However, widely used benchmarks evaluate questions independently, overlooking settings where earlier queries over the same database can supply joins or calculations for a new question. We introduce HARE (History-AwaRe Text-to-SQL BEnchmark) to measure the accuracy and cost of adapting historical SQL. HARE comprises 1,600 requests derived from a fixed pool of 823 verified queries across four datasets. Annotations record which components each request preserves and which edits it requires, distinguishing whole-query adaptation from partial reuse. Our method, MEM-SQL (Memory-EMpowered Text-to-SQL), stores whole-query templates, reusable SQL blocks, and mappings from domain concepts to schema elements. MEM-SQL uses a layer only if every requirement assigned to it has a match above that layer's threshold. With On-demand Schema Linking (OSL), MEM-SQL consults the schema only when no layer qualifies or the generator judges retrieved evidence insufficient. Across six language models on HARE, mean execution accuracy rises from 37.1% for Direct Generation without history to 50.0% for MEM-SQL, with 76.6% fewer input tokens and 68.8% lower latency on average. Further analysis shows that requests reusing several verified queries remain a bottleneck, with accuracy falling from 56.7% to 29.7%, most sharply when reused components must be placed in a new query structure or combined with a shared join. Applying OSL to three other memory designs consistently reduces generation cost, while its accuracy benefit depends on the memory design. Verified history can thus make generation both more accurate and cheaper, but its value depends on the evidence retained and when the system consults the schema.
