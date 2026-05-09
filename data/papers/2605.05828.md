# From Chat to Interview: Agentic Requirements Elicitation with an Experience Ontology

- arXiv ID: `2605.05828v1`
- Authors: Dongming Jin, Zhi Jin, Yaotian Yang, Linyu Li, Zheng Fang, Yuanpeng He, Wenchun Jing, Xiaohong Chen
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.05828v1) | [pdf](https://arxiv.org/pdf/2605.05828v1)

## Abstract

Requirements elicitation interviews are crucial and time-consuming in requirements engineering, but heavily rely on the experience of requirements analysts. Although recent advancements in large language models (LLMs) have created new opportunities to automate this process, existing approaches rely solely on LLMs for free-form chat without taking into account the interview and development experience. That leads to the omission of implicit requirements and redundant questions. Practically, experienced analysts implicitly follow a structured cognitive framework when conducting requirements elicitation. Inspired by this observation, this paper proposes an interview agent named OntoAgent for the elicitation of requirements guided by an experience ontology. OntoAgent automatically analyzes domain-specific requirements descriptions to construct an experience ontology, which organizes requirements concerns into an ontology to support systematic and explainable interviews. During the interview, OntoAgent first performs four operations (i.e., ParseUser, ScoreOnto, ReRankOnto, GatePrune) guided by the ontology to identify the relevant requirement concerns. The selected concern is then combined with the current dialogue context to generate the elicitation question. To validate OntoAgent, we conduct comprehensive quantitative experiments using the widely adopted website application domain. The results show that OntoAgent significantly outperforms existing baselines in both elicitation effectiveness and questioning efficiency, achieving a 33% improvement in IRE and a 21% improvement in TKQR. Ablation studies further validate the contribution of each key design component. In addition, a qualitative user study demonstrates its practical advantages in real-world scenarios. We believe that OntoAgent can also be extended to requirements interview tasks in other domains.
