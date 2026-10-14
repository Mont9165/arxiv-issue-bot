# Can Large Language Models Generate Observability-Aware Code?

- arXiv ID: `2607.05785v1`
- Authors: Yongliang Tao, Hongyu Zhang, Pengfei Gao, Minghua Ma, Zhiyu Fan, Yu Kang, Jue Zhang, Si Qin, Liqun Li, Qingwei Lin, Saravan Rajmohan
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05785v1) | [pdf](https://arxiv.org/pdf/2607.05785v1)

## Abstract

Recent advances in coding agents have enabled the generation of increasingly complex software systems. While existing evaluations primarily focus on functional correctness, production systems must expose failure evidence to support observability. In this paper, we present a systematic study of observability in agent-generated systems. We examine whether agents can reconstruct source-level diagnostic semantics by restoring observability artifacts in 10 open-source and 8 industrial repositories. We also evaluate whether these artifacts translate into effective fault signals at runtime through 200 generated microservice systems deployed on Kubernetes with 13 injected faults. Our results reveal a consistent gap between diagnostic semantics at the source level and fault signals (i.e., explicit, fault-specific evidence) at runtime. At the source level, agents partially recover observability artifacts but struggle to capture key diagnostic semantics. At runtime, generated systems expose fault signals for only a small fraction of failures (up to 13.99\%), despite the presence of logging, suggesting that the generated observability artifacts may lack the failure-specific semantics needed to effectively expose faults. We further introduce an observability-oriented skill, which can serve as a guidance to improve both diagnostic semantics and fault-signal exposure, but the gains remain limited, indicating that the gap is not easily addressed. More broadly, our findings suggest that current evaluations focusing primarily on functional correctness may overlook observability as an important dimension of practical software quality.
