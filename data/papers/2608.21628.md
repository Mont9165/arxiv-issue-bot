# ExploreAI: Agentic Exploration Knowledge Bases for Reproducible Observable-Regression Testing of Black-Box VR and 3D Applications

- arXiv ID: `2608.21628v1`
- Authors: Jiajie Wang, Kebin Peng, Wei Wang, Xiaoyin Wang, Sen He, Xue Qin
- Published: 2026-08-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.RO`
- Links: [abs](http://arxiv.org/abs/2608.21628v1) | [pdf](https://arxiv.org/pdf/2608.21628v1)

## Abstract

Black-box VR and 3D applications are difficult to regression test because observable failures depend on where a tester moves, what objects are visible, and which views are captured. Manual exploratory testing can find such failures, but its evidence is time-consuming to reproduce; systematic sweeps are reproducible, but they lack semantic guidance and spend exploration budget on low-value viewpoints. We observe that an LLM can make the high-level decisions a human tester makes during exploration: interpreting a task, choosing which objects to inspect, grouping related objects, recording what it saw, and deciding when missing evidence should trigger another attempt. Based on this observation, we present ExploreAI, an LLM-driven agentic framework that offloads repeated perception, navigation, multi-view capture execution, and logging to specialized modules while using the LLM for planning, evidence recording, capture-policy decisions, and verification decisions. ExploreAI constructs an Exploration Knowledge Base (EKB): a structured, per-object record of one exploration run. For each object the agent finds, the EKB stores the scan evidence that exposed it, the selected target, the navigation path, the multi-view capture, and the self-verification result. The EKB is a reusable testing artifact that supports reproducible observable-regression checking across versions of a VR or 3D application. Across six indoor and outdoor scenes in Unity, AI2-THOR, and BeamNG, ExploreAI constructs high-completeness EKBs under both complete and target exploration, and an LLM-module ablation shows where semantic planning, capture policy, evidence recording, and self-verification contribute. Reproduction pilots further show that EKB-guided traces help both humans and LLM-based reproducers reproduce exact object-view evidence more effectively than conditions without EKB context.
