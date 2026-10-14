# RepTran: Search-Based Repair of Transformer Models

- arXiv ID: `2607.11193v1`
- Authors: Yuta Ishimoto, Paolo Arcaini, Fuyuki Ishikawa, Masanari Kondo, Naoyasu Ubayashi, Yasutaka Kamei
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.11193v1) | [pdf](https://arxiv.org/pdf/2607.11193v1)

## Abstract

To ensure the overall quality of AI-enabled software, not only traditional software components but also AI components need to be tested and repaired. Among AI components, Transformer models are increasingly integrated into software systems, which makes their misbehaviors critical. Although prior work in the software engineering community has proposed deep neural network (DNN) repair methods, most overlook Transformer-specific structures. We propose RepTran, a search-based repair method for Transformer models. It targets their feed-forward networks (FFNs), which play a central role in the architecture. RepTran identifies suspicious weights by combining two types of scores: a variance-based neuron score and an existing bidirectional score. It then iteratively optimizes these weights using differential evolution. Our evaluation includes 18 fault benchmarks constructed from CIFAR-100 and Tiny-ImageNet. We compare RepTran against three baselines: random weight selection, Arachne (a state-of-the-art DNN repair method), and ArachneW, which enables Arachne to control the number of selected weights. RepTran achieved an average repair rate of 74.7%, statistically outperforming random selection and Arachne across all benchmarks. Effect size analysis revealed that RepTran achieved higher repair rates than ArachneW regardless of the number of selected weights. These results suggest that RepTran is effective for enhancing the reliability of AI-enabled software.
