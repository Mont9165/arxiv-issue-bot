# Time to Move on: Querying without Nulls and Bags

- arXiv ID: `2608.10863v1`
- Authors: Molham Aref, Leonid Libkin, Wim Martens
- Published: 2026-08-11
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2608.10863v1) | [pdf](https://arxiv.org/pdf/2608.10863v1)

## Abstract

SQL is the database community's success story in terms of language design. The key reason for its success is its declarativeness: it gives rise to optimizability, reducing the programmer's burden significantly. However, given the evolving complexity of problems to solve with query languages, our community needs to re-think some of the fundamental early query language design decisions. Our experience in having worked on the design of Rel (a language for end-to-end relational programming) tells us that it is possible to design, implement, and successfully deploy a language based on fully normalized relations. Such relations avoid what Codd called corrupted relations and what we commonly refer to as bags, and the 'harmful' 'billion dollar mistake' that we know as nulls. In the SQL world, it is accepted that bags and nulls are tolerated as an unavoidable evil. We argue that the evil is completely avoidable: reasons offered for justifying bags and nulls evaporate at a closer examination. In addition to debunking them, we also describe opportunities offered by a null-free language with set semantics.
