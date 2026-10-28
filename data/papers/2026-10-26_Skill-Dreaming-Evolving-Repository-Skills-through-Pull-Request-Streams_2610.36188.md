# Skill Dreaming: Evolving Repository Skills through Pull Request Streams

- arXiv ID: `2610.36188v1`
- Authors: Xinyuan Song, Hasibul Haque, Jay Somasundaram, Ryan Turner, Bowen Zhu, Liang Zhao
- Published: 2026-10-26
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.36188v1) | [pdf](https://arxiv.org/pdf/2610.36188v1)

## Abstract

Large language model (LLM) agents increasingly rely on reusable skills for complex software engineering tasks, making skill libraries essential for repository development and maintenance. However, repository-specific skills must evolve with changing code structures, implementation conventions, and maintenance requirements. Pull requests (PRs) provide a natural source of such knowledge by recording how repositories evolve through implementation and review. Meanwhile, new PRs must follow repository-specific implementation patterns, modify related components consistently, and ensure that existing tests continue to pass while adding coverage for new functionality. This creates a mutually reinforcing cycle: PRs provide knowledge for updating skills, while these skills improve future PRs, maintain repositories, and support further skill evolution. To enable this co-evolution of PRs, repositories, and skills, we propose Skill Dreaming, a framework that learns from PR streams to guide continuous repository development and maintenance. Given a repository and its PR history, Skill Dreaming builds a repository-specific skill library by extracting executable knowledge from validated PRs and continuously refines the skills as new PR information becomes available. These skills guide coding agents not only in implementing requested features but also in maintaining associated tests, documentation, compatibility, and repository conventions. By integrating PR analysis, skill management, code execution, and continuous integration, Skill Dreaming provides an end-to-end workflow for applying learned skills to repository changes and incorporating subsequent PR outcomes into future skill updates.
