# LLM-as-a-Judge for Human-AI Co-Creation: A Reliability-Aware Evaluation Framework for Coding

- arXiv ID: `2604.27727v1`
- Authors: Md Faizul Ibne Amin, Yutaka Watanobe, Daniel M. Muepu, Haruto Suzuki, Kenta Nanaumi, Md Mostafizer Rahman
- Published: 2026-04-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.27727v1) | [pdf](https://arxiv.org/pdf/2604.27727v1)

## Abstract

LLMs are increasingly employed both as judges for evaluating open-ended outputs and as co-creation partners in AI-assisted programming; yet rigorous evaluation in human-AI co-creation settings remains underdeveloped as judgments must be reliable, comparable across models, and interpretable over multi-turn interaction. To address this gap, a rubric-driven LLM-as-a-Judge framework is presented for contest-style human-AI co-creation in coding and software engineering (SE). The framework is built around schema-constrained judge outputs, validation and repair mechanisms, grouped and split by user and problem to prevent trajectory leakage, and participant-level NONBLIND context. Multiple LLM judges are assessed through a multi-metric protocol covering discrimination (ROC-AUC, PR-AUC), thresholded decision quality (MCC), probabilistic reliability (LogLoss, Brier score, ECE), and inter-judge agreement (Cohen's and Fleiss' k). Human-AI co-creation is further examined through trajectory-level signals, including turn-wise confidence, Success-at-Turn, time-to-success, revision churn, and CodeBLEU. Co-creation success is found to concentrate early, with Success-at-Turn rising to 0.8533 at the first observed turn and stabilizing at 0.8641 by turn 6. Revision behavior, however, remains heterogeneous, suggesting that productive progress can emerge through either incremental refinement or broader restructuring. On the judging side, the best held-out scores reach 0.5937 for ROC-AUC, 0.6904 for PR-AUC, and 0.5000 for MCC test, while inter-judge consistency remains modest overall (mean pairwise Cohen's k = 0.1592, Fleiss' k = 0.0696). Taken together, this work offers an auditable and reproducible evaluation methodology that links reliability-aware LLM judging with trajectory-based analysis of human-AI co-creation, providing a practical evaluation template for future AI-assisted coding and SE.
