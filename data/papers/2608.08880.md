# Fusing UI Structure & Semantics for Feature-Oriented App Screen Retrieval & Clustering

- arXiv ID: `2608.08880v1`
- Authors: Arun Krishna Vajjala, Yanfu Yan, Ajay Krishna Vajjala, Shrunal Pothagoni, Denys Poshyvanyk, Kevin Moran
- Published: 2026-08-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.08880v1) | [pdf](https://arxiv.org/pdf/2608.08880v1)

## Abstract

User Interface (UI) programming is challenging due to the complex abstraction gap between code and graphical software representations. To bridge this gap, UI programming tools often rely on screen retrieval and clustering, which require accurate similarity measures based on overlapping features. However, computing feature-oriented similarity is difficult because screens with similar functionality often exhibit design variations.
  To address this, we propose FRAME (ReinForced UseR InterfAce Screen EMbedding with Graphical Structural ComprEhension), a multi-modal, neuro-symbolic embedding technique. FRAME constructs symbolic, graph-based representations of UI components to encode salient relationships and capture feature patterns across different screens. It leverages large vision-language models for visual and lexical encoding, alongside a novel UI-specific computational geometry algorithm that enables weighted embedding propagation. Across three benchmarks, FRAME outperforms strong baselines by up to 13% MRR in search and 7.6 percentage points in clustering accuracy. A comprehensive ablation study further confirms the benefit of each component, demonstrating FRAME's potential for enhancing automated UI design and testing tools.
