# Is Agentic AI Ready for Real-World Hardware Engineering? A Deep Dive with Phoenix-bench

- arXiv ID: `2605.15226v1`
- Authors: Qingyun Zou, Feng Yu, Hongshi Tan, Bingsheng He, WengFai Wong
- Published: 2026-05-13
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.15226v1) | [pdf](https://arxiv.org/pdf/2605.15226v1)

## Abstract

We ask whether agentic AI systems built for software engineering transfer to realistic hardware engineering. Existing hardware LLM benchmarks isolate sub-tasks but none jointly requires repository navigation, hierarchy-aware localization, Electronic Design Automation (EDA) executable verification, and maintenance-style patching. We introduce \textbf{Phoenix-bench}, a synchronized corpus of 511 verified Verilator instances from 114 GitHub repositories, each shipped with the developer patch, design-flow labels, fail-to-pass and pass-to-pass testbenches, and a Docker-pinned EDA environment so resolved-rate differences reflect agent behavior rather than toolchain availability. Using Phoenix-bench we run a uniform evaluation of four commercial agents and eight open-source agentic structures across four LLM backbones, plus two diagnostic interventions (file-level oracle localization and one round of testbench-log feedback). Three findings emerge. (i)~Software and hardware are fundamentally different engineering tasks: the same agent loses 37\% to 58\% from SWE-bench Verified to Phoenix-bench because hardware bugs propagate across parallel instantiated modules through signal flow rather than along a software-style call graph, and software-tuned agents stop at the symptom file instead of tracing back through the instantiation chain. (ii)~Failures concentrate on design control-flow / finite state machine (FSM) bugs, verification testbench bugs, and hard cases that demand cross-hierarchy signal-flow tracking and coordinated multi-file edits. (iii)~Localization granularity matters far more than localization itself: a perfect file-level oracle yields only $+1.4$\% because the agent then breaks files that did not need editing, while a single round of test case feedback lifts resolved rate by $42$\% to $45$\% because the test case tells \emph{where} the bug is and \emph{what} the fix has to look like.
