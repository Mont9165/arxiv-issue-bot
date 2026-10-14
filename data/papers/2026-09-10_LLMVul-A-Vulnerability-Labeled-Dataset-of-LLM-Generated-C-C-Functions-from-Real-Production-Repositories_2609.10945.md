# LLMVul: A Vulnerability-Labeled Dataset of LLM-Generated C/C++ Functions from Real Production Repositories

- arXiv ID: `2609.10945v1`
- Authors: Mohammad Farhad, Shuvalaxmi Dass
- Published: 2026-09-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.10945v1) | [pdf](https://arxiv.org/pdf/2609.10945v1)

## Abstract

Large language models (LLMs) are increasingly used to generate and assist with software development, yet existing vulnerability datasets largely focus on human-written code or controlled prompting environments. This limits the ability to study security weaknesses in LLM-generated code as it appears in real-world software projects. We present LLMVul, a vulnerability-labeled dataset of LLM-generated C/C++ functions mined from real production repositories. We mine AI-assisted development activity from GitHub over a 4 year period, from November 13, 2022 to September 3, 2026, using provenance signals such as commit metadata and AI-related authorship evidence. After filtering and deduplication, LLMVul contains 21,430 unique C/C++ functions from 226 repositories, together with repository, commit, function, provenance, and AI-tool metadata. We establish vulnerability labels using an ensemble of complementary static-analysis and pattern-based techniques and assign Common Weakness Enumeration (CWE) categories to confirmed vulnerable functions. To assess labeling reliability, we additionally conduct independent manual annotation and measure inter-rater agreement using Cohen's kappa ($k=0.79$). LLMVul contains 1,540 ensemble-vulnerable functions spanning 17 unique CWE categories, providing substantially more real-world LLM-generated vulnerable C/C++ functions than existing vulnerability-oriented LLM code benchmarks. By preserving both code-level vulnerability labels and generation/provenance metadata, LLMVul enables reproducible research on vulnerability detection, security evaluation of LLM-generated code, and analysis of vulnerability patterns in AI-assisted software development. The LLMVul dataset is publicly available at https://doi.org/10.5281/zenodo.22668216.
