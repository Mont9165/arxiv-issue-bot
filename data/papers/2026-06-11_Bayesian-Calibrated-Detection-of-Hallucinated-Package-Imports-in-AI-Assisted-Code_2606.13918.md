# Bayesian-Calibrated Detection of Hallucinated Package Imports in AI-Assisted Code

- arXiv ID: `2606.13918v1`
- Authors: Lom M. Hillah, Jean-Marc Richard, Ryan Hasnaoui
- Published: 2026-06-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2606.13918v1) | [pdf](https://arxiv.org/pdf/2606.13918v1)

## Abstract

We present a Bayesian calibration layer for slopsquat detectors -- those that flag hallucinated package imports in code produced by large language models (LLMs). Where existing pipelines emit binary decisions (flag / do-not-flag), our layer emits a Beta-posterior probability per detection, derived from a 3-category epistemic taxonomy that explicitly classifies each prior as empirically calibrated, constructively argued, or engineering-judgement-traced. Beyond the primary 200/404 registry channel, the calibrated layer exploits PyPI metadata signals -- package age, release count, author descriptor, summary -- to surface registered-but-suspicious packages that a binary registry detector misses, which is the realistic post-LLM-emission attacker regime. The resulting risk-aware primitive is directly consumable by downstream CI gates and supports principled threshold decisions across detection rules. We evaluate the calibration on a merged corpus of 1,734 Python snippets -- a stratified 189-prompt BigCodeBench slice plus a 100-prompt niche-library stress-test set, generated across a six-model panel spanning four cloud models (Claude-Sonnet-4.6, Mistral-Large, DeepSeek-v4-pro, DeepSeek-R1) and two local open-weight code models (Mistral Codestral, Meta CodeLlama). Against a re-implemented binary baseline inspired by Mahmud et al. -- which shares its registry oracle with our ground truth and therefore serves as a degenerate upper bound rather than a genuine competitor -- the calibrated layer reproduces the strict-registry detections and introduces well-calibrated additional flags on the metadata channel. We assess detector asymmetry with a McNemar paired test and calibration with both a flagged-subset Expected Calibration Error and a strictly proper full-corpus Brier score.
