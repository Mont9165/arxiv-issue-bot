# A Datalog Framework for Conflict-Free Replicated Data Types

- arXiv ID: `2605.31569v1`
- Authors: Elena Yanakieva, Annette Bieniusa, Stefania Dumbrava
- Published: 2026-05-29
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`, `cs.LO`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2605.31569v1) | [pdf](https://arxiv.org/pdf/2605.31569v1)

## Abstract

Distributed applications increasingly support local-first collaboration over shared data, allowing multiple users to perform updates concurrently without global coordination. Such collaboration requires careful design to capture the intended semantics of the concurrent interactions.
  We introduce a declarative framework for specifying and reasoning about the semantics of conflict-free replicated data types (CRDTs) and CRDT-based applications in Datalog. The framework models CRDT semantics as executable logic programs over operation contexts, making concurrency explicit and compositional, and thus amenable to automated analysis. As one application, we use property-based testing to compare implementations. To the best of our knowledge, this is the first work to systematically use Datalog as a foundation for prototyping and analyzing complex CRDTs and their compositions.
  We evaluate our methodology using a collaborative graph data editing case study and report experimentation results assessing correctness validation and scalability with an increasing number of operations and replicas.
