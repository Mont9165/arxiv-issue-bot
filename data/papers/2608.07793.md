# Reduce Once, Verify Many: Verifying Isolation Guarantees via Hierarchical Abstractions

- arXiv ID: `2608.07793v1`
- Authors: Shabnam Ghasemirad, Christoph Sprenger, Si Liu, David Basin
- Published: 2026-08-07
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.DB`, `cs.DC`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2608.07793v1) | [pdf](https://arxiv.org/pdf/2608.07793v1)

## Abstract

We present a mathematically rigorous, systematic approach for the verification of database isolation guarantees, which (i) supports a spectrum of seven isolation levels, (ii) uncovers a fundamental dichotomy among isolation levels: stronger levels can be verified via refinement alone, whereas weaker levels additionally require reduction, and (iii) provides a hierarchy of abstract models that substantially simplifies proofs by factoring out their most labor-intensive parts. In particular, we eliminate the need for per-protocol reduction proofs for the weaker class of isolation levels by performing a once-and-for-all reduction at a high level of abstraction in our hierarchy. To achieve this, we develop and apply a generic theory of reduction, which is also of more general interest. Overall, our approach minimizes the user's proof effort to a single, simpler refinement of the most concrete model in our hierarchy. All our results are formalized in Isabelle/HOL.
