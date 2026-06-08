# SkelDPO: A Skeleton-Guided Direct Preference Optimization Framework for Efficient Code Generation

- arXiv ID: `2606.06826v1`
- Authors: Yu Yu, Chen Lyu
- Published: 2026-06-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.06826v1) | [pdf](https://arxiv.org/pdf/2606.06826v1)

## Abstract

With the remarkable progress of Code Large Language Models (Code LLMs) in achieving semantic correctness, execution efficiency has become an increasingly important dimension for evaluating their practical utility. However, existing approaches typically treat full programs as a single optimization target during training, without explicitly modeling the structural factors that influence efficiency. As a result, although these models can generate semantically correct code, they fail to learn, at a fine-grained level, the underlying skeleton features that lead to efficient implementations. To address this limitation, we propose SkelDPO (Skeleton-Guided Direct Preference Optimization), a skeleton-guided preference optimization framework that systematically enhances the efficiency of code generation. SkelDPO first identifies efficient and inefficient implementations from the code dataset and, through comparative analysis, locates their efficiency-prone and inefficiency-prone points, forming alignment signals between efficiency and inefficiency skeletons. During training, a joint code and skeleton preference loss is introduced, enabling the model to learn semantic correctness while reinforcing its understanding of efficiency-critical components in code. Results show that SkelDPO consistently surpasses existing methods: compared with SOTA method that relies solely on efficient and inefficient code preference optimization, it improves Pass@1, Beyond@1, and Effi@1 by 3-6%, 3-7%, and 2-5%, with greater improvements observed on complex tasks. Overall, SkelDPO provides a new perspective on skeleton-level efficiency alignment, breaking the limitation of conventional preference optimization that relies solely on correctness or efficiency pairs. All datasets and source code are publicly available at: https://github.com/icpcSkelDPO/SkelDPO.
