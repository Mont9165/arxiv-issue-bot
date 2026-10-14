# RESTOR: Automated Test Oracle Generation for RESTful APIs via Reinforcement Learning

- arXiv ID: `2607.23963v1`
- Authors: Xun Zhou, Zhen Dong, Mingyu Ren, Qiang Li, JunJie Li, Sifan Wang, Xiaolong Yu, Chaofeng Sha, Xin Peng
- Published: 2026-07-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.23963v1) | [pdf](https://arxiv.org/pdf/2607.23963v1)

## Abstract

Modern REST API testing faces a critical challenge in defining reliable test oracles, particularly in agile industrial environments where formal specifications (e.g., OpenAPI) are frequently missing or outdated, and historical execution logs are unavailable for newly deployed endpoints. In this paper, we present Restor (Reinforcement Enhanced Single-Traffic Oracle generator for REST APIs), a framework that generates executable test assertions from a single observed request-response pair in a black-box setting. Unlike existing approaches that rely on rule-based templates or massive training logs, Restor utilizes a novel data augmentation pipeline to fine-tune a lightweight Large Language Model (LLM) via Group Relative Policy Optimization (GRPO). This training process enables the model to internalize testing "common sense" by optimizing a reward function that jointly encourages: (i) the selection of stable, semantically meaningful fields for validation and the avoidance of dynamic noise (e.g., timestamps or trace IDs); (ii) the generation of robust assertions that withstand logic variations. We evaluate Restor on an industrial dataset comprising over 2,300 API traces across 246 real-world services. Comprehensive experiments demonstrate that Restor significantly outperforms prompt-engineered baselines and generalist models, achieving a superior $F_1$ score of 85.42% in key field identification and increasing the proportion of semantically accurate assertions. Furthermore, deployment in a production CI/CD workflow at ByteDance confirms its practical value: the system raised the adoption rate of automatically generated test cases from 74.1% to over 96%, substantially reducing manual Quality Assurance (QA) effort while ensuring high execution stability.
