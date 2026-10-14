# MuMuTestUp: Mutation-based Multi-Agent Test Case Update

- arXiv ID: `2605.19265v1`
- Authors: Dawei Tian, Jiakun Liu, Yun Peng, Yichen Zhang, Jianlei Chi, Jun Sun, Xiaohong Su
- Published: 2026-05-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.19265v1) | [pdf](https://arxiv.org/pdf/2605.19265v1)

## Abstract

Modern software systems evolve rapidly under CI/CD practices, where tests are critical for quality. However, substantial code changes often render existing test cases obsolete, causing pipeline disruptions, reduced productivity, and compromised quality. Recent automatic test update approaches leverage LLMs to refine test cases via execution feedback and exact-matching context retrieval, prioritizing executability and line coverage but suffering three limitations: (1) neglecting test assertion adequacy, weakening fault detection; (2) relying on coarse line coverage instead of specific uncovered lines/branches; (3) using exact-matching retrieval, which fails for LLM hallucinated queries. To address these, we propose MuMuTestUp, a mutation-guided multi-agent framework with three specialized agents: Mutation Analysis (strengthens assertions via surviving mutants), Coverage Analysis (generates targeted repair instructions for uncovered lines/branches), and Semantic Retrieval (handles hallucinations via semantic-similarity search). We also construct PRBENCH, a 571-sample pull-request-level dataset from 10 open-source Java projects (validated for cross-commit update scenarios). Evaluations against state-of-the-art baselines use both open-source (Deepseek-V3.2) and closed-source (GPT-4.1) LLMs.
