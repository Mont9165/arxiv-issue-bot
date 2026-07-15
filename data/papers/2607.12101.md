# Fault Injection in OpenAPI Specifications for Evaluating Black-Box Testing Effectiveness

- arXiv ID: `2607.12101v1`
- Authors: Hamza Bin Mazhar, Yuqing Wang, Mika V. Mäntylä
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12101v1) | [pdf](https://arxiv.org/pdf/2607.12101v1)

## Abstract

OpenAPI specifications are the primary input for black-box testing tools in microservice systems (MSS), yet prior work shows these specifications are often incomplete, inconsistent, or incorrect. Despite this, most studies on OpenAPI-based black-box testing assume correct specifications and evaluate tool performance. We address this gap by introducing a literature-grounded taxonomy of six OpenAPI specification fault classes. We inject faults at five severity levels, and evaluate the resulting mutated specifications on two microservice benchmarks, TrainTicket and SocialNetwork, using three testing tools: EvoMaster, RESTler, and Schemathesis. We measure the impact of these faults using code coverage, specification coverage, request/response quality, and behavioral diversity. Our results show that specification faults cause strong and heterogeneous degradation patterns across testing tools and systems. Faults in method semantics cause broad degradation across all metrics, while others, such as modifications to response codes, remain weak. Relaxations of schema constraints cause hidden degradation, with no impact on code and specification coverage but a large impact on request/response quality. These findings demonstrate that specification quality directly shapes black-box API testing effectiveness. Also, code and specification coverage-only evaluations can understate the impact of specification faults on black-box testing in MSS and should be complemented by request/response quality and behavioral diversity.
