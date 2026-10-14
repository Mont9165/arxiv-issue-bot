# Mining Subscenario Refactoring Opportunities in Behaviour-Driven Software Test Suites: ML Classifiers and LLM-Judge Baselines

- arXiv ID: `2605.14568v1`
- Authors: Ali Hassaan Mughal, Noor Fatima, Muhammad Bilal
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.14568v1) | [pdf](https://arxiv.org/pdf/2605.14568v1)

## Abstract

Context. Behaviour-Driven Development (BDD) software test suites accumulate duplicated step subsequences. Three published refactoring patterns are available (within-file Background, within-repo reusable-scenario invocation, cross-organisational shared higher-level step), but no prior work automates which recurring subsequences are worth extracting or which mechanism applies. Objective. Rank recurring step subsequences ("slices") by refactoring suitability (extraction-worthy), pre-map each to one of the three patterns, and quantify prevalence across the public BDD ecosystem. Method. Every contiguous L-step window (L in [2, 18]) in a 339-repository / 276-upstream-owner Gherkin corpus is keyed by paraphrase-robust cluster identifiers and counted under three scopes. Sentence-BERT (SBERT) / Uniform Manifold Approximation and Projection (UMAP) / Hierarchical Density-Based Clustering (HDBSCAN) recovers paraphrase-equivalent slices. Three authors label a stratified 200-slice pool against a written rubric. An eXtreme Gradient Boosting (XGBoost) extraction-worthy classifier trained under 5-fold cross-validation is compared with a tuned rule baseline and two open-weight Large Language Model (LLM) judges. Results. The miner produces 5,382,249 slices collapsing to 692,020 recurring patterns. Three-author Fleiss' kappa = 0.56 (extraction-worthy) and 0.79 (mechanism). The classifier reaches out-of-fold F1 = 0.891 (95% CI [0.852, 0.927]), outperforming both the rule baseline (F1 = 0.836, p = 0.017) and the better LLM judge (F1 = 0.728, p < 1e-4). 75.0%, 59.5%, and 11.7% of scenarios carry a within-file Background, within-repo reusable-scenario, or cross-organisational shared-step candidate. Conclusion. Paraphrase-robust subscenario discovery yields a corpus-wide census of BDD refactoring opportunities; pipeline, classifier predictions, labelled pool, and rubric are released under Apache-2.0.
