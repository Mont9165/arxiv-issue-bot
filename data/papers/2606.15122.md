# The Hitchhiker's Guide to Program Analysis, Part III: Mostly Harmless LLMs

- arXiv ID: `2606.15122v1`
- Authors: Haonan Li, Tianyang Zhou, Manu Sridharan, Hang Zhang, Zhiyun Qian
- Published: 2026-06-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.15122v1) | [pdf](https://arxiv.org/pdf/2606.15122v1)

## Abstract

LLMs are increasingly used in bug analysis to reason about code and judge whether a potential bug can be triggered in realistic execution contexts, with recent work showing promising empirical results. However, empirical effectiveness does not make a plausible model-generated rationale sufficient for discharging warnings. This distinction is especially important for no-bug decisions: dismissing a report or warning requires establishing that the reported error state is unreachable in the program context being analyzed, not merely offering a plausible explanation for why it may not occur. We argue that program-behavior reasoning should be grounded in formal analysis, rather than performed directly by LLMs.
  We present Evident, a bug analysis system that separates LLM assistance from program-behavior reasoning, delegating the latter to backend analysis. Given a warning specifying the reported location and data flow, Evident uses an LLM only to construct a warning-specific analysis harness. Evident then validates the harness before invoking the backend. The backend performs the harness-relative check: whether the reported error state is unreachable under the constructed harness and its assumptions. We evaluate Evident on 200 real Android kernel driver warnings from two existing static detectors. Evident correctly classifies 151 cases (76%), including discharging 111 false alarms, without discharging any confirmed bug in the dataset; the remaining cases are either unresolved or conservatively retained as potential bugs. Evident also rediscovers a confirmed vulnerability overlooked by both prior LLM-based filtering and manual triage.
