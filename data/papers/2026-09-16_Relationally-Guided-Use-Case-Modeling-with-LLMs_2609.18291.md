# Relationally Guided Use Case Modeling with LLMs

- arXiv ID: `2609.18291v1`
- Authors: Guangyu Wang, Bangqi Li, Ji Wu, Zhijun Shao
- Published: 2026-09-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2609.18291v1) | [pdf](https://arxiv.org/pdf/2609.18291v1)

## Abstract

Use case flows are important elements of use case modeling because they support downstream software engineering activities, including requirements analysis, architectural and detailed design, and test case generation. However, constructing them manually is costly and expertise-intensive, while existing automated approaches still struggle to preserve semantic consistency, control-flow logic, data-flow logic, and the intended system boundary, especially when identifying branch points and generating alternative flows. To address this problem, we propose FlowGen for complete use case flow construction. FlowGen uses LLM-based Semantic Information Processing (SIP) to extract semantic elements, constructs a Semantic Relational Graph (SRG) encoded by an enhanced R-GAT for basic flow generation (BFGen), and further supports branch point prediction through BPP and branch-conditioned alternative flow generation through AFGen. Evaluations on 13 public and 7 industrial datasets show that FlowGen consistently outperforms competitive baselines in all three core components. In particular, BFGen improves over the best baseline by 14% in Precision, 7-25% in Recall, 11-30% in F1, and 10-19% in AUC; BPP improves Precision by 30-110%, Recall by 33-91%, and F1 by 32-117%; AFGen improves Precision by 8-23%, F1 by 5-18%, and AUC by 0.6-2.5%. Moreover, we validate the effectiveness of the LLM-based SIP module and the attention preservation factor in BFGen, analyze the impact of requirement completeness on BFGen, and examine how different scopes of branch-related context affect AFGen.
