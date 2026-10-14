# EvoPoC: Automated Exploit Synthesis for DeFi Smart Contracts via Hierarchical Knowledge Graphs

- arXiv ID: `2605.02868v1`
- Authors: Ruichao Liang, Jing Chen, Xianglong Li, Huangpeng Gu, Yebo Feng, Yue Xue, Cong Wu, Yang Liu
- Published: 2026-05-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.02868v1) | [pdf](https://arxiv.org/pdf/2605.02868v1)

## Abstract

Smart contract vulnerabilities in Decentralized Finance caused over billions of dollars losses every year, yet the security community faces a critical bottleneck: identifying a vulnerability is not the same as proving it is exploitable. Manual PoC construction is prohibitively labor-intensive, leaving most disclosed vulnerabilities unverified and protocols exposed long before mitigation is applied. In this paper, we propose \sys, a knowledge-driven agentic system for end-to-end contract vulnerability detection and exploit synthesis. Our core insight is that exploit synthesis is not a code generation task but a \emph{structured reasoning problem} that requires grounded knowledge of protocol semantics, failure root cause, and exploit primitives. \sys organizes this knowledge into a \emph{Hierarchical Knowledge Graph} (HKG) that serves as structured memory for LLM-guided multi-hop reasoning. To validate exploit feasibility beyond code synthesis, \sys employs a two-stage validation framework that checks exploit-path reachability via SMT solving and profit realizability via asset-level state simulation, ensuring generated PoCs satisfy both logical and economic viability constraints. Evaluated on 88 real-world DeFi attacks and 72 audited projects (2,573 contracts), \sys achieves 98\% recall and 0.9 F1-score in detection, and a 96.6\% exploit success rate (ESR), reproducing 85 historical exploits and recovering over \$116.2M revenue. \sys outperforms SOTA fuzzers (\textsc{Verite}, \textsc{ItyFuzz}) by up to $5\times$ in ESR and $300\times$ in recoverable value, and the LLM-based exploit generator \textsc{A1} by $2\times$ and $8.5\times$ respectively. In bug bounty evaluation, \sys identified 16 confirmed 0-day vulnerabilities, helping secure over \$70.6M and earning \$2,900 in bounties.
