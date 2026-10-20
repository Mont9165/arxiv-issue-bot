# Narratives Mislead: An Empirical Study of How LLMs Misjudge CVSS Severity in Bug Bounty Reports

- arXiv ID: `2610.24623v1`
- Authors: Ruitao Feng, Yuekang Li, Yao Zhang
- Published: 2026-10-17
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.24623v1) | [pdf](https://arxiv.org/pdf/2610.24623v1)

## Abstract

Bug bounty platforms receive vulnerability reports faster than vendors can triage them, and Large Language Models (LLMs) are increasingly considered for assigning the Common Vulnerability Scoring System (CVSS) severity that drives prioritization. Prior evaluations score short CVE descriptions and report accuracy, but deployment depends on how models err, not only how often. CVSS gives each metric a formal meaning that departs from how researchers describe impact in narrative reports, and model rationales suggest that errors concentrate where the two diverge; we ask whether this pattern is systematic. From 4,281 publicly disclosed reports mined from Huntr and HackerOne, we build a benchmark of 240 Huntr reports with vendor-validated CVSS vectors and evaluate eight LLMs under four prompting strategies and fine-tuning, measuring errors by severity class and score and analysing sub-vectors on individual reports. The best prompting configuration reaches only 49.58% level accuracy, ten points above always predicting the majority level, and fine-tuning a 7B model raises this to at most 56.25%, an optimistic upper bound. Errors are directional: models overestimate far more often than they underestimate, and they almost never recognize low-severity vulnerabilities. We trace these errors to three semantic boundaries that the specification draws and narrative reports blur: potential versus realized impact, impact magnitude versus authorization scope, and uncertainty versus the worst case. Because the violations originate partly in the report, we close with an exploratory case study: on four reports, a boundary-aligned, exploit-free report structure lowered a frontier model's score where the narrative invited an unclaimed account takeover, but left the metrics a report does not settle open, and the two published labels disagreed on three of the four reports.
