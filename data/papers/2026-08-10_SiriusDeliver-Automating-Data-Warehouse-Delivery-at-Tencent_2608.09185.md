# SiriusDeliver: Automating Data Warehouse Delivery at Tencent

- arXiv ID: `2608.09185v1`
- Authors: Haining Xie, Xiaokai Zhou, Jiaming Yang, Siqi Shen, Ziwei Wang, Yifeng Zheng, Tengyue Xu, Yipeng Shi, Zefang Zong, Yang Li, Peng Chen, Jie Jiang, Debiao He, Xiao Yan, Jiawei Jiang
- Published: 2026-08-10
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.09185v1) | [pdf](https://arxiv.org/pdf/2608.09185v1)

## Abstract

Enterprise data warehouses (DWs) support business-critical analytics, but warehouse task delivery remains a complicated production process involving context retrieval, workflow configuration, code generation, platform submission, and failure diagnosis. Although large language models (LLMs) and coding agents have improved software development, they are insufficient for production DW delivery, which requires dependency-aware orchestration, lifecycle-aware artifact control, and continuous adaptation to evolving platform practices. We present SiriusDeliver, an end-to-end delivery automation agent for production warehouse task submission. SiriusDeliver integrates three components: a hierarchical delivery agent that orchestrates warehouse skills, an artifact lifecycle control module that verifies and revises artifacts before and after platform execution, and a trace-driven skill evolution mechanism that maintains reusable skills from delivery trajectories. We evaluate SiriusDeliver through offline datasets and large-scale production deployment on Tencent Cloud WeData. Offline experiments on real-world warehouse delivery cases show that SiriusDeliver improves delivery success and automation efficiency over representative baselines. During a two-month deployment across 6 business teams and 4 warehouse task types, SiriusDeliver served 3,600 monthly active users and supported 18,240 delivery sessions, achieving an 87.2% end-to-end success rate and a 73.5% autonomous submission rate. A one-month A/B test shows that SiriusDeliver reduces median delivery time from 228 to 23 minutes and engineer effort from 95 to 11 minutes, while maintaining comparable final delivery success.
