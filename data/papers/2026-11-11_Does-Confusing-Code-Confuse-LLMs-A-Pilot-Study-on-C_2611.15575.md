# Does Confusing Code Confuse LLMs? A Pilot Study on C++

- arXiv ID: `2611.15575v1`
- Authors: Tim van de Wetering, Lola Solovyeva, Fernando Castor
- Published: 2026-11-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.15575v1) | [pdf](https://arxiv.org/pdf/2611.15575v1)

## Abstract

Large language models (LLMs) are increasingly deployed for software maintenance tasks that depend heavily on code comprehension. While atoms of confusion, minimal code patterns empirically shown to impair human program comprehension, are well studied, it remains unclear whether these same patterns affect LLMs, and whether their impact varies across maintenance tasks. We present a pilot study evaluating the impact of atoms of confusion on LLM performance on C++ code drawn from three production libraries, using ChatGPT and GitHub Copilot on three software development tasks: atom injection and removal, output prediction, and code explanation. Our results reveal three preliminary findings: (i) the impact of atoms on LLMs is strongly task-dependent; (ii) atoms requiring reasoning about surrounding code are the most resistant to transformation, while localized syntactic atoms are handled reliably; and (iii) LLMs remove atoms of confusion more reliably than they inject them, suggesting that removal succeeds through pattern matching while injection requires deeper comprehension.
