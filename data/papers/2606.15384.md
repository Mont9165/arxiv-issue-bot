# CoeusBI: A Comprehensive Interactive Business Intelligence System Powered by LLMs at Baidu [Extended Version]

- arXiv ID: `2606.15384v1`
- Authors: Jinqing Lian, Chaofan Li, Yingxia Shao, Ming Wang, Yang Dong, Xinyi Liu, Wei Zhang, Chaoxian Gui, Tianqi Wan, Ming Dong
- Published: 2026-06-13
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.15384v1) | [pdf](https://arxiv.org/pdf/2606.15384v1)

## Abstract

The advent of Large Language Models has catalyzed the emergence of interactive Business Intelligence (BI) systems. Although commercial BI products increasingly adopt semantic layers paired with natural language interfaces, they predominantly rely on manual configurations to define metrics and dimensions. Real-world deployments face critical challenges: (a) frequent JOIN operations degrade the accuracy of SQL generation; (b) wide schemas exacerbate the challenge of schema linking; and (c) the generation of dialect-specific queries and the accurate support for multi-round dialogues incur high computational costs and yield limited accuracy. We introduce CoeusBI, an industrial-scale interactive BI system that addresses these barriers through a novel Dual-Agent Architecture paired with a Hierarchical Schema Linking module: (1) an offline View Generation Agent that utilizes error-feedback to autonomously convert complex JOIN queries into simple single-view queries, which eliminates the need for manual semantic modeling; (2) a Hierarchical Schema Linking module that leverages vector retrieval over views to handle exceptionally wide schemas efficiently; and (3) a dynamic Routing Agent that evaluates dialogue contexts to route queries, dynamically invoking either the synthesis of new intermediate representations or targeted modifications of existing ones, before compiling the unified representation via a deterministic SQL compiler that is agnostic to dialects. Extensive experiments on both public datasets and production datasets demonstrate that CoeusBI achieves significant improvements in query accuracy, token efficiency, and user satisfaction relative to existing methods. CoeusBI is deployed as a standalone service on the data platform of Baidu and is widely used across multiple business lines supporting thousands of users daily, thereby evidencing strong practicality and scalability.
