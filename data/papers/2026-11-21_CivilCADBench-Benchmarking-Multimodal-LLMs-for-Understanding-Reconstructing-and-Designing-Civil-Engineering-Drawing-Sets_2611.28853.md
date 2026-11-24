# CivilCADBench: Benchmarking Multimodal LLMs for Understanding, Reconstructing, and Designing Civil Engineering Drawing Sets

- arXiv ID: `2611.28853v1`
- Authors: Zelin Zheng, Difei Wu, Xinyan Liu, Minghong Chen, Antoni B. Chan, Difan Zou
- Published: 2026-11-21
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.28853v1) | [pdf](https://arxiv.org/pdf/2611.28853v1)

## Abstract

Civil infrastructure is designed, built, and maintained through engineering drawing sets, yet preparing and revising them remains labour-intensive and calls for automation. Multimodal large language models (MLLMs) are promising candidates, but assessing them requires a benchmark grounded in real engineering practice. We introduce CivilCADBench, a benchmark for understanding, reconstructing, and designing civil engineering drawing sets, built from real infrastructure drawings and source CAD files containing over 250,000 CAD entities. Unlike parametric 3D CAD models, these drawings are dense, layered, and multi-sheet; and since prints are lossy projections with no pixel trace of layers, a file can print correctly yet remain wrongly organised. CivilCADBench comprises three task families of increasing difficulty: understanding tasks are evaluated with 2,183 expert-reviewed questions ranging from single sheets to whole sets, while reconstruction and design tasks are agentic, requiring models to rebuild printed pages as editable CAD files, either as single pages or entire drawing sets, and to produce new designs. These tasks are performed across 232 pages, 28 sets, and 19 design tasks, and evaluated by a deterministic scorer that compares model outputs with the designers' source files on geometry, layers, text, and dimensions. We evaluate seven frontier MLLMs on CivilCADBench, and find that they read and redraw printed content accurately but recover the file structure poorly: the best model scores above 90% in understanding and single-page reconstruction, yet only 60% on layer assignment and 48% on design. Grounded in real engineering practice, CivilCADBench exposes both the capabilities and the limitations of frontier models in professional civil engineering, laying a foundation for next-generation models and agentic systems for intelligent civil engineering.
