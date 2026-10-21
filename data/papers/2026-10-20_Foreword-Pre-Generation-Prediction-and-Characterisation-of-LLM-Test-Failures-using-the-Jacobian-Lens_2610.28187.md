# Foreword: Pre-Generation Prediction and Characterisation of LLM Test Failures using the Jacobian Lens

- arXiv ID: `2610.28187v1`
- Authors: Somin Kim, Robert Feldt, Shin Yoo
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.28187v1) | [pdf](https://arxiv.org/pdf/2610.28187v1)

## Abstract

Testing LLM-based software is expensive: each input needs several sampled responses, each judged by a costly oracle. Further, every prompt or model change calls for re-testing. Pre-generation adequacy measures cut this cost by ranking inputs by failure risk based on the model's internal state. However, the state of the art, Clotho, models only passing reference inputs, and its hidden-state representation says nothing about why inputs fail. We present Foreword, a framework built on two ideas: learn from both passing and failing references, and represent inputs through the Jacobian lens (J-lens), an interpretability technique that reads intermediate activations out as scores over vocabulary tokens. Foreword pairs these representations with two estimators: a sparse logistic-regression probe or dual Gaussian Mixture Models (dual GMMs), which also yield a reference density (to flag inputs the references do not cover) and failing-class components (to group similar failures). On ten tasks and three open-weight LLMs, all four combinations of representations and estimators outperform Clotho on average, both for prediction of failure (ROC-AUC improves by 0.14 on average and by up to 0.31) and test prioritisation (15% more failures among the 100 top-ranked inputs on average, up to 33%). Prioritisation obtained using small models also transfers better to proprietary models (on average 22% and up to 41% more failures in the first quarter of prioritised inputs). Importantly, our qualitative case study shows that Foreword supports semantic characterisation of failures by pointing to ambiguities in labels or task specifications. Combined, Foreword can support testers for prioritising inputs, checking support for a prediction, and characterising specific failures, all without generating output.
