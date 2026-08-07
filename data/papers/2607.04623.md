# Can LLMs Really Recover Microservice Failures? A Recovery-Aware Evaluation of Diagnosis-to-Action Reasoning

- arXiv ID: `2607.04623v1`
- Authors: Jiaxing Qi, Zhongzhi Luan, Hongyu Zhang, Shaohan Huang, Carol Fung, Yongxin Tong, Hailong Yang, Depei Qian
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2607.04623v1) | [pdf](https://arxiv.org/pdf/2607.04623v1)

## Abstract

Large language models (LLMs) are increasingly used to interpret operational evidence and assist incident response in cloud-native microservice systems. However, recovery-oriented use cases require more than identifying a root cause. After observing symptoms and diagnosing a fault, an operator or agent must translate the diagnosis into a concrete recovery action, apply it to an admissible target, and verify that service health has been restored. Existing RCA and log-analysis evaluations are well-suited to diagnosis, but they do not characterize this subsequent action decision. This paper presents R2Act, a recovery-action evaluation framework for post-diagnosis incident response. R2Act defines an incident schema, quality gate, action-space representation, recovery-validity metrics, offline evaluator, and live-replay protocol. We instantiate the framework as a benchmark dataset of 302 quality-audited Kubernetes incidents from \system. Each incident provides synchronized multi-modal observations, root-cause labels, an incident-specific action space, and annotated valid and invalid recovery plans. We evaluate heuristic, supervised, RCA-oriented, deep log, and LLM-based methods. The strongest RAG-based LLMs reach 91.4\%--99.7\% root-cause service accuracy, yet their recovery validity remains only 36.8\%--60.3\%. Even when both the root-cause service and fault type are correct, recovery-oriented methods still choose invalid actions for 39.5\%--62.0\% of correctly diagnosed incidents. Overall, this work reveals that many recovery failures arise not from missing diagnostic knowledge, but from the difficulty of translating diagnostic evidence into valid recovery actions and admissible targets. This work provides a reproducible, simplified starting point for research and evaluation.
