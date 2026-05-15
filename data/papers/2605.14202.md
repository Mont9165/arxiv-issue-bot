# LLM-Based Robustness Testing of Microservice Applications: An Empirical Study

- arXiv ID: `2605.14202v1`
- Authors: Hrushitha Goud Tigulla, Marco Vieira
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.14202v1) | [pdf](https://arxiv.org/pdf/2605.14202v1)

## Abstract

Malformed, missing, or boundary-value inputs in microservice APIs can cascade across dependent services, threatening reliability. Robustness testing systematically exercises such inputs to expose server-side failures, but generating diverse, effective tests remains challenging. Large Language Models can generate such tests from API specifications; however, it is unknown whether different models and prompt strategies produce diverse failure sets or converge on the same failures. We report a controlled experiment applying 7 prompt strategies to 3 open-source LLMs (14B-70B parameters) targeting 2 architecturally distinct microservice systems: one Java monolingual (6 services, 9 failure modes) and one polyglot (27 services, 14 failure modes), yielding 38 valid runs and 663 generated tests. We find that prompt strategy explains more variation in diversity than model size: a Structured prompt collapses diversity entirely, while a single model varied across three prompt strategies achieves complete failure-mode coverage on one system, outperforming any multi-model ensemble under a fixed prompt. We introduce two strategies, Guided and GuidedFewShot, that embed a mutation taxonomy from prior robustness testing research as domain context. GuidedFewShot achieves the highest single-run coverage on both systems (5 of 9 and 8 of 14 failure modes) while maintaining low cross-model similarity. A key lesson is that taxonomy rules alone are insufficient: LLMs cannot distinguish key-absent from value-empty mutations without concrete examples. Findings replicate across both systems.
