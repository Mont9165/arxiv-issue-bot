# Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution

- arXiv ID: `2606.25514v1`
- Authors: Yang Chen, Aliya Ahmad, Yiheng Zhou, Reyhaneh Jabbarvand
- Published: 2026-06-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.25514v1) | [pdf](https://arxiv.org/pdf/2606.25514v1)

## Abstract

Resolving issues with ambiguous and incomplete descriptions, particularly concerning complex bugs, requires a sophisticated, long-horizon workflow. Agents must navigate codebases to locate the root cause, reproduce the failure, implement a fix, and validate the resulting patch. Inefficient context management, thereby, can lead to rapid context degradation and context poisoning, preventing successful resolution. We propose icat-agent, a decentralized, multi-agent scaffolding that replaces shared context with synchronous, event-based message passing. Utilizing a rubric-based issue quality check, icat-agent strategically pivots its workflow: it initiates parallel patching and validation for well-defined issues, while deploying preliminary exploration for low-quality ones. A comprehensive evaluation of icat-agent on SWE-bench Verified and SWE-bench Pro demonstrates that it consistently outperforms prominent baselines across all difficulty levels, including SWE-agent, mini-SWE-agent, and Claude Code, while using the same underlying models, improving by 3.6-8.4% on SWE-bench Verified and 6.3-18.5% on SWE-bench Pro. icat-agent is also computationally efficient, reducing the average cost by $1.18 per instance compared with the multi-agent Claude Code baseline. Our findings reveal that a robust scaffold such as icat-agent unlocks substantial latent capability within a fixed model, with the same backbone resolving markedly more issues under icat-agent than under existing scaffolds. icat-agent +GPT-5.4-xhigh resolves 67.4% of SWE-bench Pro problems, outperforming the current best result on SWE-bench Pro (59.10%, mini-SWE-agent+GPT-5.4-xhigh) by 8.3 percentage points.
