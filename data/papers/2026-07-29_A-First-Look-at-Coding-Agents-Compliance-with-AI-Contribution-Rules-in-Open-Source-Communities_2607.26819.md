# A First Look at Coding Agents' Compliance with AI Contribution Rules in Open-Source Communities

- arXiv ID: `2607.26819v1`
- Authors: Wenhao Yang, Runzhi He, Minghui Zhou
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.26819v1) | [pdf](https://arxiv.org/pdf/2607.26819v1)

## Abstract

Open source communities have been flooded with AI-generated contributions. In defense, they have written contribution rules to regulate coding agents' behavior, spanning from a total ban, mandatory disclosure, to verification gates and human sign-offs. Yet, whether coding agents read and follow those rules, and behave in open source repositories, remains unknown. To estimate real-world rule compliance of coding agents, we curate 106 issues from 49 repositories containing AI contribution rules into RepoComplianceBench. We judge the trajectory of each run against the repository's rules, measuring whether the agent refuses to contribute, discloses its assistance truthfully, clears the required verification gates, or escalates critical steps to a human. We also test if extra prompts, rule disclosure, or feedback from the compliance verifier help with the situation. Our experiments on four frontier models show that today's agents almost never proactively retrieve the contribution rules. Agents pick up disclosure and verification with reminder prompts, rule quotes, and verifier feedback; however, they never refuse to contribute in AI-banned repositories under any condition we tested. The status reveals that verification and disclosure issues are solvable with existing mechanisms, yet enforcing bans and human escalations remains an open problem.
