# The Poisoned Chalice of LLM Evaluation Report

- arXiv ID: `2607.07481v1`
- Authors: Jonathan Katzy, Ali Al-Kaswan, Razvan Mihai Popescu, Zhou Yang
- Published: 2026-07-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.07481v1) | [pdf](https://arxiv.org/pdf/2607.07481v1)

## Abstract

Large language models are increasingly used to evaluate and support software engineering tasks, yet the validity of these evaluations is often undermined by uncertainty about whether benchmark instances were seen during pretraining. This can lead to data contamination, which may inflate performance and result in misleading conclusions about model capability. Despite this, the training corpora of many modern models are only partially disclosed, making direct decontamination infeasible. This creates a need for practical methods that can detect a large language models' prior exposure to training data without access to the full training corpus.
  To address this challenge, we organize the first Poisoned Chalice of LLM Evaluation Competition, co-located with the FSE-AIWare 2026 Competition Track. The competition frames contamination detection as a white-box membership inference task on source code and provides participants with curated datasets, target models, baseline attacks, and a final evaluation on a held-out model and dataset. This design encourages methods that generalize beyond superficial dataset artifacts and beyond a single training setting.
  This paper reports the setup and results of the competition. More broadly, the competition aims to catalyze the community around trustworthy LLM evaluation for software engineering.
