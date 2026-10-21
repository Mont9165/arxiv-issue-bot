# SWatcher+: A Holistic Approach to Deploying Learned Cardinality Estimators in a Dynamic Setting

- arXiv ID: `2610.28270v1`
- Authors: Yuxi Liu, Vincent Capol, Xiao Hu, Pankaj K. Agarwal, Jun Yang
- Published: 2026-10-20
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.28270v1) | [pdf](https://arxiv.org/pdf/2610.28270v1)

## Abstract

Cardinality estimation (CE) is crucial in database query optimization. Although recent advances have improved accuracy, deploying machine-learned CE models in dynamic databases remains challenging due to data updates and workload shifts. Retraining can be costly, but existing practices offer little guidance on when and how to update models, resulting in simple periodic retaining strategies that are suboptimal. We propose SWatcher+, a framework that adapts learned CE to dynamic workloads by monitoring data updates and query feedback. SWatcher+ selectively monitors high-impact subqueries for which wrong estimates lead to poor plan performance, and it proactively applies corrections to estimates during query optimization. This strategy enables immediate adaption to data and workload shifts without waiting for full model retraining, and carefully balances the cost and benefit of monitoring and adaption versus retraining. Our experiments show that SWatcher+ offers a better trade-off between query performance and overhead compared with existing approaches, making it a more practical solution for deploying learned CE in dynamic settings.
