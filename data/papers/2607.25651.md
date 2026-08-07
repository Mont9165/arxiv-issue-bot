# Demystifying Deep Learning Compiler Frontend Bugs: An LLM-Aided Empirical Study

- arXiv ID: `2607.25651v1`
- Authors: Xinyi Yuan, Wei Chen, Jinyi Liu, Pengyu Chen, Jun Wei, Guoquan Wu, Jiaxin Zhu, Tao Huang
- Published: 2026-07-28
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.25651v1) | [pdf](https://arxiv.org/pdf/2607.25651v1)

## Abstract

Deep learning compilers (DLCs) are designed to translate deep learning programs into optimized, hardware-specific code. Typically, DLC frontends translate programs into graph-based intermediate representations (IRs) to enable optimizations. Defects introduced during this stage (termed \emph{fBug}s) are severe yet understudied, as prior work predominantly focuses on low-level APIs and operators or treats DLCs as monolithic entities.
  To bridge this gap, we conduct the first systematic empirical study of \emph{fBug}s in TorchDynamo, the default DLC frontend for PyTorch 2, the most popular DL framework. Leveraging a domain-knowledge-enhanced LLM-aided methodology, we analyze 123 \emph{fBug}s and construct a taxonomy comprising 7 root cause categories and 15 subcategories. Our findings provide actionable insights for DLC development and testing. Furthermore, we leverage the LLM to generate targeted, root cause-aware test cases to detect new bugs. We uncovered 23 previously unknown \emph{fBug}s in recent releases (15 confirmed) across eight (sub)categories, demonstrating the efficacy of our methodology in testing and hardening DLC frontends.
