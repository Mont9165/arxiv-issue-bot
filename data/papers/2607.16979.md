# When Post-Anchor Metrics Fail: Stabilization Regimes in AI-Evidence Open-Source Projects

- arXiv ID: `2607.16979v1`
- Authors: Hudson Craig, Benjamin Barlog, Chenggang Wang, Longwei Wang, Zedong Peng
- Published: 2026-07-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.16979v1) | [pdf](https://arxiv.org/pdf/2607.16979v1)

## Abstract

Repository mining studies increasingly analyze AI-evidence projects, yet it remains unclear how to measure whether architectural changes create deferred stabilization obligations. A natural metric, post-anchor stabilization density, counts tests, CI gates, documentation, and fixes appearing after a durable boundary is introduced. We show that this metric fails. In a diff-level study of 338 high-visibility 2026 GitHub repositories, anchors are common (321 of 338 contain real changed-file anchor evidence), but a controlled 308-event contiguous-window experiment finds no post-anchor uplift: broad and strict stabilization signals both yield median post/pre density ratios near 1.0, and non-anchor controls are equally dense. We introduce stabilization regimes, six recurring patterns that explain why the density metric fails, and use human validation to calibrate them. Two independent coders label 100 stratified candidate-anchor events from blinded packets (kappa = 0.50 on debt attribution). The validation exposes a two-layer trap: many candidate anchors are not durable boundaries (45 of 100), and even among valid anchors in this calibration sample the no-uplift result holds: only 3 of 100 events survive as attributable delayed obligations; the remaining 97 are explained by classifier error, anchor-local hardening, background maintenance, or pre-anchor hardening. Post-anchor density conflates pervasive maintenance with genuine debt; controlled designs with regime-aware attribution are necessary before repository mining can reliably identify stabilization obligations.
