# Panache: One-Pass Motif Discovery at Every Window Length

- arXiv ID: `2607.17481v1`
- Authors: Tej Sanibh Ranade
- Published: 2026-07-20
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.17481v1) | [pdf](https://arxiv.org/pdf/2607.17481v1)

## Abstract

Motif discovery, the search for recurring patterns within a time series, is a core primitive of exploratory data analysis. A pattern, however, is defined by its duration, which analysts rarely know in advance. To resolve this unknown duration, an interval of window lengths is defined, and the accepted method is to try every length in that interval. Existing pan matrix profile (PMP) methods compute one z-normalized matrix profile per length, so $L$ lengths cost $L$ quadratic self-joins over the same series. We introduce Panache, to our knowledge the first one-pass streaming algorithm for z-normalized PMP motif discovery. It replaces the repeated self-joins with a single scan whose runtime is near-linear in the series length. The key observation is that mean-centering a subsequence changes only its DC Fourier coefficient, so the non-DC spectrum of every z-normalized subsequence can be maintained online by sliding-DFT recurrences and running statistics. This spectral state is the key under which similar subsequences collide in an occupancy-controlled hash directory and, through Parseval's theorem, yields a lower bound that rejects most colliding pairs before any exact computation. Panache computes every data-dependent parameter itself, leaving only a resource budget to tune. At the default budget, it recovers all top-20 pan-motifs against exact fixed-exclusion ground truth on 17 UCR configurations, and is faster than every CPU and GPU baseline benchmarked in this paper. On Wafer at five million samples over 51 lengths, Panache completes one pass in 2.9 minutes and emits the exact motifs in 6.0 minutes, against 7.95 hours for the fastest exact CPU baseline and 38.3 minutes for SCAMP on an H100 GPU.
