# A Model-Centric DevOps Architecture for DEVS-Based Digital Twin Simulation Services

- arXiv ID: `2609.11122v1`
- Authors: Arnis Lektauers, Gusts Linkevičs, Guntis Mosāns, Arina Fokina, Rasa Gulbe
- Published: 2026-09-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CE`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2609.11122v1) | [pdf](https://arxiv.org/pdf/2609.11122v1)

## Abstract

Digital twin simulation models are evolved and redeployed like software, yet DEVS-based engines offer a sound formal basis with little support for versioning, automated validation, or continuous delivery in cloud-native environments, leaving model lifecycle management ad hoc in most deployments. This paper proposes a model-centric DevOps architecture for deploying DEVS-based digital twin simulations as managed services. Simulation models are treated as first-class DevOps artefacts defined in a declarative YAML language with a formal mapping to multiPDEVS, supporting structural and semantic validation in a CI/CD pipeline that produces immutable versioned artefacts, so that reverting to an earlier validated version reduces to pinning its identifier. The platform is decomposed into containerised microservices on Kubernetes, with engine adaptations for state externalisation and lifecycle control. An initial case study on the Riga Route 22 public-transit corridor, the first instantiation of a planned city-wide multi-modal transport digital twin for Riga, Latvia, exercises the full lifecycle and reports single-container engine throughput for a scenario with roughly 47,870 DEVS atomic components; pipeline-level catch statistics and cluster-level concurrent multi-scenario execution are the subject of companion empirical studies.
