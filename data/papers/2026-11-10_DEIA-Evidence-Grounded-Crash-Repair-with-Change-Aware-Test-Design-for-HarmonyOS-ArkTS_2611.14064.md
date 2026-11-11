# DEIA: Evidence-Grounded Crash Repair with Change-Aware Test Design for HarmonyOS ArkTS

- arXiv ID: `2611.14064v1`
- Authors: Xuhui Lu, Zhihao Liu, Xiaoke Fang, Yuhuan Fan, Yanzhe Tang, Xiaohui Wan, Xiaoyu Wu, Zheng Zheng
- Published: 2026-11-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.14064v1) | [pdf](https://arxiv.org/pdf/2611.14064v1)

## Abstract

Mobile crash repair requires more than identifying a source edit. Developers must establish how the edit relates to the reported failure and whether the modified application can be built, launched, and exercised without disrupting valid behavior. In HarmonyOS applications, this assessment also depends on platform-specific packaging and runtime execution.
  To address this need, we present DEIA, an evidence-grounded workflow for HarmonyOS crash repair. DEIA constructs a bounded source-evidence package, uses a large language model to propose content-anchored edits, and relies on a deterministic writer to materialize and check the patch. It derives fail-to-pass (F2P) obligations from the reported fault and pass-to-pass (P2P) obligations from the potential impact of the patch. A stage-level ledger links the patch, test obligations, runtime observations, and candidate-generation cost.
  We evaluate DEIA on 30 repair tasks from 24 HarmonyOS applications and compare it with an OpenHands-based workflow on 29 matched tasks. DEIA's first-added-line location exactly matches the curated reference in 25/29 tasks (86.2%), compared with 19/29 (65.5%) for OpenHands, a difference of 20.7 percentage points. DEIA also uses 81.5% fewer tokens, makes 60.8% fewer model calls, and takes 34.9% less candidate-generation time on average. Only two of the 58 behavior-specific P2P obligations were executed, both for one repair pattern; comprehensive behavior preservation therefore remains unestablished.
