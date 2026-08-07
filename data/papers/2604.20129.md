# A Delta-Aware Orchestration Framework for Scalable Multi-Agent Edge Computing

- arXiv ID: `2604.20129v1`
- Authors: Samaresh Kumar Singh, Joyjit Roy
- Published: 2026-04-22
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DC`, `cs.PF`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.20129v1) | [pdf](https://arxiv.org/pdf/2604.20129v1)

## Abstract

The Synergistic Collapse occurs when scaling beyond 100 agents causes superlinear performance degradation that individual optimizations cannot prevent. We observe this collapse with 150 cameras in Smart City deployment using MADDPG, where Deadline Satisfaction drops from 78% to 34%, producing approximately $180,000 in annual cost overruns. Prior work has addressed each contributing factor in isolation: exponential action-space growth, computational redundancy among spatially adjacent agents, and task-agnostic hardware scheduling. None has examined how these three factors interact and amplify each other. We present DAOEF (Delta-Aware Orchestration for Edge Federations), a framework that addresses all three simultaneously through: (1) Differential Neural Caching, which stores intermediate layer activations and computes only the input deltas, achieving 2.1x higher hit ratios (72% vs. 35%) than output-level caching while staying within 2% accuracy loss through empirically calibrated similarity thresholds; (2) Criticality-Based Action Space Pruning, which organizes agents into priority tiers and reduces coordination complexity from O(n2) to O(n log n) with less than 6% optimality loss; and (3) Learned Hardware Affinity Matching, which assigns tasks to their optimal accelerator (GPU, CPU, NPU, or FPGA) to prevent compounding mismatch penalties. Controlled factor-isolation experiments confirm that each mechanism is necessary but insufficient on its own: removing any single mechanism increases latency by more than 40%, validating that the gains are interdependent rather than additive. Across four datasets (100-250 agents) and a 20-device physical testbed, DAOEF achieves a 1.45x multiplicative gain over applying the three mechanisms independently. A 200-agent cloud deployment yields 62% latency reduction (280 ms vs. 735 ms), sub-linear latency growth up to 250 agents.
