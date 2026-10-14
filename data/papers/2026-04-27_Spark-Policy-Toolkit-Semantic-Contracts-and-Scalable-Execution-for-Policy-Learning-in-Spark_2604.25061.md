# Spark Policy Toolkit: Semantic Contracts and Scalable Execution for Policy Learning in Spark

- arXiv ID: `2604.25061v1`
- Authors: Zeyu Bai
- Published: 2026-04-27
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`, `cs.LG`, `cs.PF`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2604.25061v1) | [pdf](https://arxiv.org/pdf/2604.25061v1)

## Abstract

Custom policy-learning pipelines in Spark fail for two coupled systems reasons: rowwise Python execution makes inference impractical, and driver-side candidate materialization makes split search fragile at feature scale. We present Spark Policy Toolkit, a semantics-governed systems toolkit for scalable policy learning in Spark. The toolkit provides two Spark-native primitives: partition-initialized vectorized inference through mapInPandas and mapInArrow, and collect-less split search that scores candidates on executors. Both primitives are governed by one fixed-input semantic contract: the same rows, feature order, treatment vocabulary, preprocessing manifest, and split boundaries must preserve per-row score vectors, best-split decisions, and end-to-end learned policy outputs. The evaluation combines practical baseline ladders, backend parity checks, measured split-search scale results, synthetic and Hillstrom end-to-end policy preservation, missingness stress, partition and order perturbation tests, quantile-boundary sensitivity, and a concrete adversarial failure catalog. On a 40-worker Databricks cluster, mapInArrow reaches 4.72M rows/s at 10M matched rows and 7.23M rows/s at 50M rows, while collect-less split search remains valid from F = 10 through F = 1000 with 124000 candidate rows, where the driver-collect baseline is intentionally skipped. Across 24 backend-ablation settings, mapInArrow wins 18 while mapInPandas wins 6, so the paper treats backend choice as workload-dependent rather than universal. Once the fixed-input lock is enforced, all six tested repartition/coalesce/shuffle perturbations preserve identical signatures; before lock, all six drift. The central result is not speed alone: throughput and collect-less execution are the mechanisms that let policy semantics survive at Spark scale.
