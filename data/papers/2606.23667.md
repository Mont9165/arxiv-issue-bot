# The Table Says Otherwise: Testing LLMs with Counterfactual Relational Data

- arXiv ID: `2606.23667v1`
- Authors: Xinzhi Wang, Chunwei Liu
- Published: 2026-06-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.23667v1) | [pdf](https://arxiv.org/pdf/2606.23667v1)

## Abstract

Large language models (LLMs) are increasingly used to answer natural-language questions over structured data. However, when a table contains familiar real-world facts, it is unclear whether the model answers by reading the provided data or by recalling knowledge learned during pretraining. This distinction is important for database applications, where the provided tables should be the source of truth. In this paper, we introduce ContraTable, a paired original-counterfactual benchmark for evaluating whether LLMs ground their answers in relational tables. We build the benchmark with two aligned versions: an original database with real-world facts and a counterfactual database that preserves the same schemas, identifiers, and relationships while changing selected country, club, and player attributes. We design 214 matched questions across three levels: single-table lookup, multi-table lookup, and multi-table temporal reasoning. Experiments on commercial closed-source and open-source models show that strong instruction-tuned models can often handle direct lookup, but their reliability drops as questions require joins, comparison, and temporal reasoning. The gap between original and counterfactual accuracy reveals that models may fall back on prior knowledge when table evidence conflicts with familiar facts. These results suggest that table-QA evaluation should measure not only accuracy, but also faithfulness to the provided database.
