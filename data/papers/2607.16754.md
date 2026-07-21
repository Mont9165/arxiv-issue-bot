# A Non-Intrusive Traffic Analysis Framework for Authorization Risk Detection and Coordinated Response in Web Applications

- arXiv ID: `2607.16754v1`
- Authors: Siqi Lin, Yuchao Luo, Zihan Zhu, Yiran Wang, Borui Qiu
- Published: 2026-07-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.16754v1) | [pdf](https://arxiv.org/pdf/2607.16754v1)

## Abstract

Authorization violations under valid Web sessions are difficult to identify and handle in real time from traffic because they depend strongly on business semantics and exhibit few distinctive protocol-level features. This paper proposes a non-intrusive traffic analysis framework for authorization risk detection and coordinated response. Request-response transactions are correlated to extract the access subject, business endpoint, object identifier, authentication state, and behavioral sequence. Object-access evidence, identity consistency, behavioral anomalies, authentication context, network environment, and endpoint-operation risk are mapped to interpretable risk components. Weighted fusion and high-risk priority constraints produce graded decisions that drive allow, alert, block, and external policy actions. The risk components are instantiated using deterministic and interpretable rules to evaluate multi-source evidence organization, risk fusion, and the coordinated-response loop at the framework level. In a controlled local testbed containing 2,000 balanced labeled samples, the framework classified 998 of 1,000 authorization-risk events as risky and produced no false positives among 1,000 normal accesses, achieving 99.90% accuracy, 100.00% precision, 99.80% recall, and a 99.90% F1 score. Removing runtime object evidence reduced the F1 score to 81.31%, while removing the high-risk priority constraint reduced it to 73.90%. In a prototype feasibility test with 100 concurrent requests and 1,000 total requests, mean risk-decision computation latency was 0.077 ms and P99 latency was 0.137 ms. The results demonstrate the feasibility of organizing heterogeneous runtime evidence and establishing an executable authorization-risk decision and coordinated-response loop without modifying application code, but do not establish general applicability in production environments.
