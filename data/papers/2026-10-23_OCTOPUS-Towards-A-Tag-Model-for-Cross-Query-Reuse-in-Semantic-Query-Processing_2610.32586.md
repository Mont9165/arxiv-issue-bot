# OCTOPUS: Towards A Tag Model for Cross-Query Reuse in Semantic Query Processing

- arXiv ID: `2610.32586v1`
- Authors: GuangXue Zhang, Nada Lahjouji, Yiming Lin, Ashwin Colaco, Sharad Mehrotra
- Published: 2026-10-23
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.32586v1) | [pdf](https://arxiv.org/pdf/2610.32586v1)

## Abstract

Large language models make it possible to pose semantic questions over diverse, multi-modal data. Recent systems give such workloads the declarative feel of a database through semantic operators: relational operators whose conditions a model judges. Most of them now run on a relational engine, yet almost none keeps what the model says past the query: every judgment is discarded on completion and paid for again the next time a query needs it. We present the tag model and tag operators, the right unit for semantic processing, and OCTOPUS, a prototype built as a middleware over DBMS. Two mechanisms are central. First, the tag: each semantic answer a model produces is written back to the relation as data, which the database engine filters, indexes, and stores as it would any other. Second, the tag operator: the unit into which common semantic operators are translated, which fixes the granularity of reuse. A model judges a tuple once, and later queries reuse that judgment as data: through relationships between predicates, a stored judgment can accept a tuple for a later predicate, eliminate one that cannot satisfy it, simplify its test, or order the search of a query that stops early. On the movie scenario of SemBench, our prototype sends the model 10 to 108x fewer rows than iPDB, ThalamusDB, Palimpzest, and LOTUS at broadly competitive quality, and three of its eight queries issue no model call at all. More broadly, a database that keeps its judgments lets its schema grow from the questions its users ask, so that each semantic answer is paid for once, stays consistent across queries, and can be audited through its provenance.
