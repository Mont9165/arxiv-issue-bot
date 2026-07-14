# VRExplorer: A Model-based Approach for Semi-Automated Testing of Virtual Reality Scenes

- arXiv ID: `2607.10174v1`
- Authors: Zhengyang Zhu, Hong-Ning Dai, Hanyang Guo, Zeqin Liao, Zibin Zheng
- Published: 2026-07-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2607.10174v1) | [pdf](https://arxiv.org/pdf/2607.10174v1)

## Abstract

With the proliferation of Virtual Reality (VR) markets, VR applications are rapidly expanding in scale and complexity, thereby driving an urgent need for assuring VR software quality. Different from traditional mobile applications and computer software, VR testing faces unique challenges due to diverse interactions with virtual objects, complex 3D virtual environments, and intricate sequences to complete tasks. All of these emerging challenges hinder existing VR testing tools from effectively and systematically testing VR applications.
  In this paper, we present VRExplorer, a novel model-based testing tool to effectively interact with diverse virtual objects and explore complex VR scenes. Particularly, we design the Entity, Action, and Task (EAT) framework for modeling diverse VR interactions in a generic way. Built upon the EAT framework, we then present the VRExplorer agent, which can achieve effective scene exploration by incorporating meticulously designed path-finding algorithms into Unity's NavMesh. Moreover, the VRExplorer agent can also systematically execute interaction decisions on top of the Probabilistic Finite State Machine (PFSM).
  Experimental evaluation on 11 representative VR projects shows that VRExplorer consistently outperforms the state-of-the-art (SOTA) approach VRGuide by achieving significantly higher coverage and better efficiency. Specifically, VRExplorer yields up to 122.8% and 52.8% improvements over VRGuide in terms of executable lines of code (ELOC) coverage and method (function) coverage, respectively. Furthermore, ablation results also verify the essential contributions of each designed module. More importantly, our VRExplorer has successfully detected two functional bugs and one non-functional bug from real-world projects.
