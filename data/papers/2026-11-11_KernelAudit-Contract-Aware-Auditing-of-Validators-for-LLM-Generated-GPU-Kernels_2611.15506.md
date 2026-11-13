# KernelAudit: Contract-Aware Auditing of Validators for LLM-Generated GPU Kernels

- arXiv ID: `2611.15506v1`
- Authors: Ziyuan Li, Zihe Song, Xiaofang Qi, Wei Yang, Tao Xie
- Published: 2026-11-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.15506v1) | [pdf](https://arxiv.org/pdf/2611.15506v1)

## Abstract

The effectiveness of generating GPU kernels driven by a large language model (LLM) is highly dependent on the quality of the used validator (used to accept or reject a generated kernel candidate against the contracts of the given kernel-generation task), whose results inform reward assignment, candidate selection, and speedup claims during kernel generation. However, an existing validator suffers from various limitations, e.g., wrongly accepting a candidate due to missing its forbidden library use or wrongly rejecting a candidate due to determining its permitted library use as forbidden (constraints on library uses are stated in the task contracts).
  To assess the quality of a validator against the given task contracts, we propose an independent-audit approach for the validator by (1) construction of audit oracle: labeling a candidate as PASS or FAIL based on three separate dimensions in our proposed contract model (i.e., semantic correctness, implementation integrity, and measurement integrity) and (2) auditing of the validator against the audit oracle: comparing the labels of the candidate against the validation results produced by the validator. For semantic correctness, reference-calibrated stress tests check output correctness on valid inputs for a candidate. For implementation integrity, reference and candidate execution traces are used to determine specific library uses. For measurement integrity, timing checks assess whether the reported runtime reflects the full time needed to complete the candidate's computation. We apply our approach to assess the quality of six validators and 716 candidates from seven corpora, including constructed controls. The evaluation results show that our approach helps assess the existing six validators to have nontrivial false-reject rates. There is high-degree agreement between the candidate labels produced by our audit oracle and human judgments.
