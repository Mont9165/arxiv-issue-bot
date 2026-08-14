# Requirements-Augmented Generation for Trustworthy Acceptance Testing of LLM-Based Software

- arXiv ID: `2608.12970v1`
- Authors: Fanyu Wang, Chetan Arora, Zhenping Xie, Yonghui Liu, Kla Tantithamthavorn, Aldeida Aleti, Siwei Jiang
- Published: 2026-08-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.12970v1) | [pdf](https://arxiv.org/pdf/2608.12970v1)

## Abstract

LLM-based software (LBS) integrates large language models as core components to deliver flexible, personalised responses. Unlike traditional software with deterministic outputs, LBSs exhibit context-dependent, stochastic behaviour that renders classical acceptance testing and test oracles insufficient: the same query may require fundamentally different responses depending on user personas and software context. This gap creates an urgent need for automated acceptance testing frameworks that autonomously interpret user instructions, while reliably inferring user intentions in a changing environment. In this paper, we present an automated acceptance testing framework for LBS with calibrated verdict reliability via two technical contributions. First, we introduce Requirements-Augmented Generation (REAG), which interprets user intentions by retrieving relevant software requirements, domain knowledge, and personas via adaptive RAG and self-reasoning to generate context-aware test oracles. Second, recognising that oracle generation may retrieve irrelevant constraints, misinterpret intent, or hallucinate requirements, we introduce a confidence-calibrated cascade judgment. This method quantifies verdict reliability via simulated expert agreement -- accepting high-confidence verdicts, escalating ambiguous cases, or abstaining when uncertain -- with empirical reliability guarantees backed by conformal risk control. An industrial case study on a production nutrition advisory application demonstrates that REAG achieves a 3.91/5 oracle quality score, reaching qualified or marginal oracle quality in 82% of cases. The confidence-calibrated cascade achieves 98.8% accuracy, improves oracle quality from 3.91 to 4.30 by filtering unqualified outputs, and delivers a 31.7% cost-efficiency improvement over single-judge baselines, validating industrial viability
