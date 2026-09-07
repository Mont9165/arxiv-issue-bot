# Dynamic Adaptation of the LLM Context for Generating Routines with Coupled Semantics

- arXiv ID: `2609.04570v1`
- Authors: Gnaneswar Villuri, Hashmath Shaik, Alex Doboli
- Published: 2026-09-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.04570v1) | [pdf](https://arxiv.org/pdf/2609.04570v1)

## Abstract

LLM-based code generation fails when correctness depends on execution-dependent coupling: the meaning of one routine is defined by the runtime behavior of another, a relationship that cannot be resolved from textual descriptions alone. This limitation, which we call static binding, is not confined to explicitly coupled problems; it appears to varying degrees whenever correctness depends on joint execution behavior across components, from explicit cross-coupled optimizers to subtler joint constraints in packing, routing, and symbolic search. This paper proposes dynamic context adaptation, a sample-efficient validation-generation loop designed for this setting. A validation agent extracts structured diagnostic information from execution traces, providing gradient-like guidance to a generation agent that proposes multiple candidates per iteration. A knowledge graph derived from the problem description supplies semantic constraints to the generation agent. Simulated annealing selects among candidates to avoid greedy collapse. Our method outperforms zero-shot, Reflexion, and OpenEvolve on seven of eight problems at both 300 and 600 evaluations (p < 0.01), a regime where population-based search has not yet accumulated sufficient diversity to compete. Notably, on the primary motivating problem (cross-coupled optimization), our method also achieves the best score at 1000 evaluations, consistent with the hypothesis that structured execution feedback is most beneficial when correctness depends on runtime coupling. Ablation results confirm that structured execution feedback is the primary driver.
