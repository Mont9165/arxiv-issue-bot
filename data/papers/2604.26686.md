# When Model Editing Meets Service Evolution: A Knowledge-Update Perspective for Service Recommendation

- arXiv ID: `2604.26686v1`
- Authors: Guodong Fan, Cuiyun Gao, Chun Yong Chong, Lu Zhang, Jing Li, Jinglin Zhang, Shizhan Chen
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26686v1) | [pdf](https://arxiv.org/pdf/2604.26686v1)

## Abstract

The rapid evolution of software services poses substantial challenges to the design and implementation of effective recommendation systems. Traditional service recommendation approaches often rely on static representations and historical usage data, which are insufficient for adapting to the dynamic and evolving nature of service ecosystems. Recently, large language models (LLMs) have shown strong potential to overcome these limitations by leveraging rich contextual understanding. However, their practical use faces two major challenges: outdated service facts and invalid or redundant services. To address these issues, we propose EVOREC, an evolution-aware framework for service recommendation that leverages model editing in a locate-then-edit paradigm to incorporate updated service facts without costly retraining efficiently. This allows the model to remain aligned with evolving service ecosystems. To address invalid service issues, we introduce a Finite Automata (FA)-based constrained decoding mechanism with deduplication, which enforces structural and semantic validity while eliminating repeated services. Experiments on real-world service datasets demonstrate that our framework consistently outperforms existing baselines, e.g., achieving an average relative improvement of 25.9% in Recall@5. Moreover, under evolving service scenarios, our approach outperforms model fine-tuning approaches by 22.3%, demonstrating strong adaptability to service evolution and providing a practical solution for service recommendation in dynamic ecosystems
