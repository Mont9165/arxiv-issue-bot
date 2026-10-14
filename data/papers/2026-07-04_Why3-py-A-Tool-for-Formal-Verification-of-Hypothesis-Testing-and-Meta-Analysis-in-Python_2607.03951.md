# Why3-py: A Tool for Formal Verification of Hypothesis Testing and Meta-Analysis in Python

- arXiv ID: `2607.03951v1`
- Authors: Akira Tanaka, Yusuke Kawamoto
- Published: 2026-07-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LO`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.03951v1) | [pdf](https://arxiv.org/pdf/2607.03951v1)

## Abstract

The reproducibility crisis in scientific research has received widespread recognition, thereby increasing the importance of meta-analyses that integrate statistical analyses from multiple studies. However, statistical methods often have ambiguous and implicit underlying assumptions, which can lead to their erroneous applications and interpretations. To address this issue, we propose a formal verification framework for statistical programs written in Python. Specifically, we present Why3-py, a Python front-end for the Why3 verification platform that transforms Python programs into verification-oriented WhyML representations suitable for formal verification, addressing the challenges arising from Python's dynamic typing and runtime polymorphism. Furthermore, we extend the StatWhy tool to support the verification of meta-analysis methods. These tools enable users to identify overlooked assumptions and misuse of analyses, and to verify the correctness of Python programs for hypothesis testing and for meta-analyses.
