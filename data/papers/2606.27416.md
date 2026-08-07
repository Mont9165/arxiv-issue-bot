# Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents

- arXiv ID: `2606.27416v1`
- Authors: Vassili Philippov, Pavel Katunin, Dmitry Andreev, Igor Ostanin, Anton Nikolaev
- Published: 2026-06-25
- Primary category: `cs.MA`
- Categories: `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.27416v1) | [pdf](https://arxiv.org/pdf/2606.27416v1)

## Abstract

LLM coding agents make it tempting to automate empirical research by delegating experiments to them directly, but naive delegation does not scale to large projects: low-rate instruction lapses compound into broken, irreproducible artefacts. To address this problem, we present Glite ARF, an open-source Python framework for running many LLM coding agents in parallel on a research repository without sacrificing reproducibility or auditability. The framework defines a three-role stack: a human researcher chooses which hypotheses to test, coding agents (Claude Code, Codex CLI) implement individual tasks under a fixed structure, and deterministic Python verifier scripts enforce task isolation, immutability of completed work, a corrections overlay, and a materialised project overview. We call this verifier-driven research: the rules of the research process live in code that fails loudly when violated, not in prose that agents are merely asked to follow. Using Glite ARF, we developed our submission to the BEA 2026 vocabulary-difficulty shared task, placing first in the closed track and second in the open track on all three target languages (Spanish, German, Mandarin) and reducing the official baseline RMSE by 29.9% (closed) and 35.9% (open). The campaign comprised 273 tracked tasks (146 experiment runs) across 129 feature sets, run by up to twelve parallel agents orchestrated from a single laptop - with some model training on rented A100s - at approximately \$450 in LLM API spend (\$498 total third-party cost), and structured per-fold provenance let us catch and strip four target-leaking feature sets, correcting an implausible 0.609 RMSE to 0.802. Across three campaigns in three domains, the framework's structural machinery adds only about 1% of wall-clock time. Framework and a public demo project accompany this paper.
