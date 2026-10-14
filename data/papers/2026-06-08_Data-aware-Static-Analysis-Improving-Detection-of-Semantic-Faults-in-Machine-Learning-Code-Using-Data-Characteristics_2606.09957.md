# Data-aware Static Analysis: Improving Detection of Semantic Faults in Machine Learning Code Using Data Characteristics

- arXiv ID: `2606.09957v1`
- Authors: Willem Meijer, Kristian Sandahl, Dániel Varró
- Published: 2026-06-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2606.09957v1) | [pdf](https://arxiv.org/pdf/2606.09957v1)

## Abstract

Semantic faults specific to the use of machine learning models are a common problem for machine learning developers, causing suboptimal predictions, high computational cost, or incorrect outputs. For example, one may erroneously use unscaled data to train a scale-sensitive model. Machine learning developers detect these faults after training their models and manually analyzing the results, making it an inefficient process. We propose a novel data-aware static analysis approach to detect semantic faults in machine learning code, allowing developers to reveal these bugs while writing code instead of after training the model. Our approach uses combined data and control flow analysis, and API contracts, enabling data-aware reasoning about machine learning code at a high level of abstraction. We highlight the potential of our solution by analyzing a sample of real-world machine learning notebooks, finding that we can detect faults that require a data-aware approach.
