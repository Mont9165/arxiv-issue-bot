# JoinGR: Learning to Traverse Join Graphs for Table Retrieval

- arXiv ID: `2610.01064v1`
- Authors: Sandipan De, Abhijit Chakraborty, Sambaran Bandyopadhyay, Vivek Gupta
- Published: 2026-10-01
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2610.01064v1) | [pdf](https://arxiv.org/pdf/2610.01064v1)

## Abstract

Retrieving the right tables is a prerequisite for Text-to-SQL over realistic databases. Dense table retrievers rank schema elements independently, but this ignores a key source of evidence: some required tables are not mentioned in the question and become identifiable only through their join relationships to already relevant tables. We introduce JOINGR, a join-aware table retrieval method that treats the database join graph as the retrieval space. Columns are represented as graph nodes, while intra-table and foreign-key relationships are represented as typed edges. Given a question, JOINGR selects semantically similar anchor tables, traverses join edges with a query-conditioned scorer, and aggregates the resulting edge deposits into table scores. The scorer is a lightweight MLP on top of frozen query, node, and edge embeddings, trained with a pairwise margin loss over gold tables. On BIRD and Spider datasets, JOINGR is competitive with the strongest retrieval baselines. On BEAVER, a challenging enterprise benchmark with multi-hop table requirements, JOINGR substantially improves recall over dense retrieval and re-ranking baselines. Cross-domain experiments show that the learned scorer transfers across benchmarks, indicating that the method captures reusable joingraph traversal behavior.
