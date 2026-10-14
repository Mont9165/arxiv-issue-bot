# RigorBench: Benchmarking Engineering Process Discipline in Autonomous AI Coding Agents

- arXiv ID: `2606.22678v1`
- Authors: Meher Bhaskar Madiraju, Meher Sai Preetam Madiraju
- Published: 2026-06-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.22678v1) | [pdf](https://arxiv.org/pdf/2606.22678v1)

## Abstract

Agentic coding harnesses - such as Agent-Skills, Superpowers, and Agent-Rigor - are increasingly deployed to augment underlying LLMs for real-world software engineering tasks. Existing benchmarks evaluate these agents almost exclusively on outcome correctness: whether generated code passes tests or resolves issues. We argue that this outcome-only lens is insufficient: an agent that arrives at a correct solution through reckless trial-and-error, without planning, verification, or graceful recovery, is fundamentally less reliable than one that follows sound engineering discipline. We introduce RigorBench, the first benchmark designed to measure process discipline in AI coding agents. RigorBench evaluates these harnesses across five pillars: Planning Fidelity, Verification Coverage, Recovery Efficiency, Abstention Quality, and Atomic Transition Integrity. A composite RigorScore aggregates these dimensions into a single metric via a weighted sum. We curate a suite of 30 tasks spanning five categories - Plan-Then-Build, Verify-Or-Die, Doom Loop Gauntlet, Know When to Fold, and Don't Break the Build-and evaluate leading harnesses in a controlled with/without experimental design against baseline coding assistants. Our results show that structured process discipline not only improves process quality scores by an average of 41% but also raises downstream outcome correctness by 17%, providing the first quantitative evidence that how agents code matters as much as what they produce. We release the full benchmark, scoring rubrics, and trajectory analysis tools as open-source artifacts.
