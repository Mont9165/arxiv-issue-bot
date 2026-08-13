# The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark

- arXiv ID: `2608.11469v1`
- Authors: Jeremy Spence, Nicholas Assaderaghi, Jinhao Zhu, Nikil Ravi, Raluca Ada Popa, Guannan Wei, Yangruibo Ding, Zhuo Zhang
- Published: 2026-08-11
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.11469v1) | [pdf](https://arxiv.org/pdf/2608.11469v1)

## Abstract

AI agents are rapidly improving in cybersecurity capabilities when the source code is available for analysis, yet much of the software most consequential to cybersecurity, including malware, firmware, and proprietary applications, is available only as binaries. Analyzing such software requires reverse engineering(RE): recovering program semantics before the analysis can be meaningfully performed. However, evaluating agentic RE poses a fundamental challenge: benchmark instances must be unseen as source code in the LLMs' training data to prevent models from taking shortcuts by recognizing them rather than really analyzing them, while also matching the scale and anti-analysis protections of real software. Unfortunately, however, existing benchmarks do not jointly satisfy these requirements. To this end, we introduce SRE-Bench, the first realistic, contamination-free RE benchmark. Built entirely from scratch by RE experts with over 5,000 hours, SRE-Bench comprises 19 private, real-world-scale programs averaging 16.9K lines of code. We further developed 44 in-house anti-analysis primitives, yielding 262 binary instances and 1572 deterministically graded tasks. Our evaluation across five frontier LLMs (GPT-5.6-sol,Claude-Opus-5,GPT-5.5,Grok-4.5, and GLM-5.2) shows that RE remains largely unsolved: the strongest model, GPT-5.6-sol, scores 61.4% per instance, and fully solves only 31.5% of the instances. Our analysis further reveals that agents behave differently from human engineers, where agents are relatively insensitive to compiler optimization and static linking. Controlled ablations also confirm that both contamination control and realistic scale are essential. These results indicate that strong source-code security capabilities do not yet transfer to binary analysis, highlighting RE as an important frontier for agentic cybersecurity and SRE-Bench as a rigorous testbed to measure progress.
