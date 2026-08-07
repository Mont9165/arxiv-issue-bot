# FIKA: Expanding Dependency Reachability with Executability Guarantees

- arXiv ID: `2604.20015v1`
- Authors: Yogya Gamage, Meriem Ben Chaaben, Martin Monperrus, Benoit Baudry
- Published: 2026-04-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.20015v1) | [pdf](https://arxiv.org/pdf/2604.20015v1)

## Abstract

Automated third-party library analysis tools help developers by addressing key dependency management challenges, such as automating version updates, detecting vulnerabilities, and detecting breaking updates. Dependency reachability analysis aims at improving the precision of dependency management, by reducing the space of dependency issues to the ones that actually matter. Most tools for dependency reachability analysis are static and fundamentally limited by the absence of execution. In this paper, we propose FIKA, a pipeline for providing guarantees of executability for third-party library call sites. FIKA generates code that is executed, and whose execution trace provides guarantees that a third-party library call site is actually reachable. We apply our approach to a dataset of eight Java projects to empirically evaluate the effectiveness of FIKA. On average, 54% of these call sites are covered by the existing test suites, and therefore, have evidence for their executability. FIKA further improves this coverage by 20% and is able to demonstrate executability for 2363 dependency methods. In six out of eight projects, FIKA provides strong guarantees that more than 75% of call sites are executable. We further demonstrate that FIKA is capable of improving the results provided by Semgrep, a state-of-the-art static vulnerability reachability analysis tool. We show that FIKA can help prioritize the vulnerability updates with stronger guarantees of executability in cases where Semgrep yields inconclusive reachability results.
