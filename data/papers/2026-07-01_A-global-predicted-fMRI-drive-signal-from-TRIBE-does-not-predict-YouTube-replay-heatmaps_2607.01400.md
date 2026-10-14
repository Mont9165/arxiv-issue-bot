# A global predicted-fMRI drive signal from TRIBE does not predict YouTube replay heatmaps

- arXiv ID: `2607.01400v1`
- Authors: Barada Sahu, Shivesh Pandey
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`, `q-bio.NC`
- Links: [abs](http://arxiv.org/abs/2607.01400v1) | [pdf](https://arxiv.org/pdf/2607.01400v1)

## Abstract

Deep multimodal brain-encoding models now predict fMRI responses to naturalistic video with high accuracy. Whether their predicted neural signals also forecast behavioral engagement is unknown. We run TRIBE, the winning model of the 2025 Algonauts brain-encoding challenge (Llama-3.2 + V-JEPA2 + Wav2Vec-BERT), on 48 YouTube videos and reduce its predicted cortical response to a per-second engagement curve, the global field power. Correlated against each video's "most replayed" heatmap, a passively-collected proxy for which moments viewers return to, the curve shows no evidence of predicting re-watch behavior. The pooled position-controlled partial correlation is +0.058 (95% CI [-0.04, 0.15]; one-sample t(47)=1.21, p=0.23), indistinguishable from zero and not significantly above simple loudness and motion baselines (loudness +0.04, paired p=0.74). The raw correlation is also near zero; the moderate values reported for music videos reflect a genre-specific intro/onset-replay artifact rather than content prediction, and do not generalize. The null holds across six cortical-network readouts and under an autocorrelation-preserving permutation test. We release the code, the video-ID manifest, and an acquisition method that works despite YouTube's SABR-only streaming.
