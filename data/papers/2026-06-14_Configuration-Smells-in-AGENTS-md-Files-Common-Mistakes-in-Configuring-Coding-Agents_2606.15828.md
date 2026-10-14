# Configuration Smells in AGENTS.md Files: Common Mistakes in Configuring Coding Agents

- arXiv ID: `2606.15828v1`
- Authors: Helio Victor F. dos Santos, Vitor Costa, Joao Eduardo Montandon, Luciana Lourdes Silva, Marco Tulio Valente
- Published: 2026-06-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.15828v1) | [pdf](https://arxiv.org/pdf/2606.15828v1)

## Abstract

Coding agents are increasingly used to automate software engineering tasks. To guide their behavior, these agents commonly rely on configuration files, typically named AGENTS.md or CLAUDE.md, which provide instructions about architecture, workflows, coding conventions, and testing practices. Despite their growing importance, little is known about common problems affecting the definition and maintenance of these files. In this paper, we present the first catalog of smells for coding-agent configuration files. To identify such smells, we first conducted a grey literature review and a repository mining analysis. As a result, we identified six configuration smells and proposed automated heuristics to detect them. To evaluate the prevalence of the proposed smells, we analyzed 100 popular open-source repositories containing either an AGENTS.md or a CLAUDE.md file. Our results show that configuration smells are widespread. Lint Leakage was the most common smell, affecting 62% of the files, followed by Context Bloat (42%) and Skill Leakage (35%). We further show that several smells frequently co-occur, particularly Context Bloat, Skill Leakage, and Conflicting Instructions.
