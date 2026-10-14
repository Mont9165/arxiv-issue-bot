# From Fragments to Paths: Task-Level Context Recovery for Large Industrial Codebases

- arXiv ID: `2606.22906v1`
- Authors: Jiawei He, Weisong Sun, Mengyu Shi, Jie Jia, Tong Bian, Xikai Yang, Dong Sun
- Published: 2026-06-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.22906v1) | [pdf](https://arxiv.org/pdf/2606.22906v1)

## Abstract

Large language models have shown strong performance on software engineering (SE) tasks, yet understanding large industrial repositories remains challenging. Existing methods often retrieve only local fragments and fail to recover the broader task-relevant context needed for complex repository-level tasks. We present DeepDiscovery, a task-level repository-understanding method for large industrial codebases. DeepDiscovery uses a two-stage \textit{Location--Inference} framework to localize high-confidence task anchors and recover broader task-relevant context over multi-relational repository structure under budget constraints. Across controlled method-level evaluation, organization-internal industrial repository-understanding scenarios, and end-to-end evaluation on SWE-bench Verified, DeepDiscovery consistently improves task-relevant file recovery and downstream SE performance. On 27 medium-scale tasks, DeepDiscovery achieves the best file recovery quality among five representative baselines without offline preprocessing. On organization-internal industrial tasks from a production-scale integrated codebase ecosystem, including 27 medium-scale tasks and 40 large-scale tasks, DeepDiscovery improves Full Recall Rate across multiple AI coding systems, with absolute gains ranging from 1.6 to 9.2 percentage points on large subprojects and from 2.5 to 7.4 percentage points on medium-scale subprojects. In a controlled end-to-end evaluation on SWE-bench Verified, a system equipped with DeepDiscovery achieves a 78.6\% Solve Rate, outperforming the corresponding baseline by 8.2 percentage points. These results suggest that stronger task-level repository understanding can improve coding-agent performance on complex SE tasks.
