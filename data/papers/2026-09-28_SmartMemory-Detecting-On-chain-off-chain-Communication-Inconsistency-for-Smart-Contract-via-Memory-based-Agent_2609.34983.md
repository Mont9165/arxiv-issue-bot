# SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent

- arXiv ID: `2609.34983v1`
- Authors: Zeqin Liao, Yuhong Nan, Henglong Liang, Zixu Gao, Lianyu Hu, Yuqiang Sun, Zhijie Zhong, Xiaoyu Ma, Zibin Zheng, Yang Liu
- Published: 2026-09-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2609.34983v1) | [pdf](https://arxiv.org/pdf/2609.34983v1)

## Abstract

Smart contracts underpin decentralized finance, where growing demand for on-chain/off-chain communication(OFC) has driven diverse applications such as cross-chain bridges, real-world asset tokenization, and fiat-backed stablecoins. TheOFC-related security incidents in these applications are increasingly frequent, but prior studies address separate vulnerability categories within OFC applications rather than providing a unified view, causing vulnerabilities outside known patterns to be missed.In this paper, we identify OFC inconsistency (OFCI) as a root cause of OFC vulnerabilities, which arises from business-logic flaw and ultimately breaks the equivalence between the on-chain and off-chain asset representations to induce inconsistency.Automatically detecting OFCIs faces two challenges including (1)locating heterogeneous business logic, and (2) transferring existing vulnerability knowledge to identify unseen OFCI instances.
  To this end, we propose SmartMemory, the first framework to leverage a memory-based agent for OFCI detection. To address heterogeneity, SmartMemory maps diverse implementations ofOFC contracts into a canonical business-semantic representation to locate the business logic for OFCI inspection. For knowledge reuse, SmartMemory integrates a memory-based agent to distill vulnerability knowledge from features into patterns and detection rules, enabling knowledge transfer across cases to identify unseenOFCIs. Lastly, SmartMemory performs taint analysis to verify the reachability, type, and impact of each candidate OFCI. We construct the first real-world OFCI dataset comprising 48 DApps with 81 OFCIs for evaluation, on which SmartMemory achieves80.68% precision and 87.65% recall. In addition, through an analysis of 325 real-world OFC applications, SmartMemory detects 36 previously unknown OFCIs, all of which have been confirmed and fixed by corresponding parties.
