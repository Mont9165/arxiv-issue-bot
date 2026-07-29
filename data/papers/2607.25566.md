# ARCHER: Agentic Rule and Compliance Harness for Executable Regulations

- arXiv ID: `2607.25566v1`
- Authors: Chiraag Singh Anand, Xue Wen Tan, Lionel Teo, Eric Tan
- Published: 2026-07-28
- Primary category: `cs.MA`
- Categories: `cs.MA`, `cs.CE`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.25566v1) | [pdf](https://arxiv.org/pdf/2607.25566v1)

## Abstract

Verifying building compliance requires validating thousands of rules against large Building Information Modeling (BIM) designs, which is laborious, capital-intensive, and unscalable. Existing Automated Compliance Checkers (ACCs) are often difficult to generalize across different scenarios, as they are typically developed for highly specific rule sets and use cases. In addition, many ACCs are proprietary, meaning the underlying verification code is not released to end users, so users cannot verify whether their regulatory intent can be accurately captured. We introduce ARCHER (Agentic Rule and Compliance Harness for Executable Regulations), a test-driven, deterministically orchestrated multi-agent program-synthesis harness that generates auditable verification code from regulatory Codes of Practice, enabling transparent, adaptable, and scalable compliance checking. To characterize what makes agentic synthesis work, we evaluate a taxonomy of six harnesses of increasing agentic sophistication across four backbone models, spanning realistic data-governance tiers (from frontier third-party APIs to a fully on-premise open-weights model) on a novel dataset derived from real-world compliance scenarios. ARCHER's deterministic multi-agent orchestration achieves the highest accuracy for every backbone, improving mean union accuracy by 82% over a naive single-pass prompting baseline. Our cost-accuracy analysis further shows that using the ARCHER harness, a self-hosted open-weights model can reach 97.8% of frontier-API accuracy at a quarter of the cost, making data-sovereign compliance checking practical.
