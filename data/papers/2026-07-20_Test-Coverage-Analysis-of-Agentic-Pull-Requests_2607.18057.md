# Test Coverage Analysis of Agentic Pull Requests

- arXiv ID: `2607.18057v1`
- Authors: Atish Kumar Dipongkor, Talank Baral, Wing Lam, Kevin Moran
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.18057v1) | [pdf](https://arxiv.org/pdf/2607.18057v1)

## Abstract

AI coding agents increasingly submit complete pull requests (PRs) with minimal human intervention, shifting software development from AI-assisted to autonomous workflows. As these agents become more prevalent, ensuring the code they generate is adequately tested, by existing tests or by tests the agents write, is critical to preventing regressions, yet little is known about testing in agentic PRs. To address this gap, we analyze 4882 agent-generated PRs from the AIDev dataset (532 Java and 4350 Python PRs) produced by five coding agents. We study (i) how often agents include test changes and (ii) how well covered are code changes by existing and agent-written tests. Agents include test changes in only 49.6% of PRs that change code under test files. Existing tests provide an incomplete safety net: they cover 61.5% of agents' changed executable lines in Java and only 27.0% in Python, where 64.8% of PRs have no changed line executed by any existing test. Agent-written tests improve coverage over existing tests, but only in a minority of PRs: 35.9% of Java and 22.5% of Python Code + Tests PRs show a coverage gain. Across both languages, error-handling constructs (e.g., try and catch blocks) are the most consistently under-tested, with miss rates reaching 86.0% in Java and 81.0% in Python. These findings motivate coverage-aware development practices, coverage feedback loops for coding agents, and evaluation benchmarks that measure test quality to better help agents reliably test their own code.
