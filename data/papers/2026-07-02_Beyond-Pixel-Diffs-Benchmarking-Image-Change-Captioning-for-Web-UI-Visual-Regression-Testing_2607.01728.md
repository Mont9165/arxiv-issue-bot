# Beyond Pixel Diffs: Benchmarking Image Change Captioning for Web UI Visual Regression Testing

- arXiv ID: `2607.01728v1`
- Authors: Licheng Zhang, Bach Le, Pengtao Zhao, Naveed Akhtar
- Published: 2026-07-02
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01728v1) | [pdf](https://arxiv.org/pdf/2607.01728v1)

## Abstract

Visual regression testing (VRT) is a standard quality assurance step in modern software release pipelines. On every change, it re-renders user interface (UI) screenshots, compares each one against an approved baseline image, and routes any detected difference to a human reviewer who decides whether it is an intended update or an unintended regression. A widely used approach, especially in open-source and continuous-integration pipelines, is pixel-level comparison, which is semantically blind and treats rendering noise and genuine defects identically, producing large volumes of false positives that force developers and testers to spend substantial time and effort manually reviewing flagged differences at every release cycle. Industry tools apply machine learning to VRT, but lack public evaluation. More critically, no dataset or benchmark exists to support natural language descriptions of UI changes, a capability that tells testers what changed in words instead of leaving them to interpret a binary flag or a highlighted region. To address the gap, we propose a new task, Web UI Image Change Captioning (WUICC), which sits at the intersection of VRT and image difference captioning (IDC), and release WUICC-bench, its first dataset and benchmark for the task. We evaluate eleven representative IDC methods, together with two zero-shot general-purpose LLMs. We find that: (1) these methods tend to struggle in the Web UI domain due to its layout diversity, dense text, and fine-grained changes, and (2) yet the trained methods already suppress non-meaningful visual noise far more selectively than the pixel-level comparison VRT relies on, providing a solid foundation for future domain-specific research.
