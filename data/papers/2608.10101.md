# Exploring Semantic Stability Across Reviews in the Linux Kernel

- arXiv ID: `2608.10101v1`
- Authors: Lucas Ciziks, Paulo Meirelles, Marco Aurélio Gerosa
- Published: 2026-08-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2608.10101v1) | [pdf](https://arxiv.org/pdf/2608.10101v1)

## Abstract

Code review is credited with substantially changing a patch's code between its first submission and the version that eventually lands. However, prior work typically studied only the final merged patch without comparing it to the first submission. We present a function-level measurement that tracks 10,117 trajectories (each function followed across the numbered revisions of one patch series) through the patch history of the Linux IIO subsystem, comparing similarity scores against unrelated function pairs as a baseline. A naive reading yields near-total similarity, but this is largely an artifact of composition: 75.3% of tracked trajectories are never textually modified between versions, contributing a trivial 100% similarity that inflates the headline. Restricting to the trajectories with a real edit, semantic purpose is still largely preserved (mean similarity 0.990 vs. a 0.909 baseline), but drift appears to concentrate in the first review round mainly because later rounds contain more functions that nobody touched, not because edits become more conservative over time. After controlling for it, a statistically detectable but small residual effect remains. This points to an open question: whether near-ceiling similarity reflects preserved purpose or a measurement tool that cannot detect the significance of small, localized edits. We present this work as a first look and outline next steps.
