# Probe-and-Refine Tuning of Repository Guidance for Coding Agents

- arXiv ID: `2606.20512v1`
- Authors: Asa Shepard, Jeannie Albrecht
- Published: 2026-06-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.20512v1) | [pdf](https://arxiv.org/pdf/2606.20512v1)

## Abstract

LLM-based coding agents need higher-level operational knowledge about a repository (which files house which subsystems, how to run the test suite, which workflows have historically led to wrong fixes) that does not exist in the code itself. Engineers typically maintain \texttt{AGENTS.md} files to supply this context as instructions for coding agents, but whether they help is contested: recent studies disagree on whether LLM-generated guidance improves or harms agent performance. In this paper we show that how the guidance is produced is the decisive variable, and introduce \emph{probe-and-refine tuning}: a procedure that uses synthetic bug-fix probes to iteratively diagnose and patch a repository's guidance file through single-shot LLM calls, with no agent loop or tool use during tuning. On SWE-bench Verified across four independent trials with Qwen3.5-35B-A3B at 200 steps, probe-and-refine achieves 33.0\,\% mean resolve rate vs.\ 28.3\,\% for the static knowledge base used to initialize it and 25.5\,\% for an unguided baseline ($p < 0.001$ for both probe-and-refine contrasts). The improvement comes from coverage rather than precision: refined guidance produces evaluable patches for 14.5 percentage points (pp) more instances while per-patch precision remains statistically constant ($\sim$59\,\%, $p = 0.119$), showing that improved guidance helps agents reach the correct file rather than improving the quality of the changes they make. Further, a step-budget experiment shows that guidance is what lets the agent use a larger step budget productively, and a cross-model experiment with NVIDIA-Nemotron-3-Nano-30B-A3B finds that the tuning loop degrades when the model cannot generate sufficiently diagnostic output, though per-patch precision remains constant even then.
