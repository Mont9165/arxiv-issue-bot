# Exploiting LLM Agent Supply Chains via Payload-less Skills

- arXiv ID: `2605.14460v1`
- Authors: Xinyu Liu, Yukai Zhao, Xing Hu, Xin Xia
- Published: 2026-05-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.14460v1) | [pdf](https://arxiv.org/pdf/2605.14460v1)

## Abstract

Autonomous agents powered by Large Language Models (LLMs) acquire external functionalities through third-party skills available in open marketplaces. Adopting these integrations broadens the potential attack surface, prompting a need for systematic security evaluation. Current auditing mechanisms are effective at identifying explicit code payloads and predefined threat contents through security scanning. These detection mechanisms are bypassed if malicious behaviors lack direct injection and are instead synthesized dynamically at runtime through the agent's inherent generative capabilities. Exploring this blind spot, we introduce Semantic Compliance Hijacking (SCH), a payload-less supply chain attack targeting autonomous coding environments. The SCH approach translates malicious goals into unstructured natural language instructions formatted as necessary compliance rules, leading the agent to generate and execute unauthorized code. To assess the real-world viability of this attack, we developed an automated pipeline to evaluate its effectiveness across a test matrix comprising three mainstream agent frameworks and three distinct foundation models using contextualized scenarios. The findings demonstrate the pervasive nature of this threat, with SCH achieving peak success rates of up to 77.67% for confidentiality breaches and 67.33% for Remote Code Execution (RCE) under the most vulnerable configurations. Furthermore, the introduction of Multi-Skill Automated Optimization (MS-AO) further boosted attack efficacy. By omitting recognizable Abstract Syntax Tree (AST) signatures and explicit harmful intents, the manipulated skill files maintained a 0.00% detection rate, evading current scanning tools. This research highlights an underexplored attack surface within agent supply chains, pointing to a necessary transition from signature-based detection models toward semantic intent validation.
