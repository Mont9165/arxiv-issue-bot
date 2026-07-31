# HALO: Heterogeneous Admission through Localized Obligations for Safe Agentic Execution

- arXiv ID: `2607.27636v1`
- Authors: Taewoo Park, Kyeonghyun Yoo, Kiseok Kim, Seunghyun Yoo, Hwangnam Kim
- Published: 2026-07-30
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.RO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.27636v1) | [pdf](https://arxiv.org/pdf/2607.27636v1)

## Abstract

Recent agentic AI systems may return a heterogeneous response containing notices, requests, handoffs, and actions. Conditions can change before external use, so components from the same response need not remain supported together. Rejecting the whole response discards useful components, whereas checking components independently can leave a dependent without its prerequisite. We present Heterogeneous Admission with Localized Obligations (HALO), a runtime protocol that preserves supported components whose declared prerequisites also remain supported, rechecks each exact action before dispatch, and allows blocked actions to be replaced only by fresh candidates. HALO matched all 96 admission expectations and passed all 20 protocol tests. In structured-response replay, it retained 248/248 supported components, including 128/128 unaffected by unrelated changes, while a whole-response policy retained 0/248. Across ten cold-start PX4/Gazebo sessions, HALO blocked every tested stale route, observed no matching stale setpoint, and completed all fresh recoveries.
