# Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study

- arXiv ID: `2606.12231v1`
- Authors: Guangzong Cai, Ruiyin Li, Peng Liang, Zengyang Li, Mojtaba Shahin
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.12231v1) | [pdf](https://arxiv.org/pdf/2606.12231v1)

## Abstract

The adoption of AI-powered Integrated Development Environments (AI IDEs) has introduced "Rules" as a novel software artifact, allowing developers to persistently inject project-specific constraints and architectural guidelines into the context of Large Language Models (LLMs). Despite their role in aligning AI behavior with developer intent, the taxonomy, evolution, and practical impact of these rules remain largely unexplored. To bridge this gap, we conducted a mixed-methods empirical study on AI IDE rules. By mining 83 open-source projects and extracting 7,310 rules, we established a comprehensive taxonomy comprising 5 primary and 25 secondary categories. We then triangulated these artifacts with survey responses from 99 practitioners. Our analysis identified a contrast between developer priorities and actual configurations: while practitioners rate architectural constraints as highly important, rule files in repositories primarily consist of low-level workflow and code formatting constraints. Furthermore, our analysis of 1,540 rule evolution events revealed that rules are updated frequently. Repository data further indicate that rule evolution is primarily driven by constructive context expansions (29.17%) and enrichments (26.59%). In contrast, surveyed developers reported modifying rules primarily to correct AI errors (77.78%), typically by adding new negative constraints rather than editing existing ones. Finally, an artifact compliance assessment of 160 rule evolution events revealed that updating rules significantly improves the adherence of software artifacts, with the average artifact compliance rate increasing by 22.99% (from 49.14% to 72.13%) following an update. Our study provides empirical insights that can help developers optimize prompting strategies and guide tool builders in designing automated conflict-detection and context-management mechanisms for AI IDEs.
