# How Reliable Are NVD CWE Labels? A Large-Scale Semantic Audit with Seclometry

- arXiv ID: `2608.21977v1`
- Authors: Yu Nong, Yao Du, Majid Behravan, Haipeng Cai
- Published: 2026-08-22
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.21977v1) | [pdf](https://arxiv.org/pdf/2608.21977v1)

## Abstract

CWE labels in the National Vulnerability Database (NVD) are widely treated as ground truth for vulnerability search, scanner evaluation, benchmark construction, learning-based security tools, and vulnerability prioritization. Yet their reliability has not been systematically measured at scale, despite growing concerns about NVD's enrichment backlog and anecdotal reports of inaccurate, ambiguous, or missing labels. This paper presents a large-scale, code-semantics-grounded measurement of CWE labeling quality in NVD. We build CWEAgent, a validated auditing instrument based on seclometry, a structured representation of vulnerability semantics that captures the root cause, trigger condition, violated security property, exploit mechanism, and impact of vulnerable code. On a manually curated benchmark of 100 open-source CVEs, CWEAgent achieves 85% top-1 accuracy and 92% ambiguity-aware accuracy. Applying CWEAgent to 15,556 open-source CVEs disclosed from 2017-2026, we find that only 49.70% of NVD CWE labels exactly match the code-grounded label. Another 31.37% are defensible alternatives under taxonomy ambiguity, while 3.63% are evidence-inconsistent likely errors. Label reliability varies sharply by assigning organization and weakness type, and apparent project- or language-level differences are largely composition effects of those underlying weakness types. Evidence-inconsistent labels have also increased over time. Through manual review of 434 confirmed mislabels, we identify six recurring error patterns, showing that CWE noise is a structural problem in vulnerability metadata rather than isolated annotation mistakes.
