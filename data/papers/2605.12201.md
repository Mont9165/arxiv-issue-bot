# Uncertainty Quantification for LLM-based Code Generation

- arXiv ID: `2605.12201v1`
- Authors: Senrong Xu, Yuhao Tan, Yanke Zhou, Guangyuan Wu, Zenan Li, Yuan Yao, Taolue Chen, Feng Xu, Xiaoxing Ma
- Published: 2026-05-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.12201v1) | [pdf](https://arxiv.org/pdf/2605.12201v1)

## Abstract

Prediction sets provide a theoretically grounded framework for quantifying uncertainty in machine learning models. Adapting them to structured generation tasks, in particular, large language model (LLM) based code generation, remains a challenging problem. An existing attempt proposes PAC prediction sets but is limited by its strong monotonicity assumption on risk and single-label classification framework, which severely limits the space of candidate programs and cannot accommodate the multiple valid outputs inherent to code generation. To address these limitations, we propose an approach RisCoSet that leverages multiple hypothesis testing to construct risk-controlling predictions for LLM-based code generation. Given a trained code generation model, we produce a prediction set represented by a partial program, which is guaranteed to contain a correct solution with high confidence. Extensive experiments on three LLMs demonstrate the effectiveness of the proposed method. For instance, compared with the state-of-the-art, our method can significantly reduce the code removal by up to 24.5%, at the same level of risk.
