# DeFiScreener: Efficient DeFi Attack Pre-screening in Smart Contracts via Historical Case Matching

- arXiv ID: `2607.22184v1`
- Authors: Rui Cao, Shaojing Fan, Zhimei Sui, Liming Fang, Ziqi Yang, Yingying Jiao, Zhenguang Liu
- Published: 2026-07-24
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.22184v1) | [pdf](https://arxiv.org/pdf/2607.22184v1)

## Abstract

Blockchain and its killer applications, particularly decentralized finance (DeFi), are gaining widespread adoption, with over 5,200 DeFi projects deployed on mainstream blockchains as of January 2026. At the same time, security risks in DeFi are becoming increasingly serious. However, existing DeFi detection tools usually cover only specific attack types, exhibiting severely limited detection coverage.
  In this paper, we argue that an effective way to address this gap is to pre-screen vulnerable instances from large volumes of smart contract functions and call sequences. This is motivated by a key phenomenon we term "perilous temporal asymmetry". Inspired by this, we propose DeFiScreener, the first automated pre-screening framework for DeFi attacks that uses historical exploit cases to identify potentially vulnerable functions and call sequences. Given the full source code of a target project, DeFiScreener builds Function Call Trees (FCTs) and generates semantic embeddings for each function using a large language model (LLM), allowing both program structure and function intent to be analyzed together. It then applies a dual-level screening process. At the function level, function embeddings are matched against an Attack Pattern Library of historically exploited functions. At the sequence level, the proposed Attack Pattern Oriented Monte Carlo Tree Search (APO-MCTS) efficiently explores the FCTs and screens vulnerable call sequences. The identified candidates are ultimately passed to an LLM for further interpretive and security analysis.
  We empirically evaluate the DeFiScreener over datasets comprising 207 real-world DeFi attack incidents. Experimental results demonstrate that DeFiScreener achieves a remarkable 98.55% recall and 84.30% precision in attack pre-screening.
