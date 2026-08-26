# EMRB: A Multi-Level Benchmark for Evaluating LLM Reasoning over Raw Electromagnetic Signals

- arXiv ID: `2608.24086v1`
- Authors: Mingxu Zhang, Ying Sun, Yuhan Li, Yang Ji, Dazhong Shen, Ke Zhang, Shan Huang
- Published: 2026-08-25
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CE`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.24086v1) | [pdf](https://arxiv.org/pdf/2608.24086v1)

## Abstract

Large language models (LLMs) are increasingly used as code agents for scientific and engineering analysis, but their ability to analyze raw physical-layer measurements remains untested. We introduce \textbf{EMRB} (\textbf{E}lectro\textbf{m}agnetic \textbf{R}easoning \textbf{B}enchmark), which evaluates whether LLMs can analyze raw I/Q data by writing and running code. EMRB contains 200 problems across five difficulty levels and 27 question types, from signal detection to OFDM design, generated from 11 signal types with verified ground truth. Unlike benchmarks built on preprocessed features or structured tables, EMRB provides only the raw capture; the quantities each question refers to must first be discovered through code. We evaluate 14 LLMs spanning proprietary, open-weight, and reasoning-oriented families. Scores range from 24.1\% to 78.9\%, with the mean dropping from 84.9\% on basic measurement to 21.2\% on system design. We also propose \textbf{ReconPilot}, a structured method that separates signal reconnaissance, targeted analysis, and self-verification. Across three backbones, ReconPilot raises the overall score by 3.8 to 17.6 points and improves 13 of 15 backbone-level combinations tested. All data and code are publicly released in \href{https://github.com/mingxuZhang2/EMRB}{\textcolor{blue}{our GitHub repository}}.
