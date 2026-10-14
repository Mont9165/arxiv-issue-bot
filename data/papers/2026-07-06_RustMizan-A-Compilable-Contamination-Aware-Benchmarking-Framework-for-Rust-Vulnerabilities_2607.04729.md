# RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities

- arXiv ID: `2607.04729v1`
- Authors: Tarek Elsayed, Shiping Yang, Eunsong Koh, Sanika Goyal, Vincent Huang, Paul Ngo, Nathan Young, Mohammad Omidvar Tehrani, Alvyn Kang, Arnell Kang, Zeyu Chen, Angélica Moreira, Xuan Feng, Angel X. Chang, Nick Sumner, Steven Y. Ko
- Published: 2026-07-06
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04729v1) | [pdf](https://arxiv.org/pdf/2607.04729v1)

## Abstract

LLM agents are increasingly applied to vulnerability analysis, but existing benchmarks have not kept pace. They typically rely on small non-compilable snippets, focus on binary classification (vulnerable or not), and do not account for the risk that publicly-released datasets are part of model training corpora. We introduce RustMizan, a benchmarking framework for Rust vulnerability analysis that addresses these gaps. RustMizan contains compilable code variants at the crate, file, and function levels, with annotations for binary vulnerability detection, CWE classification, and function- and line-level localization. A paired mutation framework produces semantics-preserving code mutants for contamination testing and robustness probing. Across four frontier models in an agentic setup with command-line access, binary classification sits in the 56-65% range, but line localization F1 stays near 20%, and adversarial cues drop line F1 by about 27%.
