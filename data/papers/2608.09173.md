# A Resource-centric Analysis and Optimization of NoSQL Workloads using Distressed Resource Volume Metric

- arXiv ID: `2608.09173v1`
- Authors: Gunika Verma, Aashutosh A, Pooja Srinivas, Yogesh Simmhan, Ayush Choure, Harshit Shah, Mayukh Das, Prashant Sasatte, Chetan Bansal, Abhijit Pai, Suraj Dixit, Achint Agrawal
- Published: 2026-08-10
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2608.09173v1) | [pdf](https://arxiv.org/pdf/2608.09173v1)

## Abstract

Large-scale managed cloud databases leverage sophisticated load Packing and Migration (PAM) algorithms, which provide the efficiencies necessary for running these services at scale on cloud resources. Research into optimizing the resources and reliability of cloud databases at massive scales is limited by a lack of public NoSQL workloads. We address this in the context of Cosmos DB, Microsoft's flagship cloud-hosted NoSQL database. We first propose open-source NoSQL workloads from real Cosmos DB clusters, and analyze these traces to derive a novel reliability metric, Distressed Resource Volume (DRV), which captures the quality of service experienced by the end user. We then develop an open-source policy simulation framework, LoadStar, powered by a non-parametric statistical model of estimating the QoS of real traffic patterns. These form a reusable benchmark pipeline for validating policies for resource-centric NoSQL workloads. We then define a resource optimization problem for placing Cosmos DB replicas onto VM nodes, develop the Luna model for forecasting future load distributions, and the Orbit PAM algorithm that uses these forecasts to trigger and rebalance stressed replicas, to reduce tail-errors. Our experiments, validated using LoadStar for these workloads, demonstrate Orbit's benefits over the existing Cosmos DB policy and a worst-fit optimized baseline, with higher load delivered at lower error rates and up to $35\%$ reduction in resources. These have been deployed in production, with potential savings of $\$100M$s/yr while improving service reliability for millions of customers.
