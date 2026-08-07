# Relational Database Data Lineage Ontology

- arXiv ID: `2605.16068v1`
- Authors: Jakub Dutkiewicz, Paweł Misiorek, Robert Wrembel
- Published: 2026-05-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.16068v1) | [pdf](https://arxiv.org/pdf/2605.16068v1)

## Abstract

Modeling data lineage in relational databases remains a challenging problem, particularly in scenarios involving incomplete or missing dependencies between database objects. In this paper, we propose a novel ontology for relational database data lineage, designed to provide a richer and more expressive semantic representation supporting discovering the lineage links by means of knowledge graphs (KGs). Building upon our previous work on KG-based lineage discovery, the proposed ontology extends the earlier model with additional concepts capturing structural, semantic, and transformation-level characteristics of relational data. These extensions enable more precise encoding of lineage evidence. To evaluate the impact of the proposed ontology, we conduct a comparative study using a KG-based inductive link prediction framework. Specifically, we assess the performance of a graph neural network model based on path embeddings under two settings: using the original baseline ontology and the newly proposed one. Experimental results demonstrate that the application of the enriched semantic model leads to improvements in lineage link prediction performance, as measured by AUC and Hits@10 metrics.
