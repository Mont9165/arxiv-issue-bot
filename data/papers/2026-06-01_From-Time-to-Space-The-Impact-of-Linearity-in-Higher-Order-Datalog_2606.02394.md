# From Time to Space: The Impact of Linearity in Higher-Order Datalog

- arXiv ID: `2606.02394v1`
- Authors: Angelos Charalambidis, Babis Kostopoulos, Panos Rondogiannis
- Published: 2026-06-01
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.CC`, `cs.DB`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2606.02394v1) | [pdf](https://arxiv.org/pdf/2606.02394v1)

## Abstract

We consider a fragment of Higher-Order Datalog with negation and argue that it generalizes the familiar and important fragment of Linear Datalog. We investigate the expressive power of this fragment, establishing a tight connection with the hierarchy of space complexity classes. In particular, we demonstrate that for all $k \ge 1$, the $(k+1)$-order fragment of Stratified Linear Higher-Order Datalog$^\neg$ captures $(k-1)$-EXPSPACE. This result suggests that restricting programs to linear recursion shifts the expressive power of the corresponding fragments from time to space, generalizing the classical result that (Stratified) Linear Datalog captures NL. Unlike the first-order setting where an ordering assumption is required to capture NL, our results hold without any such assumption on the input database. The proof relies on simulating space-bounded Turing machines using Stratified Linear Higher-Order Datalog$^\neg$ programs and providing a space-efficient evaluation of the query program. We argue that identifying such computationally well-behaved fragments is a crucial step towards paving the way for practical implementations of Higher-Order Datalog.
