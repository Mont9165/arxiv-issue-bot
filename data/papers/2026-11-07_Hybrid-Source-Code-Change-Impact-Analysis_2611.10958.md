# Hybrid Source Code Change Impact Analysis

- arXiv ID: `2611.10958v1`
- Authors: Katharina Stengg, Christian Macho, Martin Pinzger
- Published: 2026-11-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.10958v1) | [pdf](https://arxiv.org/pdf/2611.10958v1)

## Abstract

Change impact analysis (CIA) helps developers identify code entities impacted by their initial changes. While several approaches for CIA were proposed, they still struggle with either low precision or low recall, thereby increasing manual effort for developers to verify the results. Furthermore, limitations in the used datasets and experimental setups can bias the results reported by many CIA approaches. In this paper, we first address the dataset limitations by manually labeling 1,931 changed code entities stemming from 263 commits of 22 open-source Java projects. Next, we introduce two variants of katIA, our code change impact analysis approach that combines static impact analysis with the reasoning capabilities of large language models (LLMs). The first variant uses a single prompt (katIA-SP) for refining an initial static impact set while the second variant uses three specialized agents (katIA-MA). The evaluation with our curated dataset shows that katIA-SP with Gemini 2.5 Flash achieved an F1-score of 22.4% when matching impacted entities by their fully qualified names (FQN) and 27.0% when matching them by their class and entity names (CE). The latter shows an improvement of 2.0 percentage points over the state-of-the-art. This score is further improved by katIA-MA which, using Gemini 2.5 Flash, yields an FQN-matching F1-score of 29.1% and a CE-matching F1-score of 33.3%. While these improvements come at the cost of increased median generation time from 0.570 s to 11.214 s and median token usage from 1,235 to 6,462 tokens, the improved performance justifies the additional cost. The comparison of three LLMs using katIA-SP finds that Gemini 2.5 Flash is the most consistent model. These results indicate that combining static impact analysis with LLM-based refinement, particularly with the multi-agent variant, can improve code change impact analysis.
