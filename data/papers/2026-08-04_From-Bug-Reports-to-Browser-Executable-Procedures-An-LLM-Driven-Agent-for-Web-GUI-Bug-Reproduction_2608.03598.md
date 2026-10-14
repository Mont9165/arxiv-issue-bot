# From Bug Reports to Browser-Executable Procedures: An LLM-Driven Agent for Web GUI Bug Reproduction

- arXiv ID: `2608.03598v1`
- Authors: Cunming Zhang, Yu Pei, Michail Papadakis
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03598v1) | [pdf](https://arxiv.org/pdf/2608.03598v1)

## Abstract

Reproducing web GUI bugs from natural-language bug reports is critical for software maintenance, but remains difficult because reports often lack prerequisites such as dependencies and input files. Existing bug reproduction techniques mainly target code units or mobile applications and lack end-to-end visual execution and validation for web GUIs. We present ReBug, a context-aware agent system that reconstructs, executes, and validates browser-level reproduction procedures from web GUI bug reports by driving a real browser. ReBug separates reproduction into two stages. In the preparation stage, ReBug reconstructs missing prerequisites from the report and available artifacts, and it produces a high-level reproduction plan. In the execution stage, it performs tool-mediated interactions in the browser, maintains structured summaries of page state and action history, and validates the final state against expectations derived from the report. We evaluate ReBug on 667 real-world bug reports from four open-source web applications. On controlled current deployments, ReBug outperforms both baselines, achieving an average RSR of 49.96%, a mean task completion rate of 74.96%, and a mean action execution success rate of 86.54%. Our results show that explicit context reconstruction and state-aware browser execution effectively support report-derived browser reproduction, while historical replay shows that successful procedures often expose the original bug-present behavior on restored buggy versions.
