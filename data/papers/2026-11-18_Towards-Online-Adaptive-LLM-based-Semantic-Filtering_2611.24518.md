# Towards Online Adaptive LLM-based Semantic Filtering

- arXiv ID: `2611.24518v1`
- Authors: Ziqi Zou, Zhenyan Nie, Kangfei Zhao, Zhiwei Zhang, Aoqian Zhang, Peng Wu, Xuefeng Zhao
- Published: 2026-11-18
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.24518v1) | [pdf](https://arxiv.org/pdf/2611.24518v1)

## Abstract

Large language models (LLMs) enable semantic filtering over unstructured documents using natural language predicates, but invoking an oracle LLM on every document incurs prohibitive monetary cost and online latency. Existing model-cascade approaches reduce this cost by using a lightweight proxy model to score each document and forwarding only uncertain documents to the oracle. However, their proxy models have limited generalization capability, and they typically adopt fixed sampling budgets for proxy training and threshold calibration, which insufficiently adapts to diverse online queries. To address this, we present OASIS, an online adaptive framework for LLM-based semantic filtering. OASIS combines a query-agnostic document similarity prior with query-adaptive online learning and sampling. In the offline phase, OASIS utilizes query-agnostic document similarity as a prior and constructs a document navigating spread-out graph (NSG) over document embeddings. For each online query, OASIS trains a query-conditioned graph attention network over the document NSG to obtain proxy scores through semi-supervised node classification. To allocate labels effectively, OASIS adopts density-aware active learning to explore uncertain score regions, selectively annotate informative documents, retrain the proxy, and stop early when additional labels are unlikely to improve the cascade. During threshold calibration, OASIS progressively samples an adaptively sized calibration set, adapting calibration cost to the query's score distribution. Extensive experiments demonstrate that OASIS achieves a 1.75x-5.42x reduction in online latency and reduces the number of LLM-processed documents by 35%-75% relative to the state-of-the-art methods at an achieved accuracy of 0.9.
