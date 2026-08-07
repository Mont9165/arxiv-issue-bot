# Dashboard2Code: Evaluating Multimodal Models on Reconstructing Interactive Dashboards

- arXiv ID: `2607.04727v1`
- Authors: Tianhao Niu, Ziyu Han, Qiguang Chen, Shiqi Zhou, Baocai Shan, Hengjie Fang, Qingfu Zhu, Wanxiang Che
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CV`
- Links: [abs](http://arxiv.org/abs/2607.04727v1) | [pdf](https://arxiv.org/pdf/2607.04727v1)

## Abstract

Automatic data visualization generation has advanced rapidly with multi-modal large language models, yet existing efforts largely focus on static charts and overlook the interactive dashboards commonly used for real-world data exploration. We introduce Dashboard2Code, a novel task that requires a model to proactively explore an interactive dashboard, acquire and integrate feedback from its own interactions (e.g., clicking and filtering), and generate code that reproduces the target dashboard. To support comprehensive evaluation, we present DashboardMimic, the first Plotly+Dash benchmark for Dashboard2Code, comprising 180 carefully designed and manually verified dashboard-code pairs spanning three difficulty levels and covering eight common real-world interaction patterns. We further propose an automated evaluation framework tailored to dashboards that combines code semantic analysis with dynamic interaction-based testing to assess visual and interaction consistency, showing strong agreement with human judgments. Experiments across a range of open- and closed-source multi-modal models reveal that even the strongest systems struggle on high-complexity dashboards and that a substantial performance gap remains between open-source and closed-source models on the Dashboard2Code task.
