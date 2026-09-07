# The History Is the Detector: Executing CVE Patch History, End-to-End

- arXiv ID: `2609.05335v1`
- Authors: Qiushi Wu, Kevin Eykholt, Youngja Park, Xiaokui Shu, Dhilung Kirat, Douglas Lee Schales, Ian Molloy
- Published: 2026-09-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.05335v1) | [pdf](https://arxiv.org/pdf/2609.05335v1)

## Abstract

Public vulnerability databases collect rich information about known software flaws, including their weakness types, affected components, and related patches. Fixing commits provide the exact code changes that removed these flaws. While these records capture why the original code was unsafe, they are documented mainly for human inspection rather than automated reuse. Consequently, the same unsafe conditions may still exist elsewhere in code without a known advisory, leaving much of this detection knowledge unused.
  We present BUGSTONE-E2E, a framework that transforms vulnerability history into executable detection rules and validates their findings. First, BUGSTONE-E2E mines reusable rules from verified fixing commits, capturing scan anchors, fix semantics, and CVE provenance and organizing them by CWE and language. Second, detection follows a funnel-shaped pipeline: early stages process a large pool of candidates using lightweight analysis, while later stages apply increasingly capable and expensive models to a shrinking set of targets. Specifically, BUGSTONE-E2E first enumerates call sites matching rule anchors using Tree-sitter, then removes benign sites using lightweight heuristics without LLM calls. Next, LLM-based agents inspect the remaining candidates guided by the rule. Following this inspection, the system re-triages surviving candidates and builds runtime verifications, then generates scope-checked patches validated via two-sided differential tests. Using 19,325 high-severity CVEs from 2022 to 2026, BUGSTONE-E2E identifies 2,710 fixing commits and constructs 1,033 detection rules across 56 CWE families, packaged into 172 skills. When applied across 14 programs, it produced runtime evidence for 644 findings. These results demonstrate that CVE history can be turned into an executable workflow, transforming past vulnerabilities into reproducible detection and repair.
