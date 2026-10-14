# XAgent: eXecution-guided Agentic AI for Effective Localization and Resolution of GitHub Issues

- arXiv ID: `2609.09769v1`
- Authors: Hieu Huynh, Patanamon Thongtanunam, Michael Fu, Bach Le, Kla Tantithamthavorn
- Published: 2026-09-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.09769v1) | [pdf](https://arxiv.org/pdf/2609.09769v1)

## Abstract

Agentic AI has enabled capabilities in leveraging Large Language Models (LLMs) to autonomously resolve repository-level GitHub issues. However, due to the reliance on limited static description of issues, existing agentic approaches suffer from incorrect localization and incomplete validation. Solely relying on this information can bias LLM reasoning toward the narrow scope of the issue description, leading to incomplete patches that fail to address the underlying issue. In this paper, we present XAgent, an execution-guided agentic framework that analyzes dynamic behavior and additional program context to localize and validate issues. The experimental results on the SWE-bench-lite dataset demonstrate that XAgent outperforms other existing approaches, achieving a resolve rate of 62.0% and a function localization accuracy of 72.8%, while maintaining cost efficiency. Our analysis further shows that XAgent successfully resolves 7 additional issues that the top existing baselines fail to address. This work highlights a shift from static, description-oriented patch generation toward dynamic execution-guided issue resolution, opening new opportunities for LLM-based coding agents to achieve more robust and generalizable software maintenance.
