# Non-Functional Requirements to Hyperparameter Translation for Quantum Software via LLMs

- arXiv ID: `2611.16902v1`
- Authors: Joseph G. Bronyah, Nasir U. Eisty
- Published: 2026-11-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.16902v1) | [pdf](https://arxiv.org/pdf/2611.16902v1)

## Abstract

Quantum software engineering (QSE) lacks validated approaches for translating natural-language non-functional requirements (NFRs) into execution parameters such as shots and transpiler optimization levels. Existing methods emphasize semantic similarity rather than execution outcomes. We evaluate seven large language models (LLMs) against a deterministic heuristic baseline using 540 synthetic and 18 real-world user stories. We assess semantic accuracy and execution outcomes, including time, cost, top-state probability, and two-qubit gate exposure, through Qiskit/Aer simulations. All LLMs significantly outperformed the heuristic in semantic accuracy, achieving 55.6 to 83.3 percent on real-world stories compared to 16.7 percent for the heuristic. However, no LLM demonstrated statistically significant superiority over others on the real-world dataset. Speed- and cost-oriented configurations reduced execution time and cost, but fidelity improvements were not supported. Some failures resulted from provider safety refusals rather than translation errors. Our findings demonstrate the potential of LLMs as middleware for NFR-to-configuration translation in QSE, while emphasizing execution-based validation, human oversight, and careful interpretation of model differences.
