# Checked-In Secret Detection: Strings Are All You Need

- arXiv ID: `2608.04523v1`
- Authors: Zhengdong Huang, Kevin Li, Jinqiu Yang, Yepang Liu, Lili Wei
- Published: 2026-08-05
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.04523v1) | [pdf](https://arxiv.org/pdf/2608.04523v1)

## Abstract

Hardcoded secrets in source code pose critical security vulnerabilities which can be easily exploited by malicious adversaries. Existing regex-based detection approaches suffer from fundamental limitations, as secrets often lack identifiable patterns, resulting in poor precision and recall. Recent studies have explored context-aware detection methods, as surrounding code can reveal the purpose of candidate strings. However, these methods confront three key challenges: (1) obfuscation robustness where models over-rely on easily obfuscated identifiers, (2) cross-language generalization difficulties due to uneven training data distribution, and (3) lengthy and noisy context that introduces excessive irrelevant tokens and slows inference. We observe that strings serve as a critical information source for code semantics, offering superior contextual density, obfuscation robustness, and language independence. Based on this insight, we propose StringGroup, a novel context extraction algorithm that mines strings surrounding potential secrets. By introducing a relatively simple modification to existing patterns that narrows the analysis specifically to string literals, the method achieves significant gains. With only 33.2% of the original context, it preserves over 80% of semantic information and significantly improves the signal-to-noise ratio for secret detection. We further design a context-aware secret detection tool, Secretron, based on StringGroup methods and Transformer model. Evaluation on the SecretBench dataset demonstrates high accuracy with 98.74% F1-score and strong robustness under obfuscation and cross-language scenarios, outperforming state-of-the-art LLM-based baselines. We deploy our tool in real-world environments and successfully detect 48 previously unknown secret keys from 26 applications, demonstrating the practical effectiveness of our approach.
