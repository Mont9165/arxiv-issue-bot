# Step-Aligned Script Generation with Verification and Recovery for Web Automation Testing

- arXiv ID: `2610.25601v1`
- Authors: Hridya Dhulipala, Xiaokai Rong, Aashish Yadavally, Tien N. Nguyen
- Published: 2026-10-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.25601v1) | [pdf](https://arxiv.org/pdf/2610.25601v1)

## Abstract

Automated generation of end-to-end web tests remains costly: developers must identify stable selectors, encode multi-step workflows, attach assertions, and maintain scripts as interfaces evolve. Recent LLM-based web agents can complete natural-language tasks in a live browser session, but task completion is not the same as producing a test-ware artifact - code that is executable, replay-able from a reset state, inspectable by developers, and tied to an oracle. We present TESSARA, an adaptive test-script generation framework that converts natural-language test intent into Playwright scripts consisting of executable interaction code, goal-state assertions, and step-level provenance linking each step to its generated code fragment, selector evidence, execution outcome, and repair history. TESSARA grounds each planned step via Step-Aligned Scripting (SAS), enabling fine-grained failure localization, selective regeneration of failing suffixes, and reversibility-aware backtracking that avoids undoing likely commit points (e.g., form submissions). A three-level verification pipeline (syntactic, execution, and semantic/oracle), detects and repairs malformed code, interaction failures, and incorrect landing states. We evaluate TESSARA on three public web benchmarks, measuring script executability, oracle satisfaction, replay stability, and repair efficiency, and show substantial improvements over baselines and underlying VLMs used directly as script generators.
