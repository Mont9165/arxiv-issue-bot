# Static Metrics Are Insufficient: Predicting Java Method Energy Usage with Execution Time

- arXiv ID: `2607.06124v1`
- Authors: Muhammad Imran, Vincenzo Stoico, Ivano Malavolta
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.06124v1) | [pdf](https://arxiv.org/pdf/2607.06124v1)

## Abstract

The increasing energy demand of software systems is raising concerns about their environmental impact and associated costs. Reasoning on energy usage early in the development flow has the potential to significantly reduce the overall energy usage of a software system, as it allows developers to make informed design and refactoring decisions before inefficiencies propagate. However, assessing energy usage without repeated profiling and direct measurement is difficult, which limits early reasoning in practice. This study investigates the limits of method-level energy prediction in Java, examining whether static source code metrics complemented with method-level execution time can estimate the energy consumption of Java methods. We profile 2,786 Java methods to extract 33 static features and measure execution time and energy, then train and compare eleven regression models. Our findings show that static source code metrics alone yield poor predictive performance, with average R2 values close to zero. Incorporating execution time as a lightweight dynamic input significantly improves accuracy, raising R2 to as high as 0.46. Execution time, internal method calls, and cyclomatic complexity consistently emerge as the strongest predictors of energy consumption.
