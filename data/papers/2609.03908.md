# Property Testing for Recursive Query Languages

- arXiv ID: `2609.03908v1`
- Authors: Isolde Adler, Carsten Lutz, Quentin Manière, Marcin Przybyłko, Lukas Schulze
- Published: 2026-09-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2609.03908v1) | [pdf](https://arxiv.org/pdf/2609.03908v1)

## Abstract

In the context of database querying, property testing provides a framework for testing query answers with high confidence while inspecting only a sublinear part of the database, through completion queries and size queries. A fundamental result of Chen and Yoshida (2019) states that non-satisfaction of a Boolean conjunctive query $q$ is testable with a constant number of such queries and one-sided error if and only if $q$ is equivalent to an $α$-acyclic query. In this article, we initiate the study of property testing for recursive query languages, focusing on two-way regular path queries (2RPQs) and monadic Datalog. One of our main results is positive: non-answers to any 2RPQ are constant query testable with one-sided error. We extend this slightly to a certain class of monadic Datalog programs in which recursion is restricted to be linear and rule bodies must be $α$-acyclic. Turning towards unrestricted monadic Datalog, we next show that if a monadic Datalog program $Π$ is not equivalent to an $α$-acyclic program, then falsity of $Π$ is not constant query testable with one-sided error. This is under the assumption that all rule-bodies are self-join free. We leave open the case of monadic Datalog programs with $α$-acyclic rule bodies that are not restricted to linear recursion, but observe as a first step that there exist $α$-acyclic programs that are mildly non-linear and constant query testable with one-sided error.
