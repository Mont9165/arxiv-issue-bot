# LLM-Assisted Software Migration: from Module-Level Transformation to Repository-Level Integration

- arXiv ID: `2611.29942v1`
- Authors: Yanan Zhang, Shengqi Liu, Tao Zhang, Yidi Liu, Alan Tang, Hailong Chen, Yantao Jia
- Published: 2026-11-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.29942v1) | [pdf](https://arxiv.org/pdf/2611.29942v1)

## Abstract

Software migration adapts an existing implementation to a new language, version, API, framework, or platform while preserving its behavior. Large language models (LLMs) succeed on individual functions and modules, but this success does not readily carry over to entire repositories, particularly deployable applications. This survey reviews LLM-assisted migration from module-level transformation to repository-level integration, culminating in the delivery of complete applications. We analyze 96 sources---including 46 direct migration papers---across four perspectives: (1) supported software engineering activities, (2) model roles as editors or orchestrators, (3) orchestration workflows (agentless, single-agent, or multi-agent), and (4) enabling techniques including knowledge engineering, project context, environment feedback, and model adaptation. We then compare evaluation practices and benchmarks. Although 30 of the 46 studies target repositories, most acceptance evidence relies merely on build success, supplied tests, or static and model-based proxies. Moreover, compilation, visual similarity, test outcomes, and runtime behavior capture fundamentally distinct properties and cannot be conflated into a single success rate. We also identify critical gaps in requirements engineering support and in controlled comparisons of agent architectures. Finally, we discuss six open problems: application integration, platform differences, non-functional properties, generalization, attribution of gains, as well as cost and maintenance.
