# DynaCI: Generating GitHub Actions Workflows via Dynamic Analysis

- arXiv ID: `2610.29890v1`
- Authors: Javid Ditty, Rahul Ghanshyam Chavan, Nimmi Weeraddana, Foyzul Hassan
- Published: 2026-10-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.29890v1) | [pdf](https://arxiv.org/pdf/2610.29890v1)

## Abstract

Continuous Integration (CI) is an essential practice that automatically validates code changes through builds and tests. However, configuring CI workflows remains challenging, as modern software often features complex architectures, numerous dependencies, and support for diverse execution environments. Most CI platforms also require workflows to be written in their particular domain-specific languages. As a result, CI workflows are often error-prone and hard to maintain, especially for those unfamiliar with CI semantics. Prior work on automated CI workflow generation require developers to create specifications that describe their intended workflows using natural language, partial workflows, etc. However, in practice, developers may struggle to articulate requirements and may be unaware of available CI features. To address these limitations, we propose DynaCI, a novel approach that uses runtime information from developers' local environments to generate CI workflows. DynaCI (i) traces the developers' local environment to collect runtime information, (ii) constructs an initial workflow by applying runtime-informed heuristics, and (iii) iteratively refines the workflow via LLM-based Retrieval Augmented Generation (RAG). We evaluate DynaCI on 50 popular Python projects that use GitHub Actions, a popular CI platform, and compare it against the state-of-the-art CI workflow generation approaches: GH-WCOM and LLM4GW. DynaCI outperforms these existing approaches by more than 21.13% in BLEU score and 20.96% in F1 score on average. It also generates workflows without missing functionality in 56% of cases, while requiring fewer manual modifications to repair such exceptions. These results demonstrate that leveraging runtime information substantially improves LLM-based CI workflow generation, and offer a promising direction for broader DevOps configuration automation.
