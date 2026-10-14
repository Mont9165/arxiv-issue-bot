# LLM-Guided Issue Generation from Uncovered Code Segments

- arXiv ID: `2604.26118v1`
- Authors: Diany Pressato, Honghao Tan, Mariam Elmoazen, Shin Hwei Tan
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26118v1) | [pdf](https://arxiv.org/pdf/2604.26118v1)

## Abstract

Developers are increasingly overwhelmed by AI-generated issue reports that lack actionability and reproducibility, eroding trust in automated bug detection tools. In this paper, we present IssueSpecter, an automated tool that finds bugs in uncovered code segments and automatically generates prioritized, actionable issue reports. IssueSpecter combines coverage analysis with LLM-based defect identification, producing structured reports complete with severity ratings, reproduction steps, and suggested fixes. We evaluate IssueSpecter on 13 actively maintained Python projects, generating 10,467 issue reports. Manual annotation of the top-130 ranked issues by IssueSpecter confirms that 84.6% of the LLM-generated issues are valid or warrant further investigation, with only 15.4% false positives. LLM-based ranking outperforms rule-based ranking by 50% at P@3 and 41% in MRR. The identified bugs cover a wide variety of types, from logic and boundary errors to security vulnerabilities and state consistency bugs. By ranking issues by priority, IssueSpecter aims to help developers focus their attention on the most impactful bugs first. Finally, we validate IssueSpecter through case studies reproducing real bugs surfaced from its generated issue reports, demonstrating its practical value for automatic bug discovery in open-source Python projects. Compared against CoverUp, a state-of-the-art coverage-driven test generation tool, IssueSpecter achieves a higher bug validity rate (81.0% vs. 76.2%) under identical evaluation conditions, using the same model and the same number of evaluated artifacts per project, while additionally providing structured issue reports with reproduction steps and candidate fixes that are immediately actionable without requiring developers to interpret generated test intent.
