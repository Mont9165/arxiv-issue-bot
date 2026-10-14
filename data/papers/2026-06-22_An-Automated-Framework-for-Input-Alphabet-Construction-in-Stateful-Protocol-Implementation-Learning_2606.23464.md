# An Automated Framework for Input Alphabet Construction in Stateful Protocol Implementation Learning

- arXiv ID: `2606.23464v1`
- Authors: JiongHan Wang, WenChao Huang
- Published: 2026-06-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2606.23464v1) | [pdf](https://arxiv.org/pdf/2606.23464v1)

## Abstract

As a prevalent analytical technique for stateful protocol implementations, state machine learning suffers from a core bottleneck stemming from handcrafted input alphabets. Manual alphabet definition inherently limits the completeness of input exploration, making it difficult to capture anomalous non-conformant messages and consequently missing latent semantic defects.
  In this paper, we target automatic input alphabet generation to break the above limitation for state machine learning. We adopt large language models to parse protocol message layouts and produce candidate input symbols following structured mutation rules, which automatically covers valid and invalid message spaces and eliminates reliance on manual protocol expertise.
  Considering the rising overhead brought by continuously growing alphabets, we introduce a mini-batch incremental learning strategy to reuse existing learned automata when incorporating new alphabet entries. Comprehensive experiments on practical protocol stacks indicate our approach can reproduce existing security vulnerabilities and identify novel semantic bugs. A subset of these newly discovered issues has been confirmed and patched by developers, proving the practicability and effectiveness of our proposed method.
