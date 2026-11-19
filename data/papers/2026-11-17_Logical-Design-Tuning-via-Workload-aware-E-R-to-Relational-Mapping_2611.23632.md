# Logical Design Tuning via Workload-aware E/R-to-Relational Mapping

- arXiv ID: `2611.23632v1`
- Authors: Hasara Kalumin, Amol Deshpande
- Published: 2026-11-17
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.23632v1) | [pdf](https://arxiv.org/pdf/2611.23632v1)

## Abstract

Conceptual data models, like the E/R model, can provide a more stable and intuitive user-facing interface and better logical independence for applications, compared to the relational model which is forced to closely mirror the physical representation. However, this flexibility introduces a challenge as well as an opportunity: a single conceptual schema admits many semantically equivalent relational schemas, whose performance can differ substantially across workloads. Traditional mapping methods use a set of predefined transformation rules or designer-selected mapping strategies, rather than optimizing the relational realization with respect to the expected workload. In this paper, we present a cost-based framework for workload-aware conceptual-to-relational mapping. Given an E/R schema and a representative workload, our framework automatically selects an efficient relational schema by optimizing mapping decisions, including inheritance, entity and relationship representations. User-specified E/R queries are compiled into SQL over the selected relational realization, allowing existing relational query optimizers to determine the physical execution plan. Experiments on real-world-inspired schemas show that mapping choices strongly affect performance; fixed or heuristic strategies exhibit large variability across workloads, whereas our approach consistently achieves competitive performance avoiding pathological cases.
