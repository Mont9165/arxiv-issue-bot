# ORCA-bench: How Ready Are Language Model Agents for Oncall?

- arXiv ID: `2607.28545v1`
- Authors: Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi
- Published: 2026-07-30
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.28545v1) | [pdf](https://arxiv.org/pdf/2607.28545v1)

## Abstract

Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system--exposing six days of metrics, logs, and traces through real telemetry interfaces (Prometheus, Jaeger, and OpenSearch via Grafana) and full source-code access--with 1,079 RCA tasks that systematically vary report specificity, time-to-detection, and co-occurring fault scenarios. Ground-truth symptoms are curated and signed off by expert SREs, and our LLM-as-judge is independently re-scored by humans (Cohen's $κ_w=0.90$). Across five frontier agents, the best RCA Accuracy is 25.3% on Medium-difficulty tasks (the realistic-input setting) and 10.0% on Hard--a gap that remains even with Claude Fable 5. The weakest model hallucinates an implausible root cause in 40% of incident reports, and removing source-code access degrades every metric. Crucially, these are performances on a curated 50 GB / six-day testbed with tasks investigated in isolation on a system whose code and instrumentation are public. Since real production systems are order of magnitudes larger, more dynamic, and more idiosyncratic, the gap we report is a lower bound on the engineering investment required before frontier coding agents can be safely entrusted with production reliability. We release the public set at https://hub.harborframework.com/datasets/orca-bench/ORCA-bench.
