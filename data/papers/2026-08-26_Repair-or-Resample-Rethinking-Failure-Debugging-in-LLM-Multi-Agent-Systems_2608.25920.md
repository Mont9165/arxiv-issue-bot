# Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems

- arXiv ID: `2608.25920v1`
- Authors: Zhongwen Luan, Xiaoyu Zhang, Ming Hu, Yue Yang, Jiongchi Yu, Xiaohong Chen
- Published: 2026-08-26
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.25920v1) | [pdf](https://arxiv.org/pdf/2608.25920v1)

## Abstract

As large language model (LLM)-based multi-agent systems (MASs) are increasingly applied to long-horizon complex tasks, their reliability has emerged as the core bottleneck hindering their real-world deployment. Existing MAS debugging and repair methods typically rely on rerunning and resampling the entire execution trajectory. However, a fundamental question remains to be answered: do these methods causally repair MAS failures or merely stochastically repair by leveraging the randomness of LLM sampling? To evaluate the effectiveness of MAS repair methods, we introduce SymTrace, a controlled evaluation framework that records the MAS execution trajectory and establishes intervention anchors. During replay, it effectively reconstructs the execution before the anchor using recorded logs and only regenerates the downstream trajectory, thereby enabling the reliable reproduction of MAS failures. We further construct the dataset SymFail, comprising 536 human-annotated failure trajectories with graph-linked locations, categories, and trace evidence. Based on these foundations, we conduct a large-scale empirical study across three mainstream MAS frameworks. Our findings reveal that existing unguided rerun methods are highly unreliable, exhibiting low failure reproduction and repair rates (only 67.97% and 6.90%, respectively). Building upon these findings, we further explore the effectiveness of a symptom-driven intervention method, which successfully repairs 20.15% of the failed cases (a 191.89% improvement to state-of-the-art repair methods). This study aims to provide actionable insights for MAS debugging and repair research, paving the way for the robust deployment of multi-agent systems.
