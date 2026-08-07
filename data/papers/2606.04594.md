# Ekka: Automated Diagnosis of Silent Errors in LLM Inference

- arXiv ID: `2606.04594v1`
- Authors: Yile Gu, Zhen Zhang, Shaowei Zhu, Xinwei Fu, Jun Wu, Yida Wang, Baris Kasikci
- Published: 2026-06-03
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.04594v1) | [pdf](https://arxiv.org/pdf/2606.04594v1)

## Abstract

LLM serving frameworks are quickly evolving with a complex software stack and a vast number of optimizations. The rapid development process can introduce silent errors where output quality silently degrades without any explicit error signals. Diagnosing silent errors is notoriously difficult due to the substantial semantic gap between the high-level symptoms and the low-level root causes. We observe that diagnosis of silent errors can be effectively framed as a differential debugging problem by leveraging the existence of semantically correct reference implementations. We propose Ekka, an automated diagnosis system that identifies root causes by systematically aligning and comparing intermediate execution states between a target and a reference framework. We constructed a benchmark of real-world silent errors from popular serving frameworks, where Ekka shows 80% pass@1 diagnosis accuracy and 88% pass@5 diagnosis accuracy, outperforming state-of-the-art systems. Ekka also diagnoses 4 new silent errors from serving frameworks, all of which have been confirmed by the developers.
