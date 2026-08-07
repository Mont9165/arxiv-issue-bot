# Beyond Refusal: A Same-Lineage Study of Aligned and Abliterated LLMs for Vulnerability Analysis

- arXiv ID: `2607.05842v1`
- Authors: Mingchen Li, Meikang Qiu, Zifan Peng, Heng Fan, Song Fu, Junhua Ding, Yunhe Feng
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.05842v1) | [pdf](https://arxiv.org/pdf/2607.05842v1)

## Abstract

Large language model (LLM)-assisted software security operates at a difficult boundary: the vulnerability-analysis terminology needed for legitimate code review, triage, and repair can closely resemble terminology associated with misuse. Existing safety and cybersecurity evaluations are difficult to interpret in this setting because they often compare unrelated model families, thereby conflating safety behavior with differences in architecture, scale, training data, and deployment. To isolate this factor, we study safety state: whether refusal behavior remains intact (Aligned) or has been refusal-ablated (Abliterated) within same-lineage models. We ask how this safety state affects defensive utility across software-security workflows. We compare aligned instruction-tuned models with publicly released refusal-ablated descendants from two model families, Gemma and Qwen. We evaluate Aligned and Abliterated states on vulnerability detection, CWE attribution, vulnerable-line localization, root-cause localization, and executable patch validation. We further treat prompt wording as a controlled framing dimension: prompts begin with neutral code-review language, add authorization context, and vary the density of cybersecurity terminology. In a Gemma-based Java/Vul4J repair-validation study, Abliterated achieves higher early-stage validation rates, with 67.8%, 65.0%, and 32.8% of patches judged usable, successfully applied, and successfully compiled, respectively, compared with 29.9%, 24.9%, and 9.0% for Aligned. In the Qwen pair, Abliterated improves localization performance, increasing line-level F1 from 2.08% to 3.91% and Top-1 accuracy from 4.10% to 6.95%. These findings suggest that evaluations of LLM-based security assistants should jointly measure whether models respond, whether their usable responses are correct, and whether their outputs remain actionable across the engineering workflow.
