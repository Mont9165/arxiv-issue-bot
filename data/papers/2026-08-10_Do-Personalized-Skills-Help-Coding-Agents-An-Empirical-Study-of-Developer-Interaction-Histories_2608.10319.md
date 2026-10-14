# Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Histories

- arXiv ID: `2608.10319v1`
- Authors: Shuyan Huang, Kai Du, Andrew Lan
- Published: 2026-08-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.10319v1) | [pdf](https://arxiv.org/pdf/2608.10319v1)

## Abstract

Large language model (LLM)-powered agents have rapidly evolved from code-completion tools into solvers of complex software engineering tasks. As developers collaborate with coding agents over time, their preferences emerge through repeated interactions and can be used to adapt agent behavior to better meet individual developers' needs. Capturing and reusing these preferences may reduce repeated corrections and improve developer-agent collaboration. Agent skills provide a lightweight mechanism for transferring experience without modifying model parameters. However, existing work primarily focuses on task-specific skills, and it remains unclear whether developer-specific skills distilled from interaction histories can generalize to future tasks. We propose a framework for extracting reusable developer preferences from interaction traces. It first generates personalized skills through rule-based bootstrapping and evidence-grounded refinement, and then evaluates them using a reproducible replay framework with an interactive, trajectory-conditioned LLM-based human developer simulator. We conduct an experiment on 206 real-world developer-agent sessions from 13 developers and compare personalized skills against no-skill, generic-skill, and other-user-skill baselines. Personalized skills provide small and inconsistent improvements over the no-skill baseline, whereas generic skills pooled across developers achieve the largest and most consistent gains. Further analysis suggests that personalized skills become more effective when developer preferences appear frequently, particularly when their histories contain multiple examples relevant to future tasks. These findings provide empirical insights into when developer-specific personalization is effective and demonstrate that broadly transferable procedural knowledge can be more robust than developer-specific preference signals.
