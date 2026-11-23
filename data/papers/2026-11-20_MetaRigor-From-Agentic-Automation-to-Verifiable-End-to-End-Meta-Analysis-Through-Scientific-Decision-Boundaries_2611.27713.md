# MetaRigor: From Agentic Automation to Verifiable End-to-End Meta-Analysis Through Scientific Decision Boundaries

- arXiv ID: `2611.27713v1`
- Authors: Yifeng Xie, Chenke Li, Yangshuo Miao, Jingyuan Zheng, Mingxuan Liu, Feiwei Qin, YaQi Wang, Huiyu Zhou, Yifei Chen
- Published: 2026-11-20
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.27713v1) | [pdf](https://arxiv.org/pdf/2611.27713v1)

## Abstract

Automated meta-analysis requires not only accurate numerical extraction but also the consistent preservation of result identity across stages, including the associated study, comparison, population, outcome, time point, and analysis conditions. We present MetaRigor, an LLM workflow framework for verifiable end-to-end evidence synthesis. MetaRigor organizes study results as Study x Target units and operationalizes scientific decision boundaries at the task level through Task Contracts, programmatic rules, and source binding. The model performs semantic interpretation that depends on study context, whereas programs execute formalizable rules, computations, validation, and source verification. We conducted controlled evaluations across five stages: evidence acquisition, data extraction, risk of bias assessment, certainty of evidence assessment, and manuscript generation. MetaRigor achieved an F1 score of 86.29% for complete result delivery and 80.20% agreement for domain-level certainty of evidence judgments. Generated manuscripts received scores of 86.00 under human evaluation, exceeding all three baselines. A seven-case downstream end-to-end evaluation further yielded an aggregate F1 score of 77.01%, exceeding the strongest baseline by 9.78 percentage points. Cross-system tracing of archived outputs from three systems further showed that local mismatches or omissions in result identity could alter statistical inputs and the objects subjected to risk of bias assessment, with these errors subsequently propagating into the final report. Ablation experiments showed that task constraints and programmatic rules played distinct roles across different stages. These findings indicate that, in LLM-driven evidence synthesis workflows, consistently maintaining explicit result identity, decision boundaries, and provenance relationships is critical to improving end-to-end verifiability.
