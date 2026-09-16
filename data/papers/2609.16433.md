# Evaluating the NIST Bugs Framework Against CWE as a Successor for Automated Vulnerability Classification

- arXiv ID: `2609.16433v1`
- Authors: Md Nazmul Hoque, Shaswata Mitra, Subash Neupane, Sudip Mittal, Shahram Rahimi
- Published: 2026-09-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.16433v1) | [pdf](https://arxiv.org/pdf/2609.16433v1)

## Abstract

Vulnerability classification based on root cause weaknesses is essential for numerous cybersecurity activities, where the Common Weakness Enumeration (CWE) serves as a public repository of such flaws. However, its overlapping entries create a non-orthogonal structure. The result is the same vulnerability being mapped to multiple weaknesses, complicating Root Cause Analysis (RCA) and triage. To address this, NIST Special Publication 800-231 introduces the Bugs Framework (BF), which organizes vulnerabilities into <cause, operation, consequence> triples and links such triples into a causal chain, so that a vulnerability carries its root cause and its sink together instead of a single terminal label. To date, however, BF has been specified but not evaluated regarding its performance against the challenges to automated classification. The evidence required for adoption has not been investigated empirically. We evaluate BF as a classification target and a complement to CWE using a systematically screened corpus of automated Common Vulnerabilities and Exposures (CVEs) linked to CWE research. We assess the reproducibility of CVE-to-BF classification through two evaluations. The first is qualitative: an anonymized inter-rater study in which 2 subject-matter experts (SMEs) independently mapped 13 CVEs onto the four BF axes. Annotators showed strong agreement on the cause and operation axes, while the attribute axis indicated fair agreement. We also tested our automated framework across two large language model (LLM) deployments under different budgets for reproducibility analysis. Despite limitations, such as evidence availability and the absence of retrievable fix commits for closed-source software, our findings support the claim that BF is a more structured and automation-friendly framework than CWE. Our exploration reveals specific gaps in BF, including under-specified guidance on attributes.
