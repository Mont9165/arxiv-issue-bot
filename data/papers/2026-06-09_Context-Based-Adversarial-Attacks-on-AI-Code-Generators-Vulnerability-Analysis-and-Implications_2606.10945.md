# Context-Based Adversarial Attacks on AI Code Generators: Vulnerability Analysis and Implications

- arXiv ID: `2606.10945v1`
- Authors: Walther A. Del Orbe, John D. Hastings, Varghese Vaidyan
- Published: 2026-06-09
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.10945v1) | [pdf](https://arxiv.org/pdf/2606.10945v1)

## Abstract

AI-powered code generation systems have transformed software development but introduce critical inference-time security vulnerabilities. This research presents a systematic investigation of context-based adversarial attacks, where strategically crafted contextual inputs, including comments, documentation, variable names, bias large language models toward generating exploitable code. Through 2,800 controlled experiments across CodeT5+, CodeLlama, GPT-3.5-Turbo, and GPT-4, we quantify attack effectiveness and defense mechanisms. Results demonstrate that adversarial conditions increase vulnerability generation 10.7x (from 3.5% to 37.4%), with direct instruction attacks achieving 100% success on GPT-3.5-Turbo. Cross-model transferability reaches 60-100%, indicating systemic architectural vulnerabilities rather than model-specific flaws. Our dual-layer defense framework achieves 89.1% detection rate with 0.3% false positives and 520ms latency, demonstrating practical feasibility for real-time deployment in development environments.
