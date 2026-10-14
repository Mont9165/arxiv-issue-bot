# Toward Inferring Accurate Context-free Grammars for Big Languages in a Black-box Setting

- arXiv ID: `2607.08959v1`
- Authors: Mohammad Rifat Arefin, Nuhiat Arefin, Shanto Rahman, Christoph Csallner
- Published: 2026-07-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.08959v1) | [pdf](https://arxiv.org/pdf/2607.08959v1)

## Abstract

Black-box context-free grammar inference is crucial for program analysis, reverse engineering, program understanding, fuzzing, and security. But existing approaches such as Arvada, TreeVada, Kedavra, and Cucio struggle with scalability, accuracy, and grammar readability, especially on larger languages. To address this challenge, Xvada introduces several new techniques for deterministic inference of context-free grammars. In an empirical comparison that avoids several pitfalls of recent studies, Xvada improves on the highest-scoring competitor (TreeVada) both in grammar accuracy and grammar compactness. Xvada also found a CVE in the widely used Python Liquid engine. Fuzzing based on the XVada-inferred grammar found five more bugs, which the Python Liquid developers fixed based on our bug reports. XVADA and all experimental data and scripts are freely available.
