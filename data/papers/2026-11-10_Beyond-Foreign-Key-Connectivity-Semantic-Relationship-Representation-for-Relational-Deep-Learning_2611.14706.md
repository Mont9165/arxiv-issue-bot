# Beyond Foreign-Key Connectivity: Semantic Relationship Representation for Relational Deep Learning

- arXiv ID: `2611.14706v1`
- Authors: Noy Cohen-Shapira
- Published: 2026-11-10
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.14706v1) | [pdf](https://arxiv.org/pdf/2611.14706v1)

## Abstract

Relational databases encode information through tables and primary--foreign key constraints. Although recent Relational Deep Learning (RDL) approaches represent these databases as heterogeneous graphs, a foreign-key connection primarily specifies structural connectivity between records. Its semantic interpretation may involve additional information that is not explicitly represented by connectivity alone.
  This paper introduces a conceptual framework for constructing relationship-aware representations from relational databases. The framework distinguishes three complementary aspects: (i) schema-defined relationship semantics, including endpoint types and foreign-key roles; (ii) association entities and explicitly available relationship-level attributes; and (iii) contextual information describing the temporal and structural circumstances of a connection.
  We formulate a Relationship Representation Construction (RRC) protocol that maps relational schema elements and database records to node representations, relationship descriptors, and contextual representations. A key principle of the protocol is semantic ownership: attributes are assigned to records, relationships, or context according to their meaning, rather than merely their physical location in a database table. Ambiguous attributes are not automatically promoted to relationship features.
  The resulting representations can be incorporated into existing relational graph learning architectures through relationship-conditioned message passing. The proposed framework is complementary to recent work on relational message passing, graph transformers, and task-dependent graph construction. We discuss its conceptual foundations, illustrate the construction protocol using a multi-table database, and identify research questions and empirical evaluations required to establish its potential benefits.
