# Test Before You Deploy: Governing Updates in the LLM Supply Chain

- arXiv ID: `2604.27789v1`
- Authors: Mohd Sameen Chishti, Damilare Peter Oyinloye, Jingyue Li
- Published: 2026-04-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.27789v1) | [pdf](https://arxiv.org/pdf/2604.27789v1)

## Abstract

Large Language Models (LLMs) are increasingly used as core dependencies in software systems. However, the hosted LLM services evolve continuously through provider-side updates without explicit version changes. These silent updates can introduce behavioral drift, causing regressions in functionality, formatting, safety constraints, or other application-specific requirements. Existing approaches focus primarily on regression testing or versioning but do not provide deployer-side mechanisms for governing compatibility during opaque model evolution. This paper proposes a deployment-side governance framework based on three components: clearly defined rules for how the model is allowed to behave (production contracts), focused testing organized by deployment risk categories (risk-category-based testing suite), and release checkpoints that block updates unless they meet defined safety and performance standards (compatibility gates). Through exploratory validation across multiple LLM versions, we provide evidence that targeted testing in specific risk areas can uncover performance regressions that overall metrics miss. We also identify several open research challenges, including how to systematically build effective test suites, how to set reliable performance thresholds in non-deterministic systems, and how to detect and explain model drift when providers offer limited transparency. Overall, we frame LLM update management as a software supply chain governance problem and outline a research agenda for putting deployer-side compatibility controls into practice.
