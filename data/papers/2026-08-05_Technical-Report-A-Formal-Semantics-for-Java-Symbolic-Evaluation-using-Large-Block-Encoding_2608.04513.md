# Technical Report: A Formal Semantics for Java Symbolic Evaluation using Large-Block Encoding

- arXiv ID: `2608.04513v1`
- Authors: Soha Hussein, Stephen McCamant, Kelton OBrien, Kuen-Bang Hou, Michael Whalen, Vaibhav Sharma
- Published: 2026-08-05
- Primary category: `cs.SC`
- Categories: `cs.SC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.04513v1) | [pdf](https://arxiv.org/pdf/2608.04513v1)

## Abstract

Symbolic execution plays a critical role in software reliability, as they are used to find bugs, generate test cases, and provide correctness guarantees, particularly for safety-critical systems. Yet their own correctness is rarely subject to formal scrutiny, as it is typically established empirically by evaluating tool behavior across many programs. This leaves open the possibility that the tools themselves introduce unsoundness, potentially invalidating the verification results they produce and undermining the very guarantees they are meant to provide.
  In this paper, we address this gap by providing the formal treatment of symbolic execution with path-merging, an optimization that improves path explosion by summarizing branching code regions into disjunctive constraints rather than exploring each path independently. Specifically, we target Java Ranger, a path-merging tool for Java programs that progressively transforms imperative Java code toward the language of formal logic through a series of code transformations. We formalize each of these transformations and prove their soundness with respect to a simplified version of the Java concrete semantics, establishing that Java Ranger's path-merging process preserves program semantics.
