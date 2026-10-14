# The Cathedral and the Bazaar of Software Vulnerabilities: From the NVD to the CNAs

- arXiv ID: `2607.05670v1`
- Authors: Siqi Zhang, Fabio Massacci, Mengyuan Zhang
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.05670v1) | [pdf](https://arxiv.org/pdf/2607.05670v1)

## Abstract

For decades, the National Vulnerability Database (NVD), the "Cathedral", has been the reference source for vulnerability information for downstream research and industry tasks, e.g., software update prioritization. An emerging "Bazaar" of diverse CVE Numbering Authorities (CNAs) has created many alternative and sometimes diverging sources. We conduct a systematic analysis of divergence in Common Vulnerability Scoring System (CVSS) metrics covering the NVD and the public CNAs. We also check for self-divergence: two identical textual descriptions of CVEs with identical CWEs are rated differently by the same CNA. The odds of diverging are widespread, not uniform and sometimes unexpected. The assessment of Attack Complexity, User Interaction, and Impact are the major metrics where divergence happens. To understand the root causes, we perform a qualitative study by reaching out to the NVD and other CNAs (both open sources and proprietary products). We also discussed the findings at the CVSS Special Interest Group of FIRST, the community responsible for maintaining and evolving the CVSS standard. The key insights are that while something might be due to human errors, in some cases diverging is actually the right thing to do and might require changes in the way CVEs are generated industry-wide, in other cases explaining divergence requires access to additional FAQs. The good news is that the situation is improving since 2025, the bad news is that if one downloads the whole NVD (or another CNA dataset) from several years and uses it for predictions, the models trained on one source do not reliably generalize to a different source (accuracy can drop by 40%). We discuss the implications for practice and research.
