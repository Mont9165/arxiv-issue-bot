# An Empirical Evaluation of Cost-Efficient Large Language Models on Algorithmic Programming Tasks

- arXiv ID: `2609.18052v1`
- Authors: Chandimal Adikari, Nandika Herath
- Published: 2026-09-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.18052v1) | [pdf](https://arxiv.org/pdf/2609.18052v1)

## Abstract

This study empirically evaluates whether cost-efficient Large Language Models (LLMs) can be trusted to generate enterprise code to a written specification. Three models (Gemini Flash 3, GPT-5.4 mini and Claude Haiku 4.5) were asked to solve 992 algorithmic problems as Java Spring Boot service methods conforming to a mandated signature and data-transfer-object specification, crossing four model and agentic coding tool combinations with two prompt variants to yield eight configurations, with iteration forbidden and hardcoded answers explicitly prohibited. Eight problem statements were withheld to probe how models respond to missing input. The 7,593 resulting methods were classified by an eight-class outcome taxonomy describing what each does about producing an answer, then deployed and executed, giving 7,936 measured requests joined to that classification. Structural conformance approached ceiling, yet 38.4% of methods do not compute the value they returned and only 12.9% of returned answers were correct. Conditioning on outcome class shows that response reliability and correctness are inversely related, whereas genuinely computing methods answered least often and were correct 19.3%. Limitations include single generation runs per configuration, partial harness coverage, single-pass timing, syntactic classification, and probable corpus contamination.
