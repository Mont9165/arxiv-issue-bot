# CodeGraph: Open-Taxonomy Knowledge Graph for Source Code with Wikidata Grounding

- arXiv ID: `2609.29474v1`
- Authors: Federico Pennino, Andrea Gurioli, Stefano Zacchiroli, Maurizio Gabbrielli, Paolo Ferragina
- Published: 2026-09-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2609.29474v1) | [pdf](https://arxiv.org/pdf/2609.29474v1)

## Abstract

Public software repositories, like GitHub and Software Heritage Archive, store billions of files, yet extracting their implicit engineering knowledge ---i.e., the algorithms they implement, the paradigms they follow, the patterns they instantiate, and the application domains they serve--- remains challenging, as current tools are constrained to syntactic and token-level analysis. We present a pipeline for building an open-taxonomy semantic annotation of source code using a code-specialised Large Language Model. The extracted entities are grounded in Wikidata through a three-stage linking procedure: a deterministic SPARQL stage handles unambiguous entities, a Deep Research Agent resolves the residual long tail, and a hierarchy-rollup stage imports the parent-of closure of each resolved Wikidata identifier. The resulting annotations are materialised as a source-code-specific open-taxonomy knowledge graph. We further introduce a calibrated quality-assurance protocol that quantifies annotation precision by combining a small human gold set with an LLM-as-a-judge filter. We applied our pipeline to the 167 million files of the Stack-Edu corpus, creating the first known large-scale open-taxonomy knowledge graph for source code. Our graph, named CodeGraph, contains approximately 158 million nodes, which include around 145 million files, about 63,000 extracted concept entities (such as algorithms, paradigms, design patterns, and application domains), and roughly 19,800 grounded Wikidata entities. Furthermore, CodeGraph features approximately 1 billion typed edges that connect files to their respective concepts, link these concepts to their grounded Wikidata identifiers, and relate them to their parent categories, covering 14 programming languages.
