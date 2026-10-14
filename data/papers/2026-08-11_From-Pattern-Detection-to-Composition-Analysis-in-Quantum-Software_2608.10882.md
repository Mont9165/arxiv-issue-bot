# From Pattern Detection to Composition Analysis in Quantum Software

- arXiv ID: `2608.10882v1`
- Authors: Neilson Carlos Leite Ramalho, Erico Augusto da Silva, Anthony Accioly, Higor Amario de Souza, Marcos Lordello Chaim
- Published: 2026-08-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2608.10882v1) | [pdf](https://arxiv.org/pdf/2608.10882v1)

## Abstract

Quantum software patterns provide high-level abstractions for building quantum programs, but there is still little empirical evidence on how they are adopted in practice. In prior work, we extended an existing quantum-pattern atlas into a 61-pattern catalog, created a knowledge base that links framework components to those patterns, and built a tool that mines pattern implementations from open-source code. We applied this tool on 80 projects and find that all 23 patterns occur in practice. In this work, we extend the tool with two additional matching channels and a vocabulary expansion step, and execute a quantitative evaluation of its accuracy on Qrisp, a framework not present in the knowledge base, reaching a micro-F1 of 0.712 against 0.449 without the expansion step. We then construct composition graphs that record calls among the high-level framework components associated with patterns and store them in a graph database. We use these graphs to examine how pattern implementations are assembled inside each framework, why patterns co-occur, and how much of a pattern's detection count comes from components called directly by developers rather than introduced through internal framework calls. We release qpa, an open-source mining pipeline, together with the knowledge base, which maps 286 framework components across five sources to the pattern catalog, maintained with the support of an LLM ensemble that classifies newly extracted components, and the resulting pattern usage dataset, to support reproducible studies on the adoption and evolution of quantum patterns.
