# A Semantic Model of Genetic Evidence: A Step Toward Bridging the Basic-Science-Clinic Gap

- arXiv ID: `2609.04509v1`
- Authors: Michael Bouzinier, Dmitry Etin
- Published: 2026-09-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `q-bio.GN`
- Links: [abs](http://arxiv.org/abs/2609.04509v1) | [pdf](https://arxiv.org/pdf/2609.04509v1)

## Abstract

Scientific and clinical decision-making depends on evidence from the primary literature, but existing standards for representing that evidence (FHIR Evidence, ECO, SEPIO, and the GA4GH Genomic Knowledge Standards) are oriented toward clinical-trial workflows, evidence codes, or single-variant assertions, and do not capture the fine-grained, domain-specific structure of claims in basic and pre-clinical research. We introduce a semantic model for scientific evidence with three core classes, specialize it for genetics, align it structurally to FHIR Evidence with a SEPIO-anchored credibility decomposition, and attach a compact dimensional vocabulary whose conditional-activation rules are validated by a SHACL schema for the implemented constraints. Using clinical variant interpretation as the driving use case, we evaluate the model through a human-AI annotation pilot over six genetics papers, yielding 28 evidence items and 95 source-anchored assertions, with a workflow that keeps curator-authored reference annotations distinct from AI-drafted annotations. Treating the pilot as a feasibility study rather than a benchmark, we argue that the model is a useful increment toward trustworthy, AI-ready infrastructure for variant interpretation: a reference data model and validation schema for representing genetic evidence.
