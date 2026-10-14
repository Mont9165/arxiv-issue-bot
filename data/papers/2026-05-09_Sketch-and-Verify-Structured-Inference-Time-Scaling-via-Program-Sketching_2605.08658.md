# Sketch-and-Verify: Structured Inference-Time Scaling via Program Sketching

- arXiv ID: `2605.08658v1`
- Authors: Shan Jiang, Zijian Yi, Chenguang Zhu
- Published: 2026-05-09
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.08658v1) | [pdf](https://arxiv.org/pdf/2605.08658v1)

## Abstract

SKETCHVERIFY is a within-tier cost-performance policy, not a universal accuracy improvement. The operational question: a practitioner stuck with a small, cheap code model (here, Gemini 3.1 Flash Lite) for latency, deployment, or budget reasons -- how should they spend a small amount of extra test-time compute? SKETCHVERIFY factorizes the search space: the LLM enumerates K distinct algorithmic strategies, writes a program sketch for each (a partial program with ?? holes), and fills each sketch M times, producing K x M structurally diverse candidates that are verified by execution and selected by fingerprint clustering. Each extra sketch is guaranteed to explore a different algorithm; each extra flat sample likely duplicates an existing one. Our central evidence is a cost-quality Pareto plot on HumanEval+ across three Gemini tiers (Lite, Flash, Pro), and a reanalysis of the 19 problems where Lite greedy fails. Two findings: (1) Within-tier, sketching dominates flat sampling at matched candidate count. On the hard subset, Lite Sketch K=2, M=5 recovers 11/19 (58%) vs. flat N=10 at 5/19 (26%, +32pp); Lite Sketch K=10, M=10 recovers 15/19 (79%) vs. flat N=100 at 10/19 (53%, +26pp). Flat cannot close the gap even at ~3x the budget: flat N=50 still loses to Sketch K=2, M=5 by +11pp. (2) Cross-tier, sketching does not replace upgrading. Pro greedy (89%) dominates Lite Sketch K=10, M=10 (79%) on both pass@1 and dollar cost. Practitioner rule: if a stronger tier is available, use greedy on it; otherwise sketching is the cost-effective way to spend extra compute. We characterize the K-vs-M trade-off via a Flash Lite scaling sweep, report HumanEval+ saturation on Flash and Pro, and show the method composes cleanly with execution-based selection from the concurrent Semantic Voting line of work.
