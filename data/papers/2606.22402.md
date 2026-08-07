# Reinforcement learning to improve large language model-based automated code compliance systems

- arXiv ID: `2606.22402v1`
- Authors: Jack Wei Lun Shi, Minghao Dang, Wawan Solihin, Leong Hien Poh, Justin K. W. Yeoh
- Published: 2026-06-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.22402v1) | [pdf](https://arxiv.org/pdf/2606.22402v1)

## Abstract

Large language model (LLM)-based approaches for automated code compliance (ACC) of building regulations are prone to generating incorrect and hallucinated computer-processable rules. This paper introduces P4IR, a two-stage framework that uses supervised fine-tuning (SFT) to instill domain knowledge in an LLM, followed by Group Relative Policy Optimization (GRPO) to improve the accuracy of the generated intermediate representations in the form of high-level code skeletons. The framework achieved reductions of up to 23.8% and 38.6% in tree edit distance and token-level Levenshtein distance respectively, relative to the SFT baselines. Comparative analysis demonstrates that this approach in a zero-shot setting outperforms leading LLMs in both code structure and semantics, specifically Claude Opus and Sonnet 4.5, GPT-5.2, Qwen-3-Max, and GLM-4.7, evaluated via few-shot prompting. Additionally, the GRPO stage produced a small yet statistically significant reduction in false positives. By combining SFT with GRPO to optimize directly for domain-specific objectives, this approach offers a path toward more accurate and reliable LLM-based ACC systems.
