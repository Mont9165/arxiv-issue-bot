# SDVDiag: Multimodal Causal Discovery for Online Diagnosis in Software-defined Vehicles

- arXiv ID: `2606.15559v1`
- Authors: Matthias Weiß, Athreya Hosahalli Prakash, Falk Dettinger, Nasser Jazdi, Michael Weyrich
- Published: 2026-06-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DC`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.15559v1) | [pdf](https://arxiv.org/pdf/2606.15559v1)

## Abstract

The transition toward software-defined vehicles concentrates an increasing share of vehicle functionality into distributed software services, where failures propagate through service dependencies and the surface symptom is often several causal hops away from the underlying defect. Existing approaches to causal root-cause analysis in such systems address this only partially: they typically reason over a single observability modality and operate in an offline, operator-driven mode that does not match the demands of continuous vehicle operation. This paper presents SDVDiag, a multimodal causal-discovery pipeline that fuses log-based and metric-based service representations into a shared embedding space before graph construction, coupled with an anomaly-driven trigger that converts the diagnostic platform from a manually operated batch tool into a continuously running online system. Evaluation on an Autonomous Valet Parking testbed shows that the multimodal pipeline produces sparser causal graphs than a metrics-only baseline (134 vs. 182 edges on average) and consistently outperforms it in edge-weighted reward against an expert knowledge graph at every stage of human-feedback refinement, showing a 2.4-fold improvement over the baseline after 60 feedback queries. An end-to-end fault-injection scenario further demonstrates that the integrated trigger correctly recovers a true root cause located two causal hops upstream of the observable symptom.
