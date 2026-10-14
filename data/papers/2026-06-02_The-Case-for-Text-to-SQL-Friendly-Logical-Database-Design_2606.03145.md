# The Case for Text-to-SQL Friendly Logical Database Design

- arXiv ID: `2606.03145v1`
- Authors: Shi Heng Zhang, Zhengjie Miao, Jiannan Wang
- Published: 2026-06-02
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.03145v1) | [pdf](https://arxiv.org/pdf/2606.03145v1)

## Abstract

Logical database design has traditionally optimized database schemas, including tables, columns, keys, constraints, and views, for correctness, integrity, and human-written application queries. LLM-based Text-to-SQL changes the consumer: the schema is now often read as text by a language model, so design choices that preserve database semantics can still change SQL-generation accuracy. We argue that this creates a new design objective alongside the classical ones - LLM-friendly logical database design, the property that a schema is easy for a language model to map from natural language to correct SQL - and treat it as the optimization target of this paper. We instantiate this objective with three semantics-preserving schema transformations that re-purpose classical schema-design ideas: schema abstraction (+A: logical views that materialize recurring join paths), schema partitioning (+P: workload-aware logical partitions that prune irrelevant context), and schema renaming (+R: descriptive identifiers that improve downstream column linking and predicate construction). The three operators compose, and each preserves the underlying database semantics. When historical question-SQL pairs are available, they guide both partitioning and abstraction; in zero-shot settings, renaming applies directly, and abstraction falls back to an ad-hoc per-question variant. We evaluate the resulting schemas on BIRD-Union and Spider-Union across multiple Text-to-SQL pipelines and language model backbones, with gains of up to 4.2% in execution accuracy. The best transformation varies modestly across pipelines and models, with the full +A+P+R consistently improving; multiple operator combinations are competitive on each pipeline. These results show that LLM-friendly logical design is a practical and underexplored database-side optimization target, complementary to existing Text-to-SQL pipelines.
