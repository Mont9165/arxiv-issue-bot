# Refine After Generation: Toward Correct and Concise Patches in LLM-based Program Repair

- arXiv ID: `2608.13292v1`
- Authors: Wenqiang Luo, Jacky Keung, Xiaoyu Shi, Yicheng Sun, Boyang Yang, Zhou Yang, Haoye Tian
- Published: 2026-08-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.13292v1) | [pdf](https://arxiv.org/pdf/2608.13292v1)

## Abstract

Large language models (LLMs) have advanced automatic program repair (APR) to the point where agentic systems routinely resolve real-world, repository-level issues. Yet the generated patch has received little scrutiny beyond whether it passes tests.
  In this paper, we identify patch verbosity as a major yet overlooked concern in LLM-based APR. Characterizing 28 state-of-the-art approaches on SWE-bench Verified, we find that even successful patches are consistently larger and more complex than developer patches, with the median approach producing 121.78% more total changes, 80.91% more net changes, and 43.99% higher cyclomatic complexity. We further show that this verbosity is rooted in capability-oriented design choices such as iterative refinement and broad context, and can hardly be reduced by surface-level controls such as output format or minimality prompts. Motivated by these findings, we formulate post-generation patch refinement and propose RECAP, a lightweight, plug-and-play adapter that attaches to existing repair frameworks after generation. RECAP's refiner is trained via supervised fine-tuning and direct preference optimization with distilled reasoning traces, on a dataset of patch pairs we construct from multiple sources. Across four host systems, prompting, commit-untangling, and minimality-aware baselines reduce patch size only by sacrificing 49 to 217 resolved instances. In contrast, RECAP achieves a substantially better size-correctness tradeoff, cutting average total changes from +242.14% to +4.24% and net changes from +348.24% to -39.75% relative to developer patches while preserving or improving resolution by up to 42 instances. Our results indicate that minimality cannot be simply reduced to syntactic compression, and that decoupling minimization from generation offers a practical path to more reviewable repairs.
