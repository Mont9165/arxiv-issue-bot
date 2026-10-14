# TeleGen: Improving LLM-Based Web Application Generation via Runtime Telemetry

- arXiv ID: `2610.04981v1`
- Authors: Yujia Luo, Haonan Zhang, Jiasi Shen, Zishuo Ding, Weiyi Shang
- Published: 2026-10-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.04981v1) | [pdf](https://arxiv.org/pdf/2610.04981v1)

## Abstract

Large language models can generate runnable web applications from natural-language requirements, but many generated applications still fail interactive tasks. Existing generate-execute-repair pipelines execute the generated application and use task outcomes or error messages to guide code revision. However, this feedback often misses the runtime behavior between a browser action and the final task outcome, making interaction-level failures difficult to diagnose. Therefore, we propose TeleGen, an observability-enhanced framework for LLM-based web application generation. TeleGen instruments generated applications, collects runtime telemetry during task execution, and compresses raw telemetry logs into concise briefs for repair. We evaluate TeleGen on WebGen-Bench and Web-Bench. On WebGen-Bench, TeleGen improves task success from 67.7% with repair without telemetry to 76.2%, an increase of 8.5 percentage points. On Web-Bench, it improves cumulative Pass@2 from 21.7% to 29.8%. Ablation results show that runtime telemetry provides a useful diagnostic signal, while telemetry briefs make this signal more effective and less costly to use. Further analysis shows that telemetry is especially helpful for failures involving hidden execution paths, such as navigation, form workflows, and frontend-backend coordination.
