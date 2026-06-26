# Are LLMs Ready for Anti-Pattern Detection in Microservice Architectures?

- arXiv ID: `2606.26927v1`
- Authors: Marco De Luca, Domenico Amalfitano, Porfirio Tramontana, Anna Rita Fasolino
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.26927v1) | [pdf](https://arxiv.org/pdf/2606.26927v1)

## Abstract

Microservice systems are prone to recurrent architectural anti-patterns (APs) that hinder maintainability, evolvability, and operational quality. Most existing AP detection approaches rely on static analysis and handcrafted rules, which can be effective but are often tool-dependent, limited to explicitly encoded detection logic, and difficult to adapt to heterogeneous repositories. In this paper, we investigate whether large language models (LLMs) are ready to support architectural anti-pattern detection in microservice architectures through a prompt-based analysis pipeline over static repository artifacts. We evaluate three general-purpose LLMs on a curated benchmark of microservice repositories annotated with 16 architectural anti-patterns, and compare their performance against the state-of-the-art static-analysis tool MARS using a uniform evaluation protocol based on precision and recall. Our results show that LLMs can provide useful support for anti-pattern detection, achieving competitive performance on several anti-patterns, especially when the relevant evidence is local, heterogeneous, or semantically rich. At the same time, they exhibit clear limitations on anti-patterns that require explicit structural or cross-service dependency evidence, where static analysis remains more reliable. These findings suggest that LLMs are not yet a replacement for traditional analyzers, but already represent a promising complementary aid for architectural assessment in microservice systems.
