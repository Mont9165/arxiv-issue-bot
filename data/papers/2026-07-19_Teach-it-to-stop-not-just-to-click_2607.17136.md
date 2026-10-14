# Teach it to stop, not just to click

- arXiv ID: `2607.17136v1`
- Authors: Barada Sahu, Shivesh Pandey
- Published: 2026-07-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.HC`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.17136v1) | [pdf](https://arxiv.org/pdf/2607.17136v1)

## Abstract

Agentic computer-use RL is reported in single runs, and those numbers mislead. Using verifier-guided repair of a 35B computer-use agent (CUA) across five oracle-graded environments, we show a repaired policy's success rate is dominated by upstream variance: a variance-components decomposition across three cells (crossed data-draw $\times$ seed grid, bootstrap CIs) finds evaluation variance negligible ($σ_{\mathrm{eval}} \approx 0$) and the training-seed effect small everywhere ($\leq 10\%$); instead it splits between the data draw and run-to-run nondeterminism, the data draw's share rising to dominant ($48\%$) on the hardest cell. There the run-to-run distribution is bimodal (Hartigan dip $p=0.07$, $k=10$), so a single run has roughly a 30% chance of the failure mode and mean$\pm$std is the wrong summary. On that footing, two findings hold. First, repairability is two-tier in how constrained the corrective action is: a single fixed token installs reliably (done-detection $0.97\pm0.06$), while open-ended corrections are only partial -- spatial-coordinate clicks (grounding $0.53\pm0.35$) and a generative field-fill ($0.14\pm0.04$). Second, the frame-level repair transfers to task success only when the corrective action is the task's sole remaining blocker (LinkedIn 8/20 vs. base 0/15, Fisher $p=0.006$). We caught two of our own over-claims -- a sample-efficiency curve and a 'grounding cannot be bought' boundary -- only by replicating across seeds; a stress test makes the stakes external: a single-run improvement of the size this field publishes would have the wrong sign roughly one-third of the time in a comparable regime. We release a library (cua_reliability) for routine k-seed reporting. The apparatus is, to our knowledge, the first multimodal segment-aggregated on-policy self-distillation (SA-OPSD) update on a real 35B CUA policy.
