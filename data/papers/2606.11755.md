# Acoda: Adversarial Code Obfuscation for Defending against LLM-based Analysis

- arXiv ID: `2606.11755v1`
- Authors: Hongzhou Rao, Zikan Dong, Yanjie Zhao, Haodong Li, Haoyu Wang
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.11755v1) | [pdf](https://arxiv.org/pdf/2606.11755v1)

## Abstract

With the widespread adoption of Large Language Models (LLMs) in software engineering (SE) tasks such as code understanding, debugging, and vulnerability detection, their powerful semantic reasoning ability has also introduced new security and privacy risks. LLMs can analyze, reconstruct, or even reverse-engineer source code logic, potentially leading to the leakage of intellectual property. To address this issue, we propose Acoda, a genetic algorithm-based adversarial code obfuscation framework that defends against LLM-based code analysis. Acoda leverages two key mechanisms of LLMs, namely safety alignment and token-based information processing, to design 8 semantics-preserving obfuscation methods. It iteratively optimizes obfuscation strategies through a genetic algorithm to generate adversarial samples that maximize defensive effectiveness. In addition, we propose a quantitative evaluation framework based on LLM responses, which combines an auxiliary LLM and four evaluation metrics to assess how target LLMs analyze obfuscated code comprehensively. Experimental results show that Acoda can effectively induce LLMs to refuse or misinterpret code analysis. On 7 state-of-the-art LLMs, including GPT-4o, DeepSeek, Qwen, Llama, and Gemma, Acoda achieves an attack success rate (ASR) of up to 70%, with strong cross-model transferability and minimal runtime overhead, while ensuring that the semantics of the original code remain unchanged. Overall, this study provides a new perspective for code protection and LLM security defense in the era of LLMs.
