# SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code Repository Setup?

- arXiv ID: `2605.26186v1`
- Authors: Zihang Zhou, Ziqian Ren, Yukai Wu, Yingjie Xiong, Wei Zhou, Chao Peng, Dong Zhang, Bingheng Yan, Xuanhe Zhou, Fan Wu
- Published: 2026-05-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.26186v1) | [pdf](https://arxiv.org/pdf/2605.26186v1)

## Abstract

Functionality-correct repository setup aims to configure execution environments (e.g., dependencies, build scripts) to successfully execute a repository's documented features. It presents significant challenges due to diverse, repository-specific failures, including dependency incompatibilities, missing toolchains, incomplete installations, and verification-strategy mismatches. Existing LLM agents struggle to robustly resolve these issues, specifically failing to support (1) cross-repository experience transfer, (2) multi-step trial-and-repair under non-invertible state changes, and (3) robust verification of setup outcomes to distinguish setup-induced failures from repository bugs. To address this, we introduce SetupX, an experiential learning-based setup framework. First, we construct a Self-Evolving Experience Representation (XPU), a dual-modality knowledge unit encoding setup signals, textual guidance, executable actions to dynamically transfer verified environment fixes to unseen repositories. Second, we employ Experience-Augmented Speculative Execution backed by a LIFO Docker snapshot stack, enabling the agent to proactively trial fixes and safely roll back to known-good states. Third, we introduce a Prosecutor-Judge Verification Protocol that separates evidence collection from final judgment, enabling more reliable setup verification beyond superficial build-time metrics. Evaluation results on carefully-crafted benchmarks show SetupX achieves highest performance (e.g., 92% pass rate) and outperforms the strongest baseline by over 19%. Crucially, SetupX excels in complex multi-repository setup requiring coordinating multiple interconnected services across different containers. The code repository is available at https://github.com/OpenDataBox/SetupX.
