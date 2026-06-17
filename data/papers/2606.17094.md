# LogCopilot: Automating Log Aggregation Analysis through Large Language Models

- arXiv ID: `2606.17094v1`
- Authors: Senyu Xie, Chenxi Zhang, Tong Zhou, Jiacheng Liu, Xiaoyu Hong, Qingshan Li, Xin Peng
- Published: 2026-06-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.17094v1) | [pdf](https://arxiv.org/pdf/2606.17094v1)

## Abstract

Logs record the runtime behavior of software and are widely used in various tasks such as debugging, testing, and fault diagnosis. With the increase in system size and complexity, log analysis has gradually become a challenging task. Current industrial systems typically use log aggregation systems such as Grafana Loki and ELK to simplify the log collection and analysis process. Engineers write queries using the DSL query language provided by these systems can complete a variety of log analysis tasks. However, writing these queries is often time-consuming and labor-intensive, as it requires engineers to have a thorough understanding of the DSL syntax and the detailed information contained in the logs. To address these challenges, this paper proposes LogCopilot, an automated log aggregation analysis framework based on large language models (LLMs). LogCopilot accepts natural language log analysis instructions and accomplishes automated log analysis through knowledge retrieval and tool calling. LogCopilot constructs a hierarchical knowledge base to represent and provide key knowledge in logs. And it achieves automated log aggregation analysis by generating and executing LogQL queries. The evaluation based on four log datasets confirm the effectiveness of LogCopilot, which achieves an average accuracy of 76.8% and outperforms baseline approaches. Moreover, experiment results shows that LogCopilot is effective in LogQL query generation.
