# Energy as a Service-Level Objective: Transaction-Level Energy Attribution

- arXiv ID: `2611.32731v1`
- Authors: Julian Legler
- Published: 2026-11-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2611.32731v1) | [pdf](https://arxiv.org/pdf/2611.32731v1)

## Abstract

Service engineers assess every change against functional requirements and qualities such as reliability, performance and availability. Energy is rarely part of this assessment. When consumption rises after a change, the team cannot tell whether the increase is worth investigating, worth accepting, or neither. A change to tracing, retries or a shared component can affect consumption far beyond the modified component. This thesis asks how energy objectives can become actionable engineering instruments rather than reporting metrics. Site Reliability Engineering (SRE) answered a similar question for reliability with service-level indicators, objectives and response policies. We take SRE as the guiding research vision and study where the analogy holds for energy and where it breaks. An energy objective could, for example, bound the energy per successful transaction under stated workload conditions. The thesis connects three threads into one experimentally evaluated methodology. Useful-work semantics define what a successful transaction is. Energy attribution assigns shared and auxiliary consumption to transactions. Service-level engineering decisions act on the resulting energy objectives. Existing work covers attribution methods, measurement frameworks and sustainability objectives, mostly at component level and without a link to decisions. Our prior work on service-level energy modeling showed that the energy of auxiliary services is often overlooked and hard to measure. Planned experiments compare aggregate, request-normalized and useful-work-based indicators under controlled changes to observability configuration and injected failures. Whether transaction-level attribution is needed for these decisions, or whether service-level attribution with outcome counts is sufficient, is an open question the experiments are designed to answer.
