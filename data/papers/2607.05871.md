# DebugTracker: Lightweight Process Evidence for Classroom Debugging

- arXiv ID: `2607.05871v1`
- Authors: Jiatong Liu, Xue Yao, Zehua Zhang, Yongqiang Tian
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CY`
- Links: [abs](http://arxiv.org/abs/2607.05871v1) | [pdf](https://arxiv.org/pdf/2607.05871v1)

## Abstract

Debugging exercises are often assessed from final code and test outcomes, yet these artifacts hide how students reproduced failures, formed hypotheses, inspected evidence, edited code, and verified fixes. We present DebugTracker, a Visual Studio Code extension that records lightweight debugging-process evidence for classroom tasks. DebugTracker separates uncoached Evaluation Mode traces from coached Training Mode traces, stores append-only JSONL events, and exports timeline and Markdown reports for human review. The prototype records test commands, editor and debugger metadata, student checkpoints, source snapshots, optional image evidence, human labels, and optional AI-assisted practice feedback. DebugTracker is largely language-agnostic: it captures process evidence through standard VS Code mechanisms rather than language-specific tooling, although debugger evidence depends on the relevant VS Code language extension. We validate the prototype with debugging tasks in Python, TypeScript, and Java, 16 automated checks, and an 11-case manual trial matrix spanning packaged VSIX installation and three operating systems.
