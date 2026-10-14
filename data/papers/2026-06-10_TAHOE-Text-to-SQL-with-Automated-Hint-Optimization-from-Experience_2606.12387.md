# TAHOE: Text-to-SQL with Automated Hint Optimization from Experience

- arXiv ID: `2606.12387v1`
- Authors: Zhiyi Chen, Jie Song, Peng Li
- Published: 2026-06-10
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.12387v1) | [pdf](https://arxiv.org/pdf/2606.12387v1)

## Abstract

Large Language Models (LLMs) have democratized database access through Text-to-SQL, but moving from prototypes to production remains difficult. Real deployments must handle strict SQL dialects, massive schemas, and evolving user preferences, while supervised fine-tuning is costly and rigid and agentic test-time scaling is expensive. We present Tahoe, a system that treats prompt optimization as a dynamic data management problem. Tahoe uses an error-driven hint learning pipeline across Development and Deployment to consolidate debugging traces into a structured Hint Bank. Compiler feedback is distilled into reusable Syntax Hints for dialect-specific rules, while execution and user feedback are converted into Semantic Hints for schema- and user-specific logic. Tahoe further introduces a Strategy Layer that models conflicting user intents as competing strategies under shared natural-language triggers, with recency signals and post-learning attribution statistics that summarize empirical success, harm, inertness, and support. At inference time, Tahoe retrieves relevant hints and guides the LLM through Logic Planning followed by SQL Synthesis. We implement and evaluate the development-phase workflow, leaving deployment-time human-feedback updates for future work. On Spider 2.0-Snow, Tahoe substantially improves Text-to-SQL without updating model parameters. On 113 supervised Spider 2.0-Snow-0212 examples using GPT-5.5, Tahoe raises pass rate from 61.95 percent to 79.42 percent and pass-at-4 from 72.57 percent to 87.61 percent, achieves 100 percent Snowflake syntax pass rate, and reduces average compiler-feedback critic rounds from 2.79 to 0.12 per sampled candidate. The same Hint Bank also transfers to weaker backbones, including a 19.7 percentage-point pass-rate gain on Doubao-2.0-lite.
