# GraphDroid: Asynchronous LLM-Based Mobile App GUI Testing via History-Aware Exploration and Hybrid Intent Fulfillment

- arXiv ID: `2609.10031v1`
- Authors: Xiaolei Li, Jialun Cao, Zhijian Hou, Yuzhi Zhao, Yepang Liu, Shing-Chi Cheung
- Published: 2026-09-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.10031v1) | [pdf](https://arxiv.org/pdf/2609.10031v1)

## Abstract

Automated GUI testing is a widely adopted technique for ensuring mobile application quality by simulating user interactions to exercise functionalities. Despite the research breakthroughs in the past decades, covering complex functionalities that require multi-step action sequences still remains challenging. Traditional tools lack semantic understanding capability and can rarely synthesize such action sequences. Recent LLM-based tools can generate test intents describing target functionalities and leverage the LLM to fulfill the intents, but suffer from three key limitations: 1) loss of historical context for identifying uncovered functionalities, 2) synchronous intent generation that blocks exploration, and 3) per-step LLM-driven fulfillment incurring high cost and latency. To address these limitations, we propose GraphDroid, an intent-driven GUI testing framework that integrates a cluster-based memory mechanism to effectively identify uncovered functionalities from historically visited states for comprehensive application testing. For improving testing efficiency, GraphDroid adopts an asynchronous intent generation paradigm that eliminates the latency bottleneck and a hybrid intent fulfillment strategy that reserves the LLM for fulfilling complex intents while delegating simple intents to a lightweight heuristic algorithm. We evaluate GraphDroid on 41 real-world Android apps against six state-of-the-art baselines. Results show that GraphDroid outperforms all baselines, achieving up to 36.4% higher code coverage while incurring less than one eighth of the cost of the best pure LLM-based baseline. GraphDroid also exposes 19 bugs in the 41 apps and detects 13 of 52 crashes in the Themis bug benchmark, surpassing all the six baselines. Seven of the 19 bugs were previously unknown and we reported them to the developers. So far, four bugs have been confirmed and fixed.
