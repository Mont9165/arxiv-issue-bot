# Boosting Automatic Java-to-Cangjie Translation with Multi-Stage LLM Training and Error Repair

- arXiv ID: `2605.07403v1`
- Authors: Xinyue Liang, Jingxuan Zhang, Lin Li, Jun Zhang, Junhao Chen
- Published: 2026-05-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.07403v1) | [pdf](https://arxiv.org/pdf/2605.07403v1)

## Abstract

With the rapid evolution of emerging programming language ecosystems, the demand for code translation to low-resource languages continues to grow. As Cangjie emerges as a new programming language, its ecosystem and development toolchains are rapidly expanding. Automated translation from popular programming languages to Cangjie is therefore valuable for practical development. However, constrained by both insufficient Cangjie knowledge and scarce parallel code corpora, general Large Language Models (LLMs) are prone to syntactic errors and semantic as well as structural misalignment in code translation. Existing approaches typically rely on fine-tuning with large-scale parallel data, but they cannot reliably improve compilability or semantic consistency for low-resource Cangjie languages. To tackle these challenges, we propose a multi-stage training framework of LLMs that employs the iterative error repair technique to translate Java code into Cangjie code. This training framework performs training on LLMs, gradually integrating knowledge and achieving semantic alignment as well as structure awareness. During the code translation, we also combine the compiler feedback and error repair case retrieval to repair the incorrect Cangjie code. We construct syntactic knowledge and monolingual instruction datasets to train the LLM. In addition, we also build a Cangjie error repair repository to support error repair in our approach. Experimental results show that, with limited parallel data, our approach improves functional equivalence by 6.06\% compared to the state-of-the-art approaches. Meanwhile, ablation studies confirm that each training stage positively contributes to the final performance.
