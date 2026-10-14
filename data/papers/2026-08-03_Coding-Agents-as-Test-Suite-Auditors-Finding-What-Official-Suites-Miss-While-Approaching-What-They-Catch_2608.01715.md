# Coding Agents as Test-Suite Auditors: Finding What Official Suites Miss While Approaching What They Catch

- arXiv ID: `2608.01715v1`
- Authors: Shuyang Xie, Shuxiao Xie, Feng Zhu, Yanli Ji, Wangmeng Zuo
- Published: 2026-08-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.01715v1) | [pdf](https://arxiv.org/pdf/2608.01715v1)

## Abstract

Online-judge verdicts and the datasets and benchmarks built on them are treated as ground truth for evaluating and training large language models for code. Yet prior audits have sounded a warning: official suites accept buggy submissions. These audits, however, stop at the warning and offer no practical remedy. Our remedy has two parts: an off-the-shelf coding agent, serving as a test-suite auditor, both builds adversarial test suites to expose what official suites miss and supplies these suites where no official suite exists; a certification chain determines whether each agent-flagged submission is genuinely buggy without relying on the official judge: multiple independently written accepted solutions agree on the expected output for every test, brute-force solutions settle disagreements, and a per-problem validator certifies each failing input legal. One such agent identifies 589 verified accepted-but-buggy submissions among AtCoder's 20,375 audited accepted submissions; extending the same certification to all five agents yields a union floor of 906 such submissions. Five agents, scored separately, each stay within 1.7pp of official-suite coverage on logic bugs those suites catch. On post-cutoff Codeforces problems with no available official suites, the same test-building method leads all five reproduced baselines at every tested input budget. Where an official suite exists, the agent audits suite adequacy instead of assuming it; where none exists, agent suites catch the most buggy submissions among methods we reproduced and tested.
