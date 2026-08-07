# Neuro-Relational Programs: Unifying Queries and Neural Computation over Structured Data

- arXiv ID: `2606.11946v1`
- Authors: Arie Soeteman, Balder ten Cate, Maurice Funk, Benny Kimelfeld, Carsten Lutz, Moritz Schönherr
- Published: 2026-06-10
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CC`, `cs.LG`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2606.11946v1) | [pdf](https://arxiv.org/pdf/2606.11946v1)

## Abstract

The conventional approach to deep learning over relational databases applies neural models, such as Graph Neural Networks (GNNs), to a graph representation of the database. Recent approaches instead operate on databases directly, associating tuples with embeddings and extending query mechanisms to jointly process embeddings and relational content. Inspired by these developments, we introduce Neuro-Relational Programs (NRPs), a declarative query language for relational databases whose facts carry numeric vector embeddings. NRPs extend Datalog-style rules with operations that combine, aggregate, and transform embeddings, thereby interleaving relational reasoning and learnable neural components within a single formalism. This yields a general approach to neural computation over relational data: an NRP can be read both as a query plan with trainable components and as a neural architecture with relational structure built in.
  Natural syntactic fragments of NRPs recover existing architectures and query formalisms. Zero-ary NRPs correspond to non-adaptive query algorithms; monadic NRPs generalize GNN-style message passing and precisely capture Deep Homomorphism Networks, a connection that we extend to frontier-guarded NRPs over databases with row-ids. We characterize the expressive power of unrestricted NRPs with ReLU-FFN transformations by FOCQ, an extension of first-order logic with counting interpreted over real-weighted structures, yielding a precise connection with uniform TC$^0$ over ordered databases. Together, these results establish NRPs as a broad declarative framework for querying and neural computation over relational data.
