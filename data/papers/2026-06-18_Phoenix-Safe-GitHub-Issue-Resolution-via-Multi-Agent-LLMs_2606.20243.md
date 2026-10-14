# Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs

- arXiv ID: `2606.20243v1`
- Authors: Kipngeno Koech, Muhammad Adam, Baimam Boukar Jean Jacques, Joao Barros
- Published: 2026-06-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2606.20243v1) | [pdf](https://arxiv.org/pdf/2606.20243v1)

## Abstract

We present Phoenix, a multi-agent LLM system that resolves GitHub issues from triage through pull-request creation, combining seven layered safety controls with a baseline-aware test evaluation strategy. Phoenix decomposes the work across six specialized agents. Planner, reproducer, coder, tester, failure analyst and Pull Request (PR) agent, all coordinated by a label-based GitHub webhook state machine. Every change is checked against a baseline test run before a pull request is opened. On a 24-instance slice of SWE-bench Lite. run on the production webhook path, Phoenix oracle-resolves 75% of instances with no pass-to-pass regressions on successful runs; this curated slice is not directly comparable to full-split leaderboard results, and we discuss the limits of the comparison. A complementary pilot on 42 real issues across 14 repositories yields 100% correctness preservation (CP; mean 122s on the hard tier). Manual inspection shows that about half of the resulting pull requests are well-targeted fixes. The other half place code at incorrect paths, a planner localization limitation we are addressing with retrieval. We also report the deployment failure modes (WAF filtering, token expiry, permission boundaries, flaky CI) that motivated each safety mechanism.
