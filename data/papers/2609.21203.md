# Embedding Drift in Code Vulnerability Models Under Intended Behaviour-Preserving Transformations

- arXiv ID: `2609.21203v1`
- Authors: Hasti Ghaneshirazi, Tahsin Reza, Ladan Tahvildari
- Published: 2026-09-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.21203v1) | [pdf](https://arxiv.org/pdf/2609.21203v1)

## Abstract

Code edits that preserve program behaviour can shift frozen code embeddings across classifier decision boundaries, causing correctly detected vulnerabilities to be predicted as benign. Such instability is problematic because semantically neutral changes, including comment removal, insertion of unreachable code, variable renaming, and loop rewriting, should not alter a model's security judgment. We investigate this issue using 15,000 C/C++ functions organized as 7,500 vulnerable-patched pairs from the Big-Vul dataset. Four mutation tracks are applied to both vulnerable and benign samples: comment removal, unreachable code insertion, variable renaming, loop rewriting, and a combined setting that applies all transformations. Using frozen microsoft/codebert-base embeddings with six downstream classifiers, we evaluate the robustness of vulnerability predictions and introduce a train-only defence that projects clean and mutated representations closer together while preserving vulnerability-class information. Under combined mutations, the baseline Vulnerable Flip Rate (VFR) ranges from 35.55% to 42.15%. The proposed defence reduces the mean common-set VFR from 22.60% to 11.32% and improves mean mutated accuracy from 55.33% to 57.10%. For Logistic Regression, VFR decreases by 17.29 percentage points, although benign-to-vulnerable flips increase by 11.95 percentage points. These results indicate that the defence improves robustness to semantics-preserving code transformations but introduces a false-positive trade-off and does not fully eliminate prediction instability.
