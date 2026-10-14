# SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills

- arXiv ID: `2607.09016v1`
- Authors: Xuan Chen, Chengpeng Wang, Lu Yan, Xiangyu Zhang
- Published: 2026-07-10
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09016v1) | [pdf](https://arxiv.org/pdf/2607.09016v1)

## Abstract

Agent skills extend LLM agents with reusable procedures, tools, and domain-specific workflows, but their safety depends on resolving dependencies among interacting instructions. We introduce SkillLogic, a framework for analyzing logical relations in skill files and constructing executable tests from them. Our taxonomy covers eight relation types, including preconditions that gate valid actions, constraints that limit how allowed actions may be performed, and fallbacks that specify recovery behavior after failure. Using SkillLogic, we scan over 5000 public skills and find that 70% contain at least one logical relation. We then construct SLBench, an 86-case executable benchmark from high-confidence, high-impact, and locally testable relations. Evaluating Codex and Claude Code across six LLM backbones shows unsafe rates up to 70%, with violations leading to privacy leaks, unsafe configuration changes, and incomplete cleanup. The human audit attributes failures to both agent capability gaps and low-salience skill text. We further show that SLGuard, a lightweight inference-time scaffold, reduces violations by 63% on targeted cases. Our results establish logical-relation following as a distinct reliability challenge for skill-guided agents.
