# Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning

- arXiv ID: `2604.20179v1`
- Authors: Ronghao Ni, Mihai Christodorescu, Limin Jia
- Published: 2026-04-22
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.20179v1) | [pdf](https://arxiv.org/pdf/2604.20179v1)

## Abstract

The rapidly evolving Node$.$js ecosystem currently includes millions of packages and is a critical part of modern software supply chains, making vulnerability detection of Node$.$js packages increasingly important. However, traditional program analysis struggles in this setting because of dynamic JavaScript features and the large number of package dependencies. Recent advances in large language models (LLMs) and the emerging paradigm of LLM-based agents offer an alternative to handcrafted program models. This raises the question of whether an LLM-centric, tool-augmented approach can effectively detect and confirm taint-style vulnerabilities (e.g., arbitrary command injection) in Node$.$js packages. We implement LLMVD$.$js, a multi-stage agent pipeline to scan code, propose vulnerabilities, generate proof-of-concept exploits, and validate them through lightweight execution oracles; and systematically evaluate its effectiveness in taint-style vulnerability detection and confirmation in Node$.$js packages without dedicated static/dynamic analysis engines for path derivation. For packages from public benchmarks, LLMVD$.$js confirms 84% of the vulnerabilities, compared to less than 22% for prior program analysis tools. It also outperforms a prior LLM-program-analysis hybrid approach while requiring neither vulnerability annotations nor prior vulnerability reports. When evaluated on a set of 260 recently released packages (without vulnerability groundtruth information), traditional tools produce validated exploits for few ($\leq 2$) packages, while LLMVD$.$js generates validated exploits for 36 packages.
