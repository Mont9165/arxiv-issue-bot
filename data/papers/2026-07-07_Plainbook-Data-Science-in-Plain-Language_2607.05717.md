# Plainbook: Data Science, in Plain Language

- arXiv ID: `2607.05717v1`
- Authors: Luca de Alfaro, Mathis Aubert, Ranjit Jhala, Eliana Pastor, Elena Baralis
- Published: 2026-07-07
- Primary category: `cs.HC`
- Categories: `cs.HC`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05717v1) | [pdf](https://arxiv.org/pdf/2607.05717v1)

## Abstract

Jupyter Notebooks have become widely adopted in data science, as they allow the sharing of reproducible computational analysis. They are, however, accessible only to people who understand computer code. To reach the broader audience of scientists interested in data analysis and computation, but unfamiliar with code, we introduce Plainbook, notebooks centered on natural language rather than code.
  Plainbook is based on two principles: promote the natural language descriptions, and verify the values. In plainbook, the natural language descriptions are preserved, rather than the resulting code; the code is generated automatically from the cell descriptions. As natural language is read top to bottom, Plainbook adopts a linear execution semantics, in which cells are guaranteed to be executed in the order in which they appear; there is no "hidden state" or out-of-order execution as in Jupyter. To allow users who may not understand code to verify the correctness of the computation, we have built into Plainbook verification mechanisms centered on values and value inspection. These include mechanisms that focus on individual cells, akin to unit tests, as well as global mechanisms. Both the linear execution semantics, and the verification mechanisms, are underpinned by a snapshot kernel that caches execution states and makes execution and verification efficient.
