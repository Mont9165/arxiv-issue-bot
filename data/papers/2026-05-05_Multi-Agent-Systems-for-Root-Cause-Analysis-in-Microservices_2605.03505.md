# Multi-Agent Systems for Root Cause Analysis in Microservices

- arXiv ID: `2605.03505v1`
- Authors: Alexander Naakka, Yuqing Wang, Mika V Mäntylä
- Published: 2026-05-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03505v1) | [pdf](https://arxiv.org/pdf/2605.03505v1)

## Abstract

Recent advances in large language models (LLMs) have enabled early attempts to automate root cause analysis (RCA) in microservice-based systems (MSS). Yet, prior works typically rely on a linear reasoning process that proceeds along a single diagnostic path. In this paper, we propose LATS-RCA, an LLM-based multi-agent framework for RCA in MSS. LATS-RCA formulates RCA as a reflection-guided tree-structured search using a Language Agent Tree Search algorithm. In LATS-RCA, multiple LLM-driven agents iteratively perform RCA for each microservice by reasoning over its execution logs and performance metrics to collect operational evidence for root cause exploration. Reflection scores derived from intermediate diagnostic states are used to guide the search toward the most likely root cause based on accumulated evidence. We evaluate LATS-RCA on the open-source industrial MSS, Light-OAuth2 (LO2), using a publicly available dataset and in a production microservice environment (Prod) in a case company with substantially higher operational complexity. LO2 is a small-team Java system with a homogeneous technology stack. The results on LO2 show that LATS-RCA achieves high diagnostic accuracy, and we further benchmark its associated computational costs. Compared to LO2, Prod attains lower diagnostic accuracy and incurs higher computational cost. The Prod deployment demonstrates the practical applicability of LATS-RCA in real-world MSS and reflects the challenges introduced by polyglot tech stack, varied logging practices of source components, and multi-factor root-causes by production-scale MSS.
