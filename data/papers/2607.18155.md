# Testing Retrieval-Augmented Generation Systems with Chunk Coverage

- arXiv ID: `2607.18155v1`
- Authors: Jinhan Kim, Samuele Pasini, Paolo Tonella
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.18155v1) | [pdf](https://arxiv.org/pdf/2607.18155v1)

## Abstract

Retrieval-Augmented Generation (RAG)-based systems\footnote{For brevity, RAG-based systems are referred to as RAG systems throughout this paper.} are increasingly deployed in high-stakes settings where correct behaviour depends not only on the language model but also on the retrieval component that selects external documents at inference time. While existing RAG evaluation metrics assess retrieval and generation quality on a per-query basis, typically relying on query-level test oracles such as reference answers or relevance annotations, they provide limited insight into whether a test suite adequately exercises the retrieval behaviour of the system as a whole. In this paper, we introduce Chunk Coverage (CC), an oracle-independent test adequacy criterion for testing the retrieval component of RAG systems. CC measures the fraction of corpus chunks that are retrieved at least once across a test suite, providing a structural view of which parts of the retrieval space have been exercised. We further show how CC can be used to guide test selection and generation by prioritising queries that expand coverage of previously unexercised retrieval regions. We evaluate CC on clinical and financial RAG system scenarios. CC-guided testing reaches 50% of attainable coverage 1.7x faster than random selection and 4.2x faster than redundancy-biased strategies. Moreover, CC improves fault detection effectiveness (APFD) by 10% to 25% over random, indicating earlier discovery of distinct retrieval faults. These results show that CC captures retrieval diversity relevant to effective testing without requiring test oracles.
