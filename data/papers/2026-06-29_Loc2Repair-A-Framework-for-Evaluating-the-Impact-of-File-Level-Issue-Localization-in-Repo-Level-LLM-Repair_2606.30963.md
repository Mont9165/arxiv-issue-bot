# Loc2Repair: A Framework for Evaluating the Impact of File-Level Issue Localization in Repo-Level LLM Repair

- arXiv ID: `2606.30963v1`
- Authors: Mohammad Nour Al Awad, Sergey Ivanov
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.30963v1) | [pdf](https://arxiv.org/pdf/2606.30963v1)

## Abstract

Repository-grounded automated repair is often reported as a single end-to-end capability, which hides distinct failure modes such as poor file targeting, incorrect patch synthesis, and failed iterative debugging. We present Loc2Repair, a modular evaluation framework for controlled analysis of repository-grounded repair pipelines, and use it to isolate file-level issue localization as an upstream variable. Loc2Repair decouples localization and repair under a shared runtime, artifact schema, and evaluation harness, allowing researchers to combine different localization models and repair backbones under matched conditions. Using three repair backbones on SWE-bench Verified, we compare baseline repair without explicit localization, repair guided by predicted localization from two localizers, and repair guided by gold modified-file sets. Explicit localization consistently improves resolved rate across all backbones: pooled performance increases from 44.7% for baseline repair to 48.9% and 49.1% with predicted localization, and to 52.4% with gold localization. Localization also reduces mean elapsed time overall: in pooled paired analysis, mean elapsed time decreases by 100.94 s and 52.25 s for the two predicted-localization settings, and by 154.45 s with gold guidance, although token effects remain heterogeneous across models. Overall, Loc2Repair shows file-level localization is a consistent repair lever, improving effectiveness and mean latency in pooled analysis, while gold-guided failures expose headroom beyond localization.
