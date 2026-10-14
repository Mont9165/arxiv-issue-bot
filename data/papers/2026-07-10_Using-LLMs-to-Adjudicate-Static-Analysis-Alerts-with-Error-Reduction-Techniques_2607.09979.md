# Using LLMs to Adjudicate Static-Analysis Alerts with Error Reduction Techniques

- arXiv ID: `2607.09979v1`
- Authors: William Klieber, David Svoboda, Lori Flynn, Ruben Martins
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09979v1) | [pdf](https://arxiv.org/pdf/2607.09979v1)

## Abstract

Static analysis is widely used for finding security weaknesses in source code before deployment, but it often produces far more alerts than analysts can review. We study how well large language models (LLMs) can adjudicate (classify as a real bug or a false alarm) static-analysis alerts. We use two mistake-mitigation methods: (1) a consistency check (CC) that runs the LLM multiple times and checks that the verdicts are consistent with each other, and (2) an LLM reasoning evaluation (LRE) step that runs the LLM multiple times and then asks the LLM to choose a verdict after evaluating the reasoning provided by each run.
  We evaluated several LLMs on three test suites: Juliet, FormAI, and SV-COMP. Across all three suites, the mid-tier reasoning LLMs that we tested (o4-mini, gpt-oss-120b, gpt-oss-20b) reach high recall (percent of real bugs that the tool correctly flags as needing repair / manual attention) and specificity (percent of actually false alerts that the tool correctly dismisses as false alarms). With mistake mitigation, they reach at least 98% recall and at least 94.8% specificity on every suite (with CC alone on Juliet and SV-COMP, and with LRE+CC on FormAI).
  We probe Juliet memorization and show that o4-mini can often reconstruct sanitized test cases' original identities, so we base our generalization claims primarily on FormAI, scored against our own unpublished manual adjudications. We also report results of using the LLM to synthesize a program that dynamically triggers the flaw as independent evidence; a validity check rejected every trigger driver aimed at a false alarm, so a valid trigger proved to be strong evidence of a real flaw.
