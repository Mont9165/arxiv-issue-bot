# Beyond Fail-to-Pass: Iterative Hardening of Co-Generated Bug Reproduction Tests and Fixes

- arXiv ID: `2607.19843v1`
- Authors: Yuhao Tan, Zhibang Yang, Fangkai Yang, Yuan Yao, Yu Kang, Lu Wang, Pu Zhao, Xin Zhang, Xiaoxing Ma, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- Published: 2026-07-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.19843v1) | [pdf](https://arxiv.org/pdf/2607.19843v1)

## Abstract

Large language models (LLMs) have made automated program repair (APR) increasingly practical for real-world bugs, but repairing directly from bug reports remains underconstrained. Bug reproduction tests (BRTs) help close this gap by turning a bug report into an executable, bug-specific signal that can guide repair and validate candidate patches. Existing work has therefore studied BRT generation as a core subproblem in APR and mainly evaluates a generated BRT using the fail-to-pass (F->P) criterion, which requires the test to fail on the buggy code but pass on the golden fix. We show that F->P alone is insufficient when the goal of a BRT is to improve downstream repair. In particular, some F->P BRTs are lax, reproducing the observed symptom yet still admitting plausible-but-incorrect patches. We formalize this missing quality dimension by separating F->P BRTs into rigorous and lax ones, and show empirically that only the former consistently improve repair success. We further find that co-generation introduces test--fix error coupling, where the in-trajectory fail-to-pass (F->P) check can pass even when both the generated patch and generated test are wrong. Based on these findings, we propose CoHarden, a co-generation framework that uses the Lax signal as an in-loop convergence criterion. CoHarden first generates a test before any fix, then iteratively hardens the test and fix against surviving mutation patches until the generated test no longer admits Lax regressions. Experiments show that CoHarden reaches 69.4% Resolved and 78.9% F->P on SWE-bench Verified, outperforming the strongest fix-only and cogeneration baselines by +9.6 and +7.9 percentage points in Resolved, respectively, with consistent gains across LLM backbones and benchmarks.
