# Recovery Gone Too Far: Understanding and Repairing Risky Fallback in LLM Agents

- arXiv ID: `2611.19886v1`
- Authors: Liwen Wang, Jiangrong Wu, Zongjie Li, Zongyi Lyu, Shuai Wang, Shing-Chi Cheung
- Published: 2026-11-15
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.19886v1) | [pdf](https://arxiv.org/pdf/2611.19886v1)

## Abstract

Large Language Model (LLM) agents interact with their environments through tools, reading repositories, running builds, and pushing code. When a tool fails with an ordinary error, such as a rate limit or a timeout, the agent can fall back to a substitute tool and still complete the task. However, the same fallback that completes a task in one environment can cross an action boundary in another. For example, after a push is rejected, a forced push in one repository replaces only the agent's own commits, while in a different repository it also removes another author's commits. We call such a fallback a risky fallback. To understand this phenomenon, we conduct an empirical study on 304 scenarios that span eight domains and cover 55 real CVEs. All four mainstream models we evaluate exhibit risky fallback, with action-boundary violations in up to 96.8% of risky scenarios. We further evaluate three mainstream mitigations and find that none of them is effective against risky fallback. We then present nrepair. At each call to the substitute tool, nrepair scores the agent's context with a monitor whose threshold is calibrated on normal runs alone; when the monitor triggers, it withholds the call once and returns the decision to the agent. nrepair reduces action-boundary violations on all four models, by up to 76.0% (from 67.5% to 16.2%), at a negligible runtime cost. On most models, the normal success rate drops by less than 7%. We also evaluate nrepair on two production agents, Claude Code and Codex, and find that it is equally effective on both.
