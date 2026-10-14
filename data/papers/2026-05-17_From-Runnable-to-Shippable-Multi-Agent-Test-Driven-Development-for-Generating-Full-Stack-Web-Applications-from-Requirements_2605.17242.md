# From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating Full-Stack Web Applications from Requirements

- arXiv ID: `2605.17242v1`
- Authors: Yuxuan Wan, Tingshuo Liang, Jiakai Xu, Jingyu Xiao, Yintong Huo, Michael R Lyu
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.17242v1) | [pdf](https://arxiv.org/pdf/2605.17242v1)

## Abstract

Coding agents can generate web applications from natural-language descriptions, yet a recent benchmark study shows that generated applications fail to meet functional requirements in over 70% of cases. The core difficulty is that web correctness cannot be assessed from source files or terminal output: the application must be deployed, exercised through simulated browser interactions, and failures must be translated into actionable repair signals -- steps that current agents cannot perform without human mediation.
  We present TDDev, a framework that automates this closed loop through three stages: (1) converting high-level requirements into structured acceptance tests before any code is written, (2) deploying the application and validating it through browser-based interaction simulation, and (3) translating browser-observed failures into structured repair reports for the coding agent. Enabled by TDDev, we conduct the first controlled empirical study of Test-driven development (TDD) strategies for web application generation, comparing four development protocols across two coding agents, two backbone models, and two benchmarks. TDD infrastructure consistently improves generation quality by 34--48 percentage points over a no-TDD baseline. The central finding is that the optimal protocol depends on the model's generation style: models that build applications holistically benefit most from agentic enforcement, while models that extend code conservatively benefit from incremental enforcement. Mismatching protocol to generation style eliminates the TDD benefit entirely while multiplying token cost up to 25-fold. A user study confirms that TDDev reduces manual developer intervention to zero, shifting the workload from continuous prompt engineering to autonomous, feedback-driven refinement.
