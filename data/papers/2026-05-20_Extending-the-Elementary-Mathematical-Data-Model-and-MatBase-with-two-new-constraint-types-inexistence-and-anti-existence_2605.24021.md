# Extending the (Elementary) Mathematical Data Model and MatBase with two new constraint types: inexistence and anti-existence

- arXiv ID: `2605.24021v1`
- Authors: Christian Mancas
- Published: 2026-05-20
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.24021v1) | [pdf](https://arxiv.org/pdf/2605.24021v1)

## Abstract

This research paper introduces two new constraint types and four subtypes of database constraints added to our (Elementary) Mathematical Data Model, which are the duals of the existence and non-existence ones. They are formally defined, characterized, and exemplified with real-life instances. The well-formedness, satisfiability, coherence, and minimality of sets of all 7 subtypes of existence constraints are studied. Corresponding SQL-embedded pseudocode algorithms for managing such sets are provided and proved to be of constant complexity, sound, complete, and optimal. Also provided are algorithms for enforcing these new types of constraints, called inexistence and anti-existence. Their characterization proves that they have linear complexity in the sum of the arities of the function (Cartesian product)s involved, and are sound, complete, and optimal as well. All these algorithms were implemented in both versions of our intelligent data and knowledge base management system prototype MatBase, which automatically generates code for enforcing all the 7 subtypes of existence constraints.
