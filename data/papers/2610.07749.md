# Cost-Effective Numerical QA over Semi-Structured Table: Structuring, Resolution, Planning

- arXiv ID: `2610.07749v1`
- Authors: Feng Luo, Hui Luo, Zhifeng Bao, J. Shane Culpepper, Xiaoli Wang, Shazia Sadiq
- Published: 2026-10-06
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.07749v1) | [pdf](https://arxiv.org/pdf/2610.07749v1)

## Abstract

Semi-structured tables encode rich semantic information through diverse layout elements, such as hierarchical row and column headers. Answering numerical questions over such data is challenging because it requires a joint effort of accurate structural understanding of tables, question uncertainty resolution, and complex query intents interpretation. Existing methods are rarely effective in handling the above multifaceted challenges in a holistic manner; moreover, they rely on LLMs without considering financial implications. We propose SemiBonsai, a cost-effective, LLM-powered framework featuring: (1) a Multiway Layered Table Structurer that converts a table into a multiway layered tree organized by structural elements; (2) a Context-Aware Uncertainty Resolver that grounds underspecified phrases to context-coherent structural elements; (3) a Plan-Guided Reasoner that decomposes complex query intents into a query plan for reasoning; (4) a Budget-Aware Bandit Router that learns per-instance LLM utilities and optimizes LLM selection under fixed monetary constraints. Experiments on three benchmarks show that SemiBonsai improves both QA effectiveness and cost-effectiveness. Notably, the Table Structurer improves answer accuracy by 46% over alternative tree construction methods, and Router achieves a 5% average relative gain in answer accuracy compared with existing routing methods across budgets.
