# ConcoLixir: Reactive LLM Discovery Oracles for Python Concolic Testing

- arXiv ID: `2606.26545v1`
- Authors: Dong Chen, Chih-Duo Hong, Fang Yu
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.26545v1) | [pdf](https://arxiv.org/pdf/2606.26545v1)

## Abstract

Concolic testing combines concrete execution with symbolic constraint solving, but Python programs expose recurring limits. Library calls can cause symbolic variables to downgrade to concrete values. Regular expressions, checksums, parsers, and other semantic operations can be hard to solve, and exploration can plateau on already covered paths. We present ConcoLixir, a reactive LLM extension for Python concolic execution. The LLM acts as a discovery oracle, not a replacement for the solver or a correctness oracle. It generates initial seeds, proposes concrete inputs after solver failures, and targets uncovered code when coverage stalls. Each candidate is executed concolically, and only observed coverage and collected path constraints guide later exploration. Across synthetic, real-world, and library targets, ConcoLixir improves mean line coverage over the baseline concolic tester without an LLM oracle by 8.6, 15.1, and 17.0 percentage points. The gains are strongest near semantic barriers and library boundaries, and the full evaluation costs \$1.63 in API charges. These results show that bounded LLM discovery can complement symbolic reasoning without replacing it.
