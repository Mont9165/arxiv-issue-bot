# JustDiag!: A Diagnostic Justification Engine for Accountable Root Cause Analysis

- arXiv ID: `2606.19407v1`
- Authors: Tingzhu Bi, Xinrui Jiang, Xun Zhang, Pengcheng Su, Congjie He, Jinglin Li, Ping Wang, Meng Ma
- Published: 2026-06-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.19407v1) | [pdf](https://arxiv.org/pdf/2606.19407v1)

## Abstract

Large language models can produce fluent root cause analyses, but fluent final answers alone are insufficient evidence for accountability in high-stakes operations. In real incident response, engineers need to know what evidence supported a diagnosis, which alternatives were considered, where contradictions remained, and whether the system resolved the case or preserved uncertainty. We address this gap with JustDiag, a diagnostic justification engine for RCA that maintains an explicit process state over evidence, findings, competing hypotheses, conflicts, and next checks. We evaluated the system on 66 real-world incidents using a two-layer protocol that separately scores final-answer quality and process quality. Relative to a matched control without diagnostic justification, JustDiag achieved stronger outcome and process scores, while accepting slightly lower terminal completion due to more calibrated non-closure. These results suggest that accountable RCA requires explicit diagnostic justification artifacts and process-aware evaluation, not only fluent final answers.
