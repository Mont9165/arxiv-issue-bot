# Mitigating LLM Sycophancy in Code Smell Detection Using Evidence-Guided Reasoning Prompts

- arXiv ID: `2607.10411v1`
- Authors: Istiaq Ahmed Fahad, Kamruzzaman Asif, Md. Nurul Ahad Tawhid
- Published: 2026-07-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.10411v1) | [pdf](https://arxiv.org/pdf/2607.10411v1)

## Abstract

Large Language Models (LLMs) are increasingly used for code smell detection tasks due to their ability to interpret program semantics. However, their reliability in this context remains poorly explored, particularly under varying prompt conditions where model predictions may be influenced by external cues rather than code characteristics. One such limitation is sycophancy bias, where models tend to align their outputs with user-provided assumptions instead of performing objective analysis. In this paper, we present the first systematic empirical study of sycophancy bias in LLM-based code smell detection. Using the MLCQ dataset, we evaluate how different prompt framings like confirmation bias, contradictory hints, and false premises affect model predictions. Our results show that LLMs are highly sensitive to prompt variations, with Decision Flip Rates reaching up to 72% and False Alignment Rates exceeding 90%, indicating substantial instability and agreement with misleading prompts. To address this issue, we propose Evidence-Guided Debiasing Prompting (EGDP), a structured prompting strategy that enforces evidence-first reasoning. EGDP reduces decision instability and improves robustness, lowering Decision Flip Rates to as low as 12% and False Alignment Rates to as low as 21%, while increasing reliance on structurally grounded evidence. Our findings demonstrate that sycophancy bias poses a critical threat to the reliability of LLM-based code smell detection, and that evidence-guided reasoning provides an effective and generalizable mitigation approach.
