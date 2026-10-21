# Raise or Check? Predicting the Necessity of Additional Fuzzing for Continuous Fuzzing

- arXiv ID: `2610.27828v1`
- Authors: Riku Kato, Tatsuya Shirai, Olivier Nourry, Yutaro Kashiwa, Kenji Fujiwara, Yasutaka Kamei, Hajimu Iida
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.27828v1) | [pdf](https://arxiv.org/pdf/2610.27828v1)

## Abstract

Continuous fuzzing is used for vulnerability detection in Open Source Software (OSS). Large-scale services such as Google's OSS-Fuzz fuzz over 1,300 projects and have revealed more than 10,000 vulnerabilities. Despite this, a considerable time lag often exists between when a vulnerability is introduced and when it is detected (i.e., the window of exposure). Given the computational cost of additional fuzzing, we aim to allocate fuzzing resources efficiently using vulnerability-risk estimates. We propose RAISE (Risk-Aware Intensive Supplemental Execution Framework), a Just-In-Time (JIT) framework that prioritizes additional fuzzing for high-risk project-days. RAISE performs binary classification at the project-day granularity to estimate whether a vulnerability is introduced on a given day. We construct a dataset combining vulnerability-introducing commits from the OSV database with daily coverage and change metrics from OSS-Fuzz, covering 15 C/C++ projects and 15,210 project-days, of which 347 (2.28%) are vulnerability-introducing. In a cross-project validation setting, our best model, a Random Forest combining VCCFinder-based static features with dynamic fuzzing features, achieves a ROC-AUC of 0.74, substantially outperforming a random baseline; coverage metrics, led by PatchCoverage, are the most important features. In a simulation over 968 vulnerabilities comparing five allocation strategies, Simple-Regression was significantly more cost-efficient than the prediction-agnostic heuristics, spending 91.60 additional fuzzing sessions per detected vulnerability, roughly half the cost of the Median heuristic (171.89). RAISE shows that JIT vulnerability prediction with coverage-aware fuzzing features can effectively guide risk-aware allocation of continuous fuzzing resources.
