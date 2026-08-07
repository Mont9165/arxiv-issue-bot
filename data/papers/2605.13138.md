# Code-Centric Detection of Vulnerability-Fixing Commits: A Unified Benchmark and Empirical Study

- arXiv ID: `2605.13138v1`
- Authors: Nils Loose, Joseph Bienhüls, Kristoffer Hempel, Felix Mächtle, Thomas Eisenbarth
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.13138v1) | [pdf](https://arxiv.org/pdf/2605.13138v1)

## Abstract

Automated detection of vulnerability-fixing commits (VFCs) is critical for timely security patch deployment, as advisory databases lag patch releases by a median of 25 days and many fixes never receive advisories. We present a comprehensive evaluation of code language model based VFC detection through a unified framework consolidating over 20 fragmented datasets spanning more than 180000 commits. Across over 180 experiments with fine-tuned models from 125 M to 14 B parameters, we find no evidence that models acquire transferable security-relevant code understanding from code changes alone. When commit messages are available, they dominate model attention, and when removed, an attribution analysis shows that enriching diffs with additional intra-procedural semantic context does not shift model attention toward the code changes. Group-stratified evaluation exposes approximately 17% performance drops compared to random splits, while temporal splits on aggregated datasets prove unreliable due to compositional shift in the underlying project distributions. At a false positive rate of 0.5% all fine-tuned code-only models miss over 93% of vulnerabilities. Larger and more diverse training data or generative approaches show preliminary improvements but do not resolve the underlying limitations. To support future research on code-centric VFC detection, we release our unified framework and evaluation suite.
