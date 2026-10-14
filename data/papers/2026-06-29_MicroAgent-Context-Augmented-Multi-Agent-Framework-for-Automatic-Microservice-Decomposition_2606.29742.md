# MicroAgent: Context-Augmented Multi-Agent Framework for Automatic Microservice Decomposition

- arXiv ID: `2606.29742v1`
- Authors: Zishan Su, Junjie Huang, Shiwen Shan, Xingyan Chen, Hui Zeng, Yuxin Su, Yanlin Wang, Michael R. Lyu
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.29742v1) | [pdf](https://arxiv.org/pdf/2606.29742v1)

## Abstract

The adoption of Microservice Architecture (MSA) has revolutionized software engineering by enhancing scalability, agility, and maintainability over traditional monolithic applications. As more developers transition their legacy systems to microservice-based architectures, effective microservice decomposition-partitioning monolithic applications into highly cohesive services-becomes vital. However, this decomposition task presents significant challenges. Manual approaches are time-consuming and labor-intensive. Existing automated methods often fail to capture the necessary semantic insights from complex applications, while naive applications of Large Language Models tend to overlook crucial contextual information and design principles, leading to suboptimal results.
  To address these challenges, we propose MicroAgent, a Context-Augmented Multi-Agent Framework for Microservice Decomposition. Our framework divides the decomposition process into five distinct subtasks and assigns each to a specialized agent. To enhance the effectiveness of each agent, we provide tailored, multi-granularity context that keeps its analysis focused and mitigates information overload. Furthermore, to ensure the decomposition adheres to established design principles, we integrate analytical tools that guide the agents' decision-making. Experimental evaluations on 10 Java Web applications demonstrate that MicroAgent achieves an average decomposition accuracy of 89.2%, outperforming the state-of-the-art method by 24.6%. We also conduct a case study to highlight the practical benefits of our design.
