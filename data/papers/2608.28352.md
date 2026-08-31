# No Silver Bullet: Boosting GaussDB Performance on the 30TB TPC-H Workload

- arXiv ID: `2608.28352v1`
- Authors: Tim Zeyl, Jason Lam, Shu Lin, Reza Pournaghi, Qi Cheng, Calvin Wong, Kaixiang Du, Yuliang He, Yang Sun, Weicheng Wang, Paul Lee, Chen Ruo, Yang Xinyi, Li Qunan, Wang Junjie, Hu Dongxing, Chong Chen, Per-Ake Larson
- Published: 2026-08-28
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2608.28352v1) | [pdf](https://arxiv.org/pdf/2608.28352v1)

## Abstract

GaussDB is Huawei's premier database system, designed for large-scale deployments and the most demanding workloads. It is a distributed shared-nothing system, capable of handling all types of workloads. This paper outlines a series of modifications to GaussDB aimed at improving its performance on large-scale and complex analytical workloads. After these changes, its performance on the TPC-H workload exceeded the best published result by 40% at 30 TB.
  The key enhancements to achieve this elite performance include adopting a pipeline execution model, a faster and more scalable inter-node data shuffle, exploiting a unified bus and unified remote memory access. We also expanded the support of cost-based Bloom filter placement and implemented several Bloom filter streaming strategies, enabling their use across nodes.
