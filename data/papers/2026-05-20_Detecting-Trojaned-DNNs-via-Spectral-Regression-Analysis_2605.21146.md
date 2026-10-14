# Detecting Trojaned DNNs via Spectral Regression Analysis

- arXiv ID: `2605.21146v1`
- Authors: Samuele Pasini, Jinhan Kim, Paolo Tonella
- Published: 2026-05-20
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21146v1) | [pdf](https://arxiv.org/pdf/2605.21146v1)

## Abstract

Modern DNNs are repeatedly fine-tuned to incorporate new data and functionality. This evolutionary workflow introduces a security risk when updated data cannot be fully trusted, as adversaries may implant Trojans during fine-tuning. We present MIST, a Trojan detection approach that analyzes how a model's internal representations change during fine-tuning. Rather than attempting to reconstruct trigger conditions, MIST characterizes benign model evolution using pre-activation spectra and flags updates whose spectral deviations are inconsistent with this reference. This framing treats Trojan detection as a regression problem over model updates. An empirical evaluation across four datasets and eight Trojan attacks shows that spectral distances reliably distinguish Trojaned updates from clean fine-tuning. MIST outperforms state-of-the-art detection accuracy after a single update, without requiring any knowledge about the poisoned data or the trigger, and remains effective under multi-step benign evolution, with graceful and bounded degradation. These results indicate that spectral evolution provides a stable and assumption-light signal for detecting malicious model updates.
