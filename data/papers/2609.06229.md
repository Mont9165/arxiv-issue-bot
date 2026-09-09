# SWE-Test: Benchmarking LLM Vulnerability Discovery via Input Prediction

- arXiv ID: `2609.06229v1`
- Authors: Yuanxiang Shi, Jiayi Lin, Xuanyong Lin, Liangcai Su, Yeheng Duan, Wei Wang, Qi Han, Bing Zhao, Wei Hu, Xander Xu, Chenxiong Qian
- Published: 2026-09-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.06229v1) | [pdf](https://arxiv.org/pdf/2609.06229v1)

## Abstract

Vulnerability discovery is becoming an important ability of large language model (LLM) agents: agents that silently miss real defects leave critical software exposed. Rigorously measuring this ability is therefore urgent, but existing benchmarks are gameable through data contamination, score recall against an unknowable vulnerability set, often rely on synthetic bugs, and report a single end-to-end verdict that cannot localize where an agent fails. Vulnerability discovery is a composite ability: an agent must comprehend source code, infer input constraints, construct inputs, execute them, and iteratively correct from feedback. We recast its measurement as an input-prediction task with a closed, deterministic ground truth: using coverage-guided fuzzing, we mine deep target branches in real-world C/C++ programs and ask an agent to predict an input that drives execution to a given branch. This decomposes discovery into three task modes over 22 real-world C/C++ programs spanning 15 domains. Open-loop and Feedback-enabled share 60 fixed-target task instances across 16 of these codebases (13 domains), testing input construction without and with a distance oracle to isolate code comprehension from feedback-driven correction. Online Arena instead removes the predefined target and scores path exploration by coverage gain on a separate, partially overlapping pool of 11 programs; agents collectively confirmed 13 distinct bugs across six programs. Evaluating 15 default-effort model-scaffold configurations, the best reaches only 55.0% pass rate in the Feedback-enabled mode, and the mean across seven paired Claude Code configurations is 36.4% with feedback versus 19.3% without. Decomposing failures, we find constraint inference, not navigation, is the dominant bottleneck. We release SWE-Test with a turnkey evaluation environment.
