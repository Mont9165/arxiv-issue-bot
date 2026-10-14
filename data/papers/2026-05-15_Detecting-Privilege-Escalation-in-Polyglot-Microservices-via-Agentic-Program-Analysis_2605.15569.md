# Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis

- arXiv ID: `2605.15569v1`
- Authors: Penghui Li, Hong Yau Chong, Yinzhi Cao, Junfeng Yang
- Published: 2026-05-15
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.15569v1) | [pdf](https://arxiv.org/pdf/2605.15569v1)

## Abstract

Microservices are widely adopted in modern cloud systems due to their scalability and fault tolerance. However, microservice architectures introduce significant complexity in privilege and permission control, creating risks of privilege escalation where attackers can gain unauthorized access to resources or operations. Detecting such vulnerabilities is challenging due to complex cross-service interactions, polyglot codebases, and diverse privileged operations and permission checks. We present Neo, an agentic program analysis framework that combines large language models (LLMs) with classic program analysis to address these challenges. Neo leverages an LLM-based agent that dynamically generates analysis plans, adapts code search strategies, and validates semantics. We develop code search primitives that enable Neo to perform scalable and flexible code exploration across services and languages. We evaluated Neo on 25 open-source microservice applications spanning 7 programming languages and 6.2 million lines of code. Neo uncovered 24 zero-day privilege escalation vulnerabilities and achieved 81.0% precision and 85.0% recall on a ground-truth dataset. Compared to existing program analysis and agentic solutions, Neo demonstrated significant improvements in both detection accuracy and scalability. We further showcased Neo's extensibility by applying it to other application domains and vulnerability types, uncovering 18 additional zero-day vulnerabilities.
