# A Comparative Study of Importance Attribution to Columns in Deep Learning over Relational Databases

- arXiv ID: `2611.05986v1`
- Authors: Hila Levi-Yosefi, Shunit Agmon, Ester Livshits, Agapi Rissaki, Benny Kimelfeld
- Published: 2026-11-04
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.05986v1) | [pdf](https://arxiv.org/pdf/2611.05986v1)

## Abstract

Deep learning over relational databases has led to increasingly effective prediction models, motivating a growing need to explain their behavior. We study explanation methods that assign importance scores to individual database attributes, focusing on a fundamental question: to what extent does the choice of importance-attribution method matter? We develop a methodology to systematically compare importance-attribution methods and analyze their similarities and differences. In particular, we study two aspects of the explanations: which attributes they deem important, captured by differences in attribute rankings, and how importance scores vary across attributes, captured by differences in score distributions. We further investigate whether these differences are reflected in the conventional measure of explanation quality, fidelity.
  We apply our methodology in an extensive empirical study of four methods: Monte Carlo Shapley, Kernel SHAP, single-attribute impact, and mask learning. We experiment with multiple datasets and tasks using two RDL architectures: heterogeneous GraphSAGE and Relational Graph Transformers. Our experiments show that explanation methods behave differently depending on the prediction type: regression or classification. In regression, most methods exhibit high agreement in attribute rankings, whereas classification yields considerably less consensus. Notably, while mask learning frequently diverges in its importance distributions, Shapley-based methods and single-attribute impact often converge to similar explanations. This suggests that, in many settings, single-attribute impact can replace Shapley at substantially lower computational cost. Overall, our study provides methodological tools for comparing importance-attribution methods, and empirical evidence that their choice has important consequences for interpreting relational deep learning models.
