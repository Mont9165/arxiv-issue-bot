# Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems

- arXiv ID: `2609.08472v1`
- Authors: Yang Li, Sergey Volkov, Hai Liu, Zongsi Xu, Xiyu Chen, Tuo Zhou, Dian Shao, Hao Sun, Ye Lu
- Published: 2026-09-08
- Primary category: `cs.MA`
- Categories: `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.08472v1) | [pdf](https://arxiv.org/pdf/2609.08472v1)

## Abstract

Agentic systems persist model-visible memory while mutating workspaces, while a runtime, registry, or approval service may hold authority state outside both. Identical final files can then require opposite safe actions. We call this the cross-substrate authority gap: decision- relevant authorization information resides outside the planner-visible workspace or memory state. Across two controlled mini-benchmark families, three experiments compare planner-observation augmentation with an execution-time authority check using real Git lineage, durably recorded agent execution attempts, deterministic oracles, and two model routes. Experiment 1 is a 128-cell controlled evidence ablation: authority-blind candidate evidence obtains 0/32 final semantic success, while raw receipts and a typed relation both obtain 32/32. The missing authority fact accounts for the gain; typed packaging provides no observed planning-accuracy gain over equal raw information. Experiment 2 uses 96 planning calls: workspace-visible evidence yields 12/16 unsafe publication decisions, and planning with the typed relation remains unreliable (15/32 first actions correct; 11/32 invalid or absent). Experiment 3 replays the same 32 fixed model-generated first-action intents with zero additional model calls; a deterministic execution guard prevents all six unsafe intents from becoming effects and permits all 12 valid authorized publish intents. These results position authority enforcement at the mutation boundary as the operational endpoint of memory governance.
