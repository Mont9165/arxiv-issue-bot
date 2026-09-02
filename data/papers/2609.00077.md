# Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops

- arXiv ID: `2609.00077v1`
- Authors: Bowei He, Weixu Zhang, Yili Jin, Xue Liu
- Published: 2026-08-31
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.00077v1) | [pdf](https://arxiv.org/pdf/2609.00077v1)

## Abstract

Code-level autonomous research loops (ARLs) have recently emerged as a concrete object of study in automated machine learning research. In such loops, an LLM agent proposes modifications to an experimental training pipeline, executes the modified pipeline, and retains edits that improve a verifiable in-loop metric. Although executable metrics may appear to provide a reliable signal of progress, it remains unclear whether repeated metric-driven code editing leads to genuine improvements that generalize beyond the loop. We provide a systematic diagnosis of this question. Across various experiment settings, we identify a robust failure mode that we call \textbf{algorithmic mode collapse}. In this regime, surface-level edit diversity remains stable, but semantic and mechanism-level diversity collapse: the agent continues to edit different lines of code while repeatedly proposing the same kinds of algorithmic changes. This collapse is accompanied by a widening gap between in-loop metric gains and gains measured on independent held-out evaluations. We then propose Diversity-Aware Proposal Sampling (\textsc{DAPS}), a lightweight mitigation that combines category-coverage reweighting, persistent edit memory, and a validation gate. Under a three-tier protocol separating the in-loop metric, the audit metric read by the gate, and a blind metric no loop component ever accesses, \textsc{DAPS} reduces semantic-cluster decay of edits by $69.1\%$ and improves relative faithfulness by $83.7\%$ blind and $81.6\%$ audited, while preserving in-loop optimization speed. We provide the code in Github \href{https://github.com/BokwaiHo/arl-mode-collapse}{repository}.
