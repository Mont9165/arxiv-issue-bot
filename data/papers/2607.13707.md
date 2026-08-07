# The Test Oracle Problem in Synthetic LLM-as-Judge Corpora: Disappearance, Distortion and a Validation Protocol

- arXiv ID: `2607.13707v1`
- Authors: Serkan Ballı
- Published: 2026-07-15
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.13707v1) | [pdf](https://arxiv.org/pdf/2607.13707v1)

## Abstract

Studies of bias in LLM-as-judge systems typically build synthetic corpora by prompting an LLM to generate a hallucinated answer to pair with a factual one, then presenting both to a judge. We report a case in which this generation step silently failed, and use it to argue that the failure mode is structural rather than incidental. In a multilingual (Turkish/English) faithfulness-judgment corpus, a decoding-budget parameter shared between judging and generation calls truncated one producer's hallucinated answers to a few words. The resulting items produced a large, statistically robust effect: a 32-point cross-lingual collapse in one judge's selection accuracy, replicated from N=50 to N=500, explained by a three-layer mechanistic account, and confirmed by a controlled producer-swap experiment, none of which was real. The effect vanished to ceiling once the shared parameter was corrected, and only manual reading of the raw generations, not any aggregate statistical check, exposed the fault. A second measured bias (Markdown-formatting preference) was not fabricated but distorted by the same fault, its magnitude and in one case its sign shifting with stimulus length, a mode aggregate metrics cannot distinguish from the first. We frame the underlying vulnerability using the test oracle problem: corpora whose negative examples are LLM-generated carry no mechanical way to verify item integrity, while corpora built by deterministic perturbation of a gold answer carry an item-level oracle for free. A positive control supports this claim directly: an analogous fault injected into a minimal perturbation-based corpus is caught with 100% accuracy by a zero-cost, zero-human gold-to-negative string comparison. We close with a validation protocol, derived from our own case, for analysts working in the oracle-less regime that we argue describes most contemporary multilingual LLM-as-judge corpora.
