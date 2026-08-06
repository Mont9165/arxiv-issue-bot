# A Unified Benchmark for Privacy-preserving Vector Search

- arXiv ID: `2608.01192v1`
- Authors: Anne-Marie Kermarrec, Rafael Pires, Mathis Randl, Martijn de Vos
- Published: 2026-08-02
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.DB`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2608.01192v1) | [pdf](https://arxiv.org/pdf/2608.01192v1)

## Abstract

Vector search powers semantic search, recommendation systems, and retrieval-augmented generation (RAG). By design, the service answering a query sees both the query embedding and, usually, the corpus against which it is matched. This is a privacy breach for both the user issuing the query and the owner of the corpus. A family of cryptographic schemes (e.g., SAP, EMVP, BNTM, Tip-toe) addresses that leak. However, as each scheme is published and evaluated on its own corpus, threat model, parameter choices, hardware, and metric conventions, the numbers cannot be compared directly. Consequently, a practitioner asking which one to deploy today has no defensible way to choose. We close that gap with a uniform experimental comparison, including a Plaintext baseline and four cryptographic backends running over the same workload, hardware, and metric definitions. Under that ruler, the schemes spread across a Pareto frontier in privacy, performance, and recall rather than imposing a flat penalty on performance. We find that the performance of SAP matches Plaintext, EMVP delivers cryptographic indistinguishability at a 4x throughput cost on CPU, BNTM adds malicious-server verifiability at a further 22x median-latency cost, and Tiptoe hides the cluster choice itself, but incurs a 190x per-query cost compared to Plaintext. GPU acceleration pays off for Plaintext and SAP but not for EMVP or BNTM. All our experiment artifacts are publicly available for reproducibility
