# One Is Not Enough: The Untold Story of Multiple Security Patches for One Vulnerability

- arXiv ID: `2609.07224v1`
- Authors: Fangyuan Zhang, Lyuye Zhang, Lingling Fan, Chengwei Liu, Yinan Li, Liang Huang, Yang Liu, Zheli Liu, Sen Chen
- Published: 2026-09-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2609.07224v1) | [pdf](https://arxiv.org/pdf/2609.07224v1)

## Abstract

Security patches (SPs) are the main mechanism for fixing software vulnerabilities, yet a single vulnerability is not always resolved by a single patch: fixes may be completed incrementally, propagated across maintained branches, or replicated across related repositories. When patch records are incomplete, downstream users may observe only part of the required fix set and therefore apply only partial patching. However, comprehensive patch discovery remains difficult because the prevalence and causes of the multi-SP phenomenon are still poorly understood. In this paper, we present the first large-scale empirical study of multi-SP vulnerabilities. By merging four major vulnerability databases, we construct a dataset of 6,053 multi-SP CVEs with 16,260 SPs, showing that 20.6% of CVEs with patches involve multiple SPs and that merging databases increases recognized multi-SP CVE counts by 36-55% over any single source. We further analyze why a vulnerability is associated with multiple SPs and derive a two-level taxonomy with 6 categories and 16 sub-categories. Based on these findings, we develop SPectre, a taxonomy-driven prototype for comprehensive patch discovery. On 300 multi-SP CVEs, after manually verifying ground-truth SPs, SPectre improves multi-SP patch coverage over representative patch localization baselines, achieving 0.927 recall on same-repository cases and 0.873 recall on cross-repository cases after manual ground truth verification. On 100 recent CVEs recorded as single-patch by all public databases, SPectre further discovers 28 previously unreported SPs across 20 CVEs. Our results show that multi-SP vulnerabilities are both prevalent and systematically underreported, motivating stronger patch-completeness awareness, improved vulnerability database curation, and relation-aware security tooling.
