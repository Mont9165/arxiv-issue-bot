# Risk Architecture for AI-Native Engineering Teams: An Organizational Framework for Agentic System Governance

- arXiv ID: `2607.01421v1`
- Authors: Laxmipriya Ganesh Iyer
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.01421v1) | [pdf](https://arxiv.org/pdf/2607.01421v1)

## Abstract

Engineering management research has produced mature frameworks for software risk: ownership by feature, escalation by severity, and assurance by test coverage. These frameworks implicitly assume deterministic behavior, discrete and auditable change events, and clear component-to-owner mappings. Teams that build and operate agentic AI systems violate all three assumptions at once: outputs are probabilistic, systems take autonomous multi-step actions, and the risk surface mutates silently between deployments. Existing AI risk literature addresses this from above (policy frameworks such as the NIST AI RMF and ISO/IEC 42001) or below (threat taxonomies such as OWASP's agentic AI guidance), but not at the layer where an engineering manager (EM) operates: roles, decision rights, and escalation structures. This paper contributes (i) a seven-dimension profile distinguishing pure software-engineering, hybrid, and AI-native teams; (ii) a six-cluster failure-mode taxonomy including a previously unarticulated cluster, dependency-boundary determinism mismatch; and (iii) a synthetic framework-adequacy methodology scoring how well each profile's risk architecture detects, contains, and escalates a defined scenario set. Because the object of study is framework adequacy rather than human behavior, the evaluation yields derived rather than observed coverage claims. Coverage degrades as teams move from pure software engineering to AI-native operation, monotonically in the median and abruptly in the count of uncovered, high-consequence failures appearing only at the AI-native step. The degradation concentrates in specific failure-mode categories, and the most severe, least-covered failures arise not inside AI-native teams but at the organizational boundary where their probabilistic outputs are consumed by determinism-assuming dependencies.
