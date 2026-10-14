# Practical Source Code Recovery from Binary Functions Using Anchor-Based Retrieval and LLM Reasoning

- arXiv ID: `2607.09452v1`
- Authors: Charles Edward Gagnon, Steven H. H. Ding, Philippe Charland, Benjamin C. M. Fung
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.09452v1) | [pdf](https://arxiv.org/pdf/2607.09452v1)

## Abstract

We present a practical pipeline for recovering source code from stripped binary functions by combining reverse engineering, anchor-based source code retrieval, and large language model reasoning. Our binary-to-source-code retrieval method attempts to identify the source function from a source code database, rather than generating approximate decompiled pseudocode. It extracts anchors such as strings, constants, external calls, and available function names using Ghidra, retrieves candidate files via an inverted-index search database, narrows candidates to likely function snippets, and re-ranks them with a large language model (LLM) based on disassembly, decompiled code, and source metadata. Confident matches can also serve as anchors in later passes. In an evaluation backed by our high-fidelity source code database on a stripped, optimized tcpdump binary, our proposed binary-to-source matching method achieves 95.2% assembly instruction coverage. Experiments on a GitHub-based retrieval database showed lower performance with 35.5% instruction coverage on average, mainly due to retrieval misses. These results show that source-level binary recovery excels with high-quality databases and remains a useful tool in noisy environments.
