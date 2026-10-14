# Microskill Architecture: A Modular Skill-Driven Framework for AI-Native Code Generation

- arXiv ID: `2606.05720v1`
- Authors: Mohammad Zare, Omid Abdolrahmani
- Published: 2026-06-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.05720v1) | [pdf](https://arxiv.org/pdf/2606.05720v1)

## Abstract

Large language models and AI coding agents have reshaped software development, but the path to fully AI-native systems faces structural challenges. Chief among them is managing context windows without losing accuracy or efficiency. When developers inject full project documentation and code into a model's memory, the model loses mid-sequence information, token costs spiral, and architecture drifts. This paper presents MicroSkill Architecture: a modular design paradigm inspired by microservices, applied to knowledge encapsulation instead of service decomposition. Instead of feeding an agent the entire codebase, the architecture partitions knowledge into atomic, sharply scoped skill capsules, and a dynamic router selects only semantically relevant capsules for the task. We formally model context allocation as constrained optimization over semantic relevance subject to a token budget. An empirical case study an enterprise content management system with fifteen complex features shows that MicroSkill cuts token consumption by over 90%, nearly doubles first-try compilation success rates, eliminates architectural violations entirely, and enables autonomous extraction and registration of seven new skill capsules via a self-learning mechanism. These findings suggest MicroSkill Architecture offers a scalable foundation for building AI-native development systems that are more efficient, more reliable, and capable of evolving over time.
