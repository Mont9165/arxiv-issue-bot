# LLM-Assisted Automatic Security Proofs for Cryptographic Protocols: How Far Are We?

- arXiv ID: `2609.35434v1`
- Authors: Tianjian Liu, Shicheng Feng, Jin'ao Shang, Xiaoting Lyu, Bin Wang, Zonghua Zhang, Lei Xue, Wei Wang
- Published: 2026-09-28
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.35434v1) | [pdf](https://arxiv.org/pdf/2609.35434v1)

## Abstract

Large language models (LLMs) have shown strong potential for assisting software and security analysis tasks, yet their effectiveness in cryptographic symbolic protocol verification remains insufficiently understood.
  In this paper, we conduct the first systematic evaluation of the capability of state-of-the-art LLMs in cryptographic symbolic protocol verification. To quantify this capability, we propose \textsc{CRoST} (Coverage Rate of Solve Tree), a proof-based metric derived from the verifier's proof skeleton that measures the similarity between generated lemmas and reference lemmas. We then establish the rationale of \textsc{CRoST} through both theoretical analysis and empirical validation. The evaluation results show that state-of-the-art models achieve 38.82\% coverage on average, with 14.4\% of generated lemmas exceeding 80\% coverage, indicating that LLMs can already generate useful lemmas to a certain extent. However, they still exhibit non-trivial failure modes on complex multi-phase protocols, show diminishing returns under naive scaling, and incur substantial verification overhead. These findings clarify the practical potential and limitations of LLMs for protocol verification and motivate future work on complex real-world protocols.
