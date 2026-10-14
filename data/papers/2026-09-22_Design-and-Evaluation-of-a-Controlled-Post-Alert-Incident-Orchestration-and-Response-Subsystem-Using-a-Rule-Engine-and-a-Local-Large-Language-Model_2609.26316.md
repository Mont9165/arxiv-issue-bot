# Design and Evaluation of a Controlled Post-Alert Incident Orchestration and Response Subsystem Using a Rule Engine and a Local Large Language Model

- arXiv ID: `2609.26316v1`
- Authors: Hoang-Lam Huynh, Quoc-Cuong Tang, Van-Tri Phan, Khuong Nguyen-An
- Published: 2026-09-22
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.26316v1) | [pdf](https://arxiv.org/pdf/2609.26316v1)

## Abstract

This paper presents a controlled post-alert incident orchestration and response subsystem for educational information systems. The architecture separates deterministic classification, contextual analysis, human approval, and technical execution. A Rule Engine determines severity and selects the playbook, while Static RAG and a local large language model provide advisory content under Validator, Guardrail, Output Sanitizer, and Safe Fallback controls. Experiments begin after simulated alerts are stored in Elasticsearch. The Rule Engine matched the predefined routing matrix in all 30 boundary cases. The Durable Queue completed 100 events without duplicate tasks, new failed tasks, or unintended firewall rules. An eight-alert contention experiment preserved the configured limit of one active model request, and 30 sequential measurements showed an overall mean post-alert processing time of approximately 33 seconds. The results demonstrate functional correctness, traceability, controlled recovery, and bounded model integration within the evaluated laboratory scope.
