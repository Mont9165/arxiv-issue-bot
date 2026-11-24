# SignalCount: Approximate Counts with Structured and Semantic Predicates in Seconds

- arXiv ID: `2611.30779v1`
- Authors: Matteo Agius-D'Arrigo, Zachary Zelner, Harrison Ju, Rushab Munot
- Published: 2026-11-23
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.30779v1) | [pdf](https://arxiv.org/pdf/2611.30779v1)

## Abstract

Many applications store records with structured columns and a text document, and ask how many records in a filtered set meet a criterion that only a reader of the text can judge, such as "How many patients with type 2 diabetes, aged 40 to 70, stopped metformin because their blood sugar stayed high?" An interactive application needs this count in seconds, as the user types the criterion, to decide whether the matching set is worth materializing with a batch pipeline in which an LLM judges the records. Prior approximate query processing over such semantic predicates has an expensive model, the oracle, label a sample at query time, so every query waits for the oracle. We present SignalCount, a production system that answers COUNT queries with structured and semantic predicates and calls no oracle at query time, even for ad-hoc criteria. Its oracle is the production LLM judge, and the judge's logged verdicts calibrate, offline, the fast classifier that already runs in front of the judge. At query time, SignalCount counts the filtered set exactly and draws a uniform sample of at most 1,000 records in one columnar scan, scores the sample with the classifier, and multiplies the average calibrated probability by the exact count. Its 90% interval combines a sampling term with one-sided, rate-dependent margins for calibration error, fitted by split conformal prediction across tenants. In a multi-tenant production deployment, latency has a p99 of 3.8 s and stays flat as the filtered set grows beyond the sample. On tenants held out from fitting, the interval covers the count that the production pipeline returns in 92% of estimates, although estimates run about 15% high in aggregate, because a calibration nearly unbiased per record is still biased per criterion.
