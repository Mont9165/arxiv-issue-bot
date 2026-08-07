# Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects

- arXiv ID: `2607.12068v1`
- Authors: Preet Jhanglani, Zeel Kaushal Desai, Vidhi Kansara, Eman Abdullah AlOmar
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12068v1) | [pdf](https://arxiv.org/pdf/2607.12068v1)

## Abstract

The integration of AI-powered coding agents into Continuous Integration/Continuous Delivery (CI/CD) pipelines has fundamentally altered how software verification is conducted. While these agents successfully automate the test generation, current evaluation benchmarks (e.g., SWE-bench) largely focus on pass-rates rather than the intrinsic quality of the generated tests. This raises the possibility of "stealth technical debt", in which test suites pass execution but do not offer comprehensive coverage or semantic value. We address this methodological gap through a large-scale, empirical comparison of 204,673 test artifacts which comprises of 24,941 human-authored files and 179,732 agent-generated files; sourced from the AIDev dataset. Using the Abstract Syntax Tree (AST) parsing with Python's naive ast module, we implemented a "white-box" static analysis framework to evaluate three quality dimensions: Assertion Strength (RQ1), Edge-Case Coverage (RQ2), and Flakiness Potential (RQ3). Our results present a nuanced inversion of traditional assumptions. AI agents performed better than humans in Edge-Case Coverage, with almost twice the variety of boundary checks (Variety Score: 0.62 vs 0.32) and a higher frequency of null-safety testing (13.40% vs. 8.3%), even though human developers had a slight advantage in Assertion Strength (88.1% strong assertions vs. 85.37% for agents). But this thoroughness comes at a price: due mostly to their reliance on file I/O and non-deterministic logic, agent-generated tests exhibited a higher risk of flakiness (Candidate Rate: 0.41 vs. 0.30). These findings suggest that while AI agents excel at rigorous boundary testing, they lack the "environmental awareness" needed to write stable, hermetic tests.
