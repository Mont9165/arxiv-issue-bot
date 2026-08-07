# DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch

- arXiv ID: `2606.10728v1`
- Authors: Jiale Zhao, Guoxin Chen, Fanzhe Meng, Wayne Xin Zhao, Ruihua Song, Ji-Rong Wen, Kai Jia
- Published: 2026-06-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.10728v1) | [pdf](https://arxiv.org/pdf/2606.10728v1)

## Abstract

As the capabilities of LLM-based code agents continue to advance, their expected role is expanding beyond localized bug fixing in existing codebases toward architecting and implementing complete software repositories from high-level specifications. However, training agents for such long-horizon software engineering tasks remains difficult due to the scarcity of large-scale, verifiable whole-repository generation data. In this paper, we introduce \textbf{DeNovoSWE}, a large-scale dataset for whole-repository generation. DeNovoSWE comprises 4,818 high-quality instances, where each instance requires generating a complete repository from documentation. Our dataset is automatically constructed through a carefully designed sandboxed agentic workflow, enabling scalable curation without human annotation. DeNovoSWE is constructed with "divide and conquer" and critic-repair philosophy. To balance data quality and diversity, we further introduce a difficulty-aware trajectory filtering strategy. Fine-tuning Qwen3-30B-A3B on DeNovoSWE substantially improves long-horizon SWE performance, raising its score on the challenging BeyondSWE-Doc2Repo benchmark from 5.8% to 47.2%.
