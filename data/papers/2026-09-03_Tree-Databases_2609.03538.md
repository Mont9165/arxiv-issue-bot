# Tree Databases

- arXiv ID: `2609.03538v1`
- Authors: Nicolas Spyratos
- Published: 2026-09-03
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.03538v1) | [pdf](https://arxiv.org/pdf/2609.03538v1)

## Abstract

We propose a novel database model whose basic structure is a labeled, directed tree with node identities. Intuitively, the root of the tree is seen as an object (or entity), the non-root nodes as attributes of the object and the semantics of each attribute is represented by the unique path leading from the root to the attribute. We define a tree database to be a set of such trees. The trees of the database can be combined to produce new trees using a set of operations on trees that we define in the paper. The query language of our model offers two types of queries, traversal queries and analytic queries. A query (whether traversal or analytic) is always defined over a tree, which is either a tree in the database or a tree derived from other trees using tree operations. The operations on trees and the query language are both defined using a simple functional algebra whose operations are: restriction of a function, composition of functions, pairing of functions and Cartesian product of sets.
  A distinctive feature of our model is that traversal queries and analytic queries are both defined within the same formal framework; and in fact, traversal queries serve as the building blocks for analytic queries. This is in sharp contrast to the relational model, where analytic queries are defined outside the relational algebra, in the form of SQL Group-by queries. Therefore our model supports data access and data analysis within the same formal framework.
  We demonstrate the expressive power of our model by showing: (a) how our model can support inheritance in a seamless manner, (b) how one can define consistent relational databases on top of a tree database - with the tree database playing the role of an underlying semantic layer and (c) how a tree database can be used as a user-friendly interface for accessing and analyzing relational data.
