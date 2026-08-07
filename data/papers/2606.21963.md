# Holmes: Multimodal Agentic Diagnosis for Mixed-Language Mobile Crashes at Industrial Scale

- arXiv ID: `2606.21963v1`
- Authors: Jia Li, Wenyuan Ma, Ting Peng, Haibin Zheng, Yuetang Deng
- Published: 2026-06-20
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.21963v1) | [pdf](https://arxiv.org/pdf/2606.21963v1)

## Abstract

Diagnosing mobile crashes in ultra-large-scale industrial applications is a formidable challenge due to the sheer volume of code, the complexity of mixed-language environments, and the inability to reproduce failures locally. Traditional static analysis struggles with scalability, while existing LLM-based agents often rely on reproducible environments unavailable in post-mortem scenarios. We present Holmes, a multi-agent system that automates root cause analysis by synthesizing multimodal runtime signals--stack traces, logs, and thread states--to reconstruct failure contexts without reproduction. Holmes introduces a hierarchical Retrieve-Explore-Reason architecture that leverages low-level artifacts (e.g., registers, assembly) to bridge the semantic gap between open-source business logic and closed-source system frameworks. By dynamically compressing the search space using runtime clues, Holmes precisely navigates 70-million-line codebases to identify non-local defects. Evaluated on real-world crashes from WeChat, Holmes achieves 87.6% accuracy in function-level fault localization and reduces average investigation time by over 98% (to ~77 seconds), demonstrating its effectiveness in transforming labor-intensive debugging into an efficient verification workflow.
