# Rethinking Tool Design for Agentic RCA: A Controlled Empirical Study

- arXiv ID: `2610.05009v1`
- Authors: Yu Luo, Rongchen Gao, Zhenhui Zhou, Changchang Liu, Yuliang You, Yongqian Sun, Shenglin Zhang, Qiuai Fu, Shijie Wang, Dan Pei
- Published: 2026-10-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.05009v1) | [pdf](https://arxiv.org/pdf/2610.05009v1)

## Abstract

Large language model (LLM) agents are increasingly explored for root cause analysis (RCA) in microservice systems, yet empirical guidance on how to design and combine their tools remains limited. We conduct a controlled empirical study of tool abstraction and composition across models and microservice environments. We implement 24 structured tools for metric access (L1), evidence analysis (L2), and diagnosis (L3), alongside a Python-based reference setting (L0). Using 375 failure cases from three microservice systems, we evaluate eight configurations with Qwen3.7-Plus and compare four Qwen models on a shared subset of four configurations. Our results show that tool configurations affect root cause localization and failure type identification differently. With Qwen3.7-Plus, L3 achieves 82.8% top-1 localization accuracy compared with 85.4% for L0, while requiring less than half the time per case. Adding tool levels can improve type identification while reducing localization accuracy. Trajectory analysis reveals cases in which agents override correct diagnostic recommendations after consulting additional evidence. Model choice also changes tool benefits: adding L3 to L1+L2 improves diagnosis for three models but hurts Qwen3-8B, which rarely invokes L3. Tool configuration rankings further change across microservice systems. These findings provide an empirical foundation for designing and using RCA tools, guiding tool selection and composition according to the model, diagnostic objective, and target system.
