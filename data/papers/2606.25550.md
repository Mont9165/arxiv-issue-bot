# On the Viability of Requirements Generation From Code: An Experience Report

- arXiv ID: `2606.25550v1`
- Authors: Alexander Korn, Jone Bartel, Max Unterbusch, Andreas Vogelsang
- Published: 2026-06-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.25550v1) | [pdf](https://arxiv.org/pdf/2606.25550v1)

## Abstract

Empirical research in Requirements Engineering is hampered by a lack of adequate datasets that pair source code with corresponding requirements. A tempting route to addressing this lack is the use of Large Language Models to synthesize requirements from existing code bases. We investigate this question by evaluating an LLM-based and RAG-supported agentic approach that generates requirements from source code, verifies their implementation status relying on a human-in-the-loop, and synthetically introduces requirements smells and non-implemented requirements. Our goal was to create datasets that mimic reality and foster empirical RE research. However, during the study, various problems arose, leading to this experience report. Contrary to our initial hypotheses, LLMs were unable to (i) generate non-implemented requirements reliably, (ii) generate high quality requirements, and (iii) reliably introduce synthetic requirements smells. Furthermore, neither an LLM nor a single human-in-the-loop suffices to detect requirements smells reliably. These findings suggest that the generation of code-to-requirements datasets using LLMs is not yet viable and requires human supervision, especially for quality assurance. We critically reflect on our lessons learned and draw relevant conclusions for both researchers and practitioners.
