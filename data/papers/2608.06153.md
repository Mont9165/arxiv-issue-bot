# Learning Globally Reusable Skills for Coding Agents

- arXiv ID: `2608.06153v1`
- Authors: Chen Yang, Jiashuo Tian, Ziqi Wang, Xinyin Liu, Meiru Ye, Junjie Chen
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.06153v1) | [pdf](https://arxiv.org/pdf/2608.06153v1)

## Abstract

Automated skill evolution enables Large Language Model (LLM) agents to continuously improve without expensive retraining. However, existing approaches typically treat skill evolution as a sequence of local updates, overlooking relationships among skills and often producing overfitted skill updates that fail to generalize across tasks. We propose GSE, a globalized skill evolution framework that jointly optimizes skill compatibility and skill generalization. To preserve consistency across the skill bank, GSE maintains a Skill Relation Graph (SRG) that explicitly models and co-evolves inter-skill relationships. To improve generalization, GSE performs cluster-based skill consolidation to abstract reusable capabilities from local updates and employs replay-driven verification to prevent overfitting and behavioral regressions. We evaluate GSE on two representative software engineering tasks: bug-revealing test generation and false-positive bug report filtering. Across two state-of-the-art coding agents, OpenHands and mini-SWE-agent, GSE consistently achieves the best precision, recall, and F1-score. Compared with existing evolution techniques, GSE improves precision and recall by 6.1%~34.1% and 31.8%~180.0% for test generation, and by 15.4%~96.4% and 13.1%~19.8% for false-positive filtering. Deployment on an internal industrial agent further yields a 61.4% improvement in F1-score, demonstrating the effectiveness and generalizability of GSE for evolving effective skills.
