# Knowledge-Based Zero-Replay Debugging of Multi-Agent LLM Traces

- arXiv ID: `2606.14805v1`
- Authors: Dong Ho Kang, Hyeonjeong Cha, Daein Weon
- Published: 2026-06-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.14805v1) | [pdf](https://arxiv.org/pdf/2606.14805v1)

## Abstract

Reliable operation of multi-agent large language model (LLM) systems depends on debugging long execution traces, where the few causally decisive events are buried in unstructured logs of messages, routes, memory writes, and tool calls. The standard tool is counterfactual replay (rewind, edit, and re-run the trajectory to measure each event's effect), but its cost grows linearly with the number of candidate events, making exhaustive replay infeasible at scale. We frame trace debugging as a knowledge-based decision-support problem. Each trace is compiled into a structured event knowledge graph over routing, memory, tool-use, uncertainty, and latent evidence, and a calibrated predictor decides where a scarce replay budget should be spent. We do not propose a new replay oracle; we propose a method to predict its results without paying the replay cost. We formulate zero-replay counterfactual-effect prediction: given a trace under a fixed budget, predict which events the oracle would mark high-effect before any replay is performed. BranchPoint-Latent is a lightweight predictor over observable, structural, uncertainty, and latent features of the knowledge graph. Calibrated against a deterministic replay oracle across 37 trace families, a single learning-to-rank gradient-boosted predictor raises per-trace localization (Branch Recall@5) from 0.73 to 0.93 on held-out families at zero oracle-replay cost. Rather than claiming universal dominance, we characterize when cheap graph centrality suffices and when learned evidence is necessary. The result is an auditable, cost-efficient decision-support system for AI-reliability debugging, positioned explicitly on the cost-accuracy frontier with reproducible artifacts.
