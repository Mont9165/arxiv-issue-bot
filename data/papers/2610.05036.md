# Characterizing Security Effects of OSS Vulnerabilities in Agent Systems

- arXiv ID: `2610.05036v1`
- Authors: Yu Ji, Yang Wei, Yutao Hu, Haojun Zhao, Yueming Wu, Deqing Zou
- Published: 2026-10-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.05036v1) | [pdf](https://arxiv.org/pdf/2610.05036v1)

## Abstract

Software agents increasingly depend on open-source components when executing tools and interacting with external systems. Security flaws in these dependencies may therefore influence more than the software process in which they occur: their consequences can be carried through tool outputs, agent state, and information subsequently exposed to the model. Determining whether such a consequence is actually realized in a particular execution, and where its influence stops within the agent system, remains challenging.
  We investigate how known OSS vulnerabilities behave when exercised as part of agent workflows. Our study reveals recurring patterns in the way security-relevant consequences emerge and propagate across runtime layers. Building on these observations, we use vulnerability-aware semantic information, differential executions of vulnerable and corrected software, and runtime provenance spanning multiple layers to determine whether a vulnerability produces an observable security effect and to identify the furthest layer at which that effect remains manifested.
  Our evaluation shows that this approach can accurately distinguish realized vulnerability effects and determine their manifestation boundaries across a diverse collection of vulnerability scenarios. We additionally apply the analysis to documented workflows in a real-world agent framework and uncover multiple security effects originating from known vulnerabilities in its OSS dependencies. These results highlight the importance of reasoning about vulnerable dependencies in terms of their execution-level consequences rather than vulnerability presence alone.
