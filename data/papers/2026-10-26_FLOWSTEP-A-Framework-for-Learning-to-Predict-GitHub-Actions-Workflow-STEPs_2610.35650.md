# FLOWSTEP: A Framework for Learning to Predict GitHub Actions Workflow STEPs

- arXiv ID: `2610.35650v1`
- Authors: Jiangnan Huang, Bin Lin, Yutaro Kashiwa
- Published: 2026-10-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.35650v1) | [pdf](https://arxiv.org/pdf/2610.35650v1)

## Abstract

Continuous Integration and Delivery (CI/CD) are fundamental to modern software development, yet configuring pipelines such as GitHub Actions (GHA) workflows remains complex and error-prone. Recent work has explored Transformer-based models for GHA workflow recommendation, but existing approaches typically model workflow steps as a single homogeneous generation task. This formulation overlooks a key distinction: reusable Actions are structured, ecosystem-level components, whereas project-specific Scripts encode local build, test, and deployment semantics. Consequently, current models struggle to capture the different forms of knowledge required for accurate workflow completion. In this work, we present FLOWSTEP, a framework for GHA workflow step completion that explicitly distinguishes between Action and Script generation. FLOWSTEP combines large language models (LLMs) with contrastive learning to better capture semantic relationships among workflow contexts, Actions, and Scripts. Evaluated on established benchmarks, FLOWSTEP improves end-to-end workflow step prediction accuracy from 38.23% to 51.09%. Beyond prediction accuracy, we further study whether LLM-as-a-judge can provide a more semantic evaluation of generated workflow steps. By comparing LLM-based assessments with human annotations, we find that the best-performing model configuration reaches substantial agreement with human ground truth (Krippendorff's alpha = 0.701), suggesting that LLM-as-a-judge can serve as a scalable complement to manual evaluation.
