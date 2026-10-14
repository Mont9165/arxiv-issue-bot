# LadderTeam: Dual-Agent Laddering Elicitation Framework

- arXiv ID: `2608.17029v1`
- Authors: Manjushree Aithal, Alexander Kotz, James Mitchell
- Published: 2026-08-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2608.17029v1) | [pdf](https://arxiv.org/pdf/2608.17029v1)

## Abstract

Eliciting detailed and actionable software requirements from end-users is a critical phase in the iterative development of a software product or application. To ensure the feedback collected is detailed and actionable, software teams can leverage the laddering interview technique. While effective for ensuring granular and actionable items from the software feedback, these interviews are subject to several limitations. They are traditionally a manual process associated with a time and financial burden, limiting scalability; interviewers must balance probing for depth while managing interviewee behavioral and cultural constraints. To address these limitations, we present \textbf{LadderTeam}, an open, reproducible framework that automates UX wireframe interviews using a dual-agent Large Language Model (LLM) architecture. An active interviewer agent executes one of three probing strategies (ACV, 5-Whys, and JTBD) to elicit actionable software requirements from usability feedback comments, while a concurrent background Judge agent evaluates probe-response pairs and triggers real-time guardrails to prevent topic drift. To rigorously evaluate LLM laddering without participant variance confounds, we introduce a controlled simulation methodology utilizing scripted ground-truth transcripts to isolate probe quality as the sole experimental variable. Across 216 interviews, \textbf{LadderTeam} achieved 99.1\% chain convergence and an 81.0\% ground-truth actionable response match (86.1\% reluctant personality, 75.9\% terse personality) with zero drift across all runs. All evaluation code, all transcripts, inputs, and a live demonstration platform will be open-sourced upon acceptance.
