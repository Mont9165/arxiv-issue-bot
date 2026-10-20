# From Finding to Fixing: How Useful is Fault Localization for Agentic Program Repair?

- arXiv ID: `2610.25826v1`
- Authors: Xinyu Shi, Zhou Yang, An Ran Chen
- Published: 2026-10-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.25826v1) | [pdf](https://arxiv.org/pdf/2610.25826v1)

## Abstract

Fault localization (FL) aims to identify code locations responsible for software failures and is commonly evaluated by how accurately it ranks known fault locations. Large language model (LLM) agents are changing program repair and are increasingly used to search and reason over repositories. Although recent LLM-based FL methods have improved localization accuracy, their impact on agentic repair remains unclear. To address this gap, we conduct a systematic empirical study of FL in agentic repair. We evaluate six recent FL methods on SWE-bench Verified and Defects4J with three LLMs under a common repair framework and analyze 16,248 repair trajectories. We also examine gold locations and bug-cause descriptions as forms of FL guidance across different repair contexts. The studied FL methods do not consistently improve repair success, and higher localization accuracy does not consistently lead to larger repair gains. Yet FL guides agents' early search and helps them reach relevant code sooner. Accurate locations can reduce repair token use by up to 39.2\%, but current FL methods often consume more tokens than they save during repair. Experiments with gold guidance suggest that FL has greater potential when bug inputs contain fewer location clues. Providing bug causes can further improve repair success beyond locations alone. We also find that ground truth from a single reference patch does not fully capture the locations used by successful repairs. These findings help clarify the value of FL in agentic repair and inform future work on its design and evaluation.
