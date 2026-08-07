# Not as Sweet by Another Name: An Empirical Study of Format Robustness in LLM Document Workflows

- arXiv ID: `2607.27648v1`
- Authors: Xiaoyu Zhang, Xianyun Cheng, Tianlin Li, Yuwei Zheng, Yue Yang, Yang Liu
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.27648v1) | [pdf](https://arxiv.org/pdf/2607.27648v1)

## Abstract

LLM-driven software systems are rapidly evolving from plain-text conversations to document-centric end-to-end workflows, where the same semantic content can be delivered in diverse document formats (e.g., CSV) through file upload interfaces. Yet existing testing work focuses on the robustness and reliability of models and systems whose input is a single prompt string, leaving a critical question unanswered: Can these document workflows maintain robust behaviors when the same content arrives in a different document format? To fill the gap, in this paper, we propose a format-aware metamorphic testing framework with three metamorphic relations to comprehensively evaluate the format robustness of end-to-end LLM document workflows. Based on this framework, we conduct a large-scale empirical study spanning four representative LLM workflows, four real-world tasks, and four document formats, comprising a total of 48,000 workflow executions. Our findings reveal that format variation poses a systematic and serious threat. Merely switching formats can cause accuracy to drop by up to 53.63% and trigger decision drifts in over 41% of instances. We further design lightweight mitigation strategies from the users' perspective that recover up to 44.21% of format-induced decision drift without model retraining. Our study demonstrates that document format is not a neutral wrapper but a critical factor affecting the reliability of LLM software systems, calling for corresponding testing and safeguards in the deployment in real-world high-stakes scenarios.
