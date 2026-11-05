# TACT: A Pragmatic Approach to Qualitative Analysis with an AI Council

- arXiv ID: `2611.05702v1`
- Authors: Rudrajit Choudhuri, Christian Bird, Carmen Badea, Anita Sarma
- Published: 2026-11-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2611.05702v1) | [pdf](https://arxiv.org/pdf/2611.05702v1)

## Abstract

Qualitative data can tell software teams what their stakeholders need, yet rigorously analyzing thousands of qualitative responses takes expert time that few teams can afford or justify. Teams therefore often face a false choice: leave the responses unanalyzed, or hand them to a large language model and accept its interpretation and judgment. In this paper, we take a pragmatic approach to AI-assisted qualitative analysis and present TACT (Traceable AI Council for Thematic analysis), a procedure that enables such analysis at scale while keeping teams in control of interpretation and judgment. TACT comes in two variants: TACT-Lite, the core AI council procedure, and TACT-Full, which adds adversaries (models from other model families that critique each model's output) and a decision model that surfaces high-uncertainty code assignments. We evaluated TACT on an independent dataset of 256 Stack Overflow threads qualitatively coded by other researchers. Against their labels, TACT's candidate codebook achieved an F1 of 0.75-0.77 and its final coding an F1 of 0.71-0.72. On a held-out sample, agreement between our own manual coding and TACT's coding was Cohen's $κ$ of 0.79-0.85. TACT is also economical: model calls cost \$13.77 (TACT-Lite) to \$33.59 (TACT-Full) per 100 threads. Finally, drawing on our experience building and validating TACT, we identify pitfalls in AI-assisted qualitative analysis, describe safeguards to address them, and offer guidance for teams and researchers applying TACT in practice.
