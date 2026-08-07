# Three Heads Are Better Than One: A Multi-perspective Reasoning Framework for Enhanced Vulnerability Detection

- arXiv ID: `2605.18153v1`
- Authors: Xin Peng, Bo Lin, Jing Wang, Xiaoling Li, Jun Ma, Jie Yu, Xiaoguang Mao, Shangwen Wang
- Published: 2026-05-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.18153v1) | [pdf](https://arxiv.org/pdf/2605.18153v1)

## Abstract

Automated vulnerability detection is crucial for enhancing software security by identifying potential flaws that attackers could exploit, thereby reducing the reliance on labor-intensive manual code audits. Recent advancements have shifted towards leveraging large language models (LLMs) for vulnerability detection, with techniques like Vul-RAG and VulnSage demonstrating progress through structured prompting and external knowledge integration. However, these approaches typically rely on a single reasoning paradigm, limiting their ability to address the complex and diverse nature of real-world vulnerabilities. To overcome these limitations, we propose ReasonVul, a novel multi-perspective reasoning framework that harnesses cognitive synergy among three specialized LLM agents, each embodying a distinct reasoning mode. The framework begins with independent analyses of the source code, followed by a structured debate mechanism to resolve conflicts through iterative rebuttal and revision, ultimately converging on a collaborative judgment. Evaluated on the PrimeVul dataset, ReasonVul achieves a PairAcc of 40.00% and an F1-score of 72.52%, surpassing the best baseline by 81.24% in PairAcc. Further tests on the JITVUL dataset confirm its generalizability, with a PairAcc of 28.67%. Additionally, we analyzed 542 conflict cases and found that 389 were correctly resolved, highlighting the framework's ability to uncover hidden vulnerabilities through the error-correction mechanism driven by the debate. This work emphasizes the importance of multi-perspective reasoning and collaborative validation in achieving robust and comprehensive vulnerability detection in real-world software systems.
