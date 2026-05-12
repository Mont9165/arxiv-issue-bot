# Agentic Fuzzing: Opportunities and Challenges

- arXiv ID: `2605.10074v1`
- Authors: Junyoung Park, Insu Yun
- Published: 2026-05-11
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.10074v1) | [pdf](https://arxiv.org/pdf/2605.10074v1)

## Abstract

Fuzzers and static analyzers find many bugs but struggle with logic bugs in mature codebases. Triggering such a bug often requires multi-step reasoning that produces no distinctive execution feedback, and variants can appear across implementations too different for a single pattern to match. Recent LLM-assisted approaches help, but they use LLMs as auxiliaries rather than as the reasoning engine.
  We propose agentic fuzzing, a bug-finding approach seeded by historical bugs in which deep agents perform the reasoning directly. Given a reference bug, the agent analyzes its root cause, hypothesizes new scenarios elsewhere in the codebase that may share that cause, and verifies each hypothesis by generating and running proof-of-concept code. This lets the agent find variants that differ completely in trigger path or code structure from the reference.
  We identify three practical challenges in implementing agentic fuzzing: harness engineering, redundant investigations across seeds with similar root causes, and scheduling seeds in a large corpus. We address these in AFuzz through a four-stage agent pipeline, scenario coverage that deduplicates previously explored scenarios, and a DPP-MAP scheduler that orders seeds by diversity. We ran AFuzz on the V8 JavaScript engine for about one month, finding 40 bugs (including three duplicates), receiving a total $35,000 bounty, and being assigned two CVEs. AFuzz also found 19 bugs (including one duplicate) in SpiderMonkey and JavaScriptCore using the seeds from V8. However, agentic fuzzing is in its early stages with several remaining open problems we discuss in the paper. Still, we think it points to a promising direction for finding logic bugs.
