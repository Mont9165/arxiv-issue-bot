# Rethinking Access Control for AI Agents: Recent Advances and Open Challenges

- arXiv ID: `2611.06764v1`
- Authors: Chijin Zhou, Quan Zhang
- Published: 2026-11-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.06764v1) | [pdf](https://arxiv.org/pdf/2611.06764v1)

## Abstract

Large language model agents access data, invoke tools, and act on users' behalf. Keeping these actions within authorized bounds is challenging because agents choose their own execution paths while permissions and operating conditions may change. This paper surveys recent advances in agent access control across four areas: policy specification and derivation, identity and delegation, action and resource enforcement, and information flow control. We compare their control objects, enforcement boundaries, and assumptions to examine what individual mechanisms achieve and how they can work together. Building on this analysis, we rethink four aspects of authorization: plan selection shapes permission requirements; contextual information can inform decisions without itself granting authority; restrictions must retain their meaning across system interfaces; and authorization must be reassessed as workflows evolve. These insights motivate open challenges and future directions, together with concrete research questions and evaluation criteria. In particular, evaluation should examine both observed agent behavior and the unauthorized effects that remain enabled. Our analysis connects existing mechanisms to the requirements for preserving authorization throughout an agent workflow.
