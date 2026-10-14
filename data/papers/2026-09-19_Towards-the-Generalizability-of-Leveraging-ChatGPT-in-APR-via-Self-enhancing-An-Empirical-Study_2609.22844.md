# Towards the Generalizability of Leveraging ChatGPT in APR via Self-enhancing: An Empirical Study

- arXiv ID: `2609.22844v1`
- Authors: Qingyuan Li, Chuanyi Li, Yaopeng Yang, Ziwen Ge, Jidong Ge, Bin Luo
- Published: 2026-09-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.22844v1) | [pdf](https://arxiv.org/pdf/2609.22844v1)

## Abstract

Automated Program Repair (APR) increasingly relies on Large Language Models (LLMs). ChatGPT-enhanced APR uses techniques such as self-correction and autonomous agents to improve repair without modifying model parameters. Although these approaches report strong results on Defects4J and SWE-bench, the stability of enhancement gains across benchmarks remains under-explored. We evaluate three ChatGPT-enhanced APR methods on three representative, long-standing benchmarks. With GPT-3.5-Turbo, SRepair achieves a larger absolute gain on HumanEval-Java than on Defects4J, while SRepair and FixAgent without extrinsic information yield negative gains on BugsInPy. With GPT-5.4-mini, the evaluated methods achieve larger absolute gains on Defects4J than on HumanEval-Java, while gains on BugsInPy are non-negative but limited. We investigate benchmark-related factors through code transformations and benchmark-specific fine-tuning. Code transformations reduce enhancement gains on Defects4J, while benchmark-specific fine-tuning increases gains on BugsInPy. Directly supplying GPT-3.5-Turbo with error messages and triggering tests yields more correct repairs than the evaluated ChatGPT-enhanced APR methods on BugsInPy. These findings highlight the need to evaluate generalizability across benchmarks and models using multiple metrics, and suggest that directly providing repair-specific extrinsic information may be more effective than enhancement methods when their gains are limited.
