# Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability

- arXiv ID: `2610.01168v1`
- Authors: Roberto Stanzione, Jules Barbe, Magali Parrino, Jérémie Fourmann, Paul Boniol
- Published: 2026-10-01
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.01168v1) | [pdf](https://arxiv.org/pdf/2610.01168v1)

## Abstract

Time Series Anomaly Detection has received increasing attention, driven by the growing availability of complex time series data. This surge has led to the development of numerous detection methods, as well as a variety of benchmarks aimed at thoroughly evaluating their performance. However, most existing detectors remain largely agnostic to domain context, overlooking explainability and interpretability. One of the main reasons for this gap is that current benchmarks primarily focus on detection accuracy, and only few of them evaluate spatial explainability. Moreover, no benchmark currently provides sufficiently rich semantic annotations to support the generation of human-understandable interpretations of anomalies. To address these limitations, we introduce SHAD (Scality High-dimensional Anomaly Detection benchmark), a fully annotated benchmark composed of 215 multivariate, high-dimensional time series collected from real-world distributed cloud storage systems operated by Scality. The proposed dataset includes rich contextual information, covering three families of anomalies with varying degrees of severity. As further contribution, we provide a foundation for future work by evaluating baseline methods for Detection, Explainability, and Interpretability, covering all stages of a TSAD pipeline. For Detection, we benchmark a wide range of existing anomaly detectors, testing their effectiveness on the proposed real-world dataset. Then, we consider explainability by evaluating whether measuring the contribution of each dimension in the generated anomaly score can provide accurate anomaly attributions. Finally, for interpretability, we investigate the effectiveness of frozen LLM baselines in localizing and interpreting anomalies.
