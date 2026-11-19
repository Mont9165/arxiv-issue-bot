# ProvCards: Artifact-Oriented Provenance for Heterogeneous Scientific Workflows

- arXiv ID: `2611.24894v1`
- Authors: Tanja Auge, Marinus Holitschke, Meike Klettke
- Published: 2026-11-18
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.24894v1) | [pdf](https://arxiv.org/pdf/2611.24894v1)

## Abstract

Reproducibility in scientific workflows is hindered by heterogeneous components and execution environments, as well as fragmented provenance capture. Although existing approaches offer established semantics and workflow-specific solutions, provenance remains difficult to capture, exchange, and compose across workflow boundaries. We present ProvCards, an artifact-oriented approach that treats provenance as a first-class artifact grounded in the W3C PROV Data Model. Individual workflow components can generate cards that are stored, exchanged, reused, and composed independently of any workflow system or centralized execution context. ProvDecks group related cards into portable scopes while preserving their identities. ProvGraphs provide derived views for provenance reconstruction, querying, visualization, and analysis. Together, these representations support coherent, task-specific provenance views across heterogeneous components, facilitating traceability, reuse, and reproducibility. We implement ProvCards using a graph-based infrastructure and evaluate them in a scientific data-processing workflow. The results demonstrate independent provenance capture at the component level, composition across component boundaries, and reconstruction for querying and analysis. ProvCards provide a portable, composable, and incrementally extensible foundation for provenance management in heterogeneous scientific workflows.
