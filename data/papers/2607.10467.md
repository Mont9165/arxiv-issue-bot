# Toward Production-Ready Federated Learning in Healthcare: Privacy, Orchestration, and Governance in MLOps

- arXiv ID: `2607.10467v1`
- Authors: Sakshi Gorkhali, Jonesh Shrestha
- Published: 2026-07-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.10467v1) | [pdf](https://arxiv.org/pdf/2607.10467v1)

## Abstract

Healthcare organizations often cannot freely centralize patient data because medical records are sensitive, regulated, and institutionally controlled. Federated learning offers a practical alternative by allowing hospitals and clinics to train a shared model while keeping raw data local. However, federated learning is not automatically production-ready or private by default. Model updates can still leak information, and decentralized training introduces operational challenges in deployment, monitoring, rollback, debugging, and governance. This paper examines how MLOps practices and the emerging idea of Federated Learning Operations (FLOps) can make federated healthcare machine learning systems scalable, reliable, and trustworthy. It answers three research questions: how containerization and orchestration support federated deployment, how privacy-preserving mechanisms affect trade-offs among privacy, utility, scalability, and operational complexity, and which post-deployment practices are most important for long-term governance. The central argument is that federated healthcare ML requires more than privacy-preserving algorithms. It needs an integrated MLOps architecture that combines reproducible deployment, secure orchestration, model versioning, audit logging, drift monitoring, heterogeneity management, and clear governance.
