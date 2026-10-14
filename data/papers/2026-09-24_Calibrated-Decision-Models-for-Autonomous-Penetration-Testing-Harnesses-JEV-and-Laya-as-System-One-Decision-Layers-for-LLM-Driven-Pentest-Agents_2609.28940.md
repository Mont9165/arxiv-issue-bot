# Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers for LLM-Driven Pentest Agents

- arXiv ID: `2609.28940v1`
- Authors: Joas Antonio dos Santos Barbosa
- Published: 2026-09-24
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.28940v1) | [pdf](https://arxiv.org/pdf/2609.28940v1)

## Abstract

Autonomous penetration-testing harnesses use large language models (LLMs) for reconnaissance, exploitation, and reporting, but often rely on those same models to confirm findings, grade severity, and select agents. This can lead to false positives, inflated severity, and wasted compute. We examine how System One decision models, lightweight non-generative classifiers that return typed, calibrated verdicts, can support these decisions. We make five contributions. First, we define four decision points: finding adjudication, severity recalibration, agent pruning, and confirmation loops. Second, we present an exploratory NeuroSploit case study comparing one run with TypeSafe System One (Jev) and one without it against a web target containing 13 vulnerabilities. Differences in severity distribution, runtime, and grading by exposed data type motivate the architecture but do not establish statistical significance. Third, we review published specifications for Jev, Jev-Ultrafast, and the open-source Laya without assuming that results from other benchmarks transfer to penetration testing. Fourth, we discuss RLHF, RLAIF, RLCD, and RLHV as training approaches and their implications for trust in security decisions. Finally, we propose Rave, a domain-adapted System One model, and outline its training data, evaluation protocol, and potential effect on harness assurance.
