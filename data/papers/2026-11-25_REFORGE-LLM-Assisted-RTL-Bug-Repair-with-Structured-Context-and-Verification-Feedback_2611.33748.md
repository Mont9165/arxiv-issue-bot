# REFORGE: LLM-Assisted RTL Bug Repair with Structured Context and Verification Feedback

- arXiv ID: `2611.33748v1`
- Authors: Tanvir Hossain, Sudipta Paria, Aidan Gleason Myers, Swarup Bhunia, Tamzidul Hoque
- Published: 2026-11-25
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.33748v1) | [pdf](https://arxiv.org/pdf/2611.33748v1)

## Abstract

Large language models (LLMs) can write and repair RTL, but successful compilation or testbench execution does not establish defect removal, behavioral preservation, security, or implementation feasibility. Existing LLM-based RTL repair methods often report a single repair rate without retaining separate evidence for these properties, limiting reproducible comparison and integration into hardware design flows. We present REFORGE, which, to our knowledge, is the first LLM-assisted RTL repair framework that maintains and accumulates structured repair evidence across iterations, allowing it to generate fixes that satisfy multiple objectives simultaneously, including functionality, behavioral equivalence, security, and cost efficiency. REFORGE profiles buggy RTL, identifies structural and security-relevant features, localizes failing behavior, and uses verification-guided diagnosis to generate complete RTL repair variants. Each variant undergoes syntax checking, simulation, formal analysis, off-trigger preservation, security re-scan, and synthesis-based power, performance, and area analysis. We implement REFORGE as a backend-independent repair-and-verification flow and evaluate it in 288 runs across three LLM backends and three benchmark suites. On CirFix, the proposed context and diagnosis increase runs delivering a checked repair from 32/63 to 51/63, while every configuration repairs the Hack@DAC OpenTitan defect. Evidence records also show that a testbench-only criterion reports 3.9 times more repairs than the full set of applicable checks, security-clean outputs may lack functional verification, and different RTL repairs can implement equivalent hardware. These results show that LLM-generated RTL repairs require explicit multi-stage verification evidence rather than a single pass/fail outcome.
