# What Was Once Learned May Need to Be Unlearned: Machine Unlearning for Deprecated API Knowledge in Large Language Models

- arXiv ID: `2609.25786v1`
- Authors: Jin Liu, Yanzhong He, Guancheng Lin, Xiao Liu, Jacky Wai Keung, Xiao Yu, Xiaoxue Ma
- Published: 2026-09-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.25786v1) | [pdf](https://arxiv.org/pdf/2609.25786v1)

## Abstract

Large language models (LLMs) for code completion may generate deprecated APIs because their pre-training corpora contain code from historical library versions. Existing approaches use inference-time intervention, model editing, or machine unlearning, but multiple plausible completions make predefined replacements restrictive. Moreover, existing studies rarely verify whether models exhibit the targeted deprecated behavior or evaluate unintended changes to other APIs.
  We conduct a systematic empirical study of machine unlearning for deprecated API knowledge and construct MUDAPIBench, a behavior-grounded benchmark with over 7,000 model-specific instances derived from 145 deprecated-to-up-to-date API mappings across eight Python libraries. Instances are retained only when the original model generates the target deprecated API. We evaluate eight representative unlearning methods across three code LLMs on deprecated API forgetting, up-to-date API generation, preservation of other and unrelated API behaviors, general code-generation capability, and efficiency.
  Results show that Gradient Difference (GD) provides the best overall trade-off, suppressing deprecated APIs while preserving other capabilities with moderate computational costs. Further analyses reveal substantial variation across libraries and show that APIs deprecated after the model's training-data cutoff are harder to forget. Layer-wise analyses indicate that GD achieves effective forgetting with comparatively controlled internal changes.
