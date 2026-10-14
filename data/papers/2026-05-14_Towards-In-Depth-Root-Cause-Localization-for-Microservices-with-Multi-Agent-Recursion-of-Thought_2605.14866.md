# Towards In-Depth Root Cause Localization for Microservices with Multi-Agent Recursion-of-Thought

- arXiv ID: `2605.14866v1`
- Authors: Lingzhe Zhang, Tong Jia, Kangjin Wang, Chiming Duan, Minghua He, Rongqian Wang, Xi Peng, Meiling Wang, Gong Zhang, Renhai Chen, Ying Li
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.14866v1) | [pdf](https://arxiv.org/pdf/2605.14866v1)

## Abstract

As modern microservice systems grow increasingly complex due to dynamic interactions and evolving runtime environments, they experience failures with rising frequency. Ensuring system reliability therefore critically depends on accurate root cause localization (RCL). While numerous traditional machine learning and deep learning approaches have been explored for this task, they often suffer from limited interpretability and poor transferability across deployments. More recently, large language model (LLM)-based methods have been proposed to address these issues. However, existing LLM-based approaches still face two fundamental limitations: context explosion, which dilutes critical evidence and degrades localization accuracy, and serial reasoning structures, which hinder deep causal exploration and impair inference efficiency. In this paper, we conduct a comprehensive study of both how human SREs perform root cause localization in practice and why existing LLM-based methods fall short. Motivated by these findings, we introduce RCLAgent, an in-depth root cause localization framework for microservice systems that realizes multi-agent recursion-of-thought with parallel reasoning. RCLAgent decomposes the diagnostic process along the trace graph by assigning each span to a Dedicated Agent and organizing agents recursively and in parallel according to the graph topology, with the final diagnosis obtained by synthesizing the Root-Level Diagnosis Report and the Global Evidence Graph. Extensive experiments on multiple public benchmarks demonstrate that RCLAgent consistently outperforms state-of-the-art methods in both localization accuracy and inference efficiency.
