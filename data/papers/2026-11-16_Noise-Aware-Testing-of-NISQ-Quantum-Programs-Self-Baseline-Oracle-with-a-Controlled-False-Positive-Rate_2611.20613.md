# Noise-Aware Testing of NISQ Quantum Programs: Self-Baseline Oracle with a Controlled False-Positive Rate

- arXiv ID: `2611.20613v1`
- Authors: Mir Mohammad Yousuf, Shabir Ahmad Sofi
- Published: 2026-11-16
- Primary category: `quant-ph`
- Categories: `quant-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.20613v1) | [pdf](https://arxiv.org/pdf/2611.20613v1)

## Abstract

Testing quantum programs on Noisy Intermediate-Scale Quantum (NISQ) devices faces a test-oracle problem: hardware noise and finite-shot sampling make the runs of a correct program vary as much as those of a faulty one, so oracles with a fixed acceptance threshold produce false positives that depend on the program and the backend. We present a noise-aware testing framework built on self-baseline calibration: each run of the program under test is compared with repeated executions of a trusted reference program on the same backend, and the acceptance threshold is the $(1-α)$ quantile of the finite-shot null distribution of the Jensen-Shannon divergence, so the oracle's false-positive rate is a level set in advance. A noncentral chi-square model predicts detection power, a homogeneity test and a two-run sentinel detect drift, a mutation engine labels every mutant exactly within a three-class noise-aware taxonomy, and zero-noise extrapolation attributes rejections to faults or noise. In simulation on nine core benchmarks, 32 QASMBench programs, ten real bugs, seven noise regimes and three device snapshots, the oracle's false-positive rate is 0.0011 at $α= 10^{-3}$ over 9,000 correct runs, against 36-74% for fixed thresholds, 8.9% for a QOIN-style filter and 10.8% for a globally calibrated threshold, while attaining the highest F1 on non-equivalent faults (0.941). On an IBM Heron device, using about 14 minutes of QPU time, it rejected none of 82 correct runs and detected 120 of 121 faults and semantic mutants, and a two-run sentinel reduced drift-induced false positives from 27.4% to 1.8%.
