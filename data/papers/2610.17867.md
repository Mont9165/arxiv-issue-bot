# RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions

- arXiv ID: `2610.17867v1`
- Authors: Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal, Charilaos Kanatsoulis, Roshan Upendra, Tom Palczewski, Carlos Guestrin, Jure Leskovec
- Published: 2026-10-13
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.17867v1) | [pdf](https://arxiv.org/pdf/2610.17867v1)

## Abstract

Foundation models for tables and relational databases are increasingly used for predictive tasks across various scientific and industrial domains. However, adapting existing models to unseen datasets requires tens of thousands of examples. Here we introduce RT-J, an 85M-parameter relational foundation model (RFM) that makes accurate predictions even with hundreds of in-context examples or fewer. To achieve this, we first assemble the Join, a large collection of 639 web-crawled databases with 6,023 LLM-generated forecasting tasks. We pretrain with long contexts of up to 8,192 database cells, using in-context examples from a novel lightweight random-walk retriever. Finally, we leverage context tuning and ensembling to scale up test-time compute. On in-context regression tasks from RelBench, RT-J requires 10x fewer examples on average to match strong feature engineering pipelines with LLM-agent or RDBLearn featurizers and TabICLv2 or LightGBM predictors. Overall, our work pushes the frontier for context-efficient predictions on relational data and highlights the importance of real-world semantics, context engineering and large-scale pretraining for RFMs.
