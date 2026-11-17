# Live Noise Fingerprints for Quantum Program Analysis

- arXiv ID: `2611.19143v1`
- Authors: Avner Bensoussan, Karine Even-Mendoza, Debalina Banerjee, Elena Chachkarova, Sophie Fortz, Vasileios Klimis, Mohammad Reza Mousavi
- Published: 2026-11-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2611.19143v1) | [pdf](https://arxiv.org/pdf/2611.19143v1)

## Abstract

Quantum programs are probabilistic in nature, and noisy execution due to current imperfect hardware further complicates their analysis. In this paper, we study abstract semantics for analysing quantum programs under these conditions. We introduce noise fingerprints, compact descriptions of the observable effects of noise relative to a finite interface of input states and output measurements. We use them to define our abstract domain with respect to the concrete noise-related behaviour. We relate the concrete and abstract domains through a probabilistic Galois connection, extending the Galois-connection framework to distribution-valued interpretations. We study the resulting abstraction in terms of observational soundness, conciseness, efficiency, and ability to adapt to changing noise. We show that polynomial-size interfaces yield exponentially smaller fingerprints than full noise models while preserving the chosen observations, and that fingerprint distance characterises the largest observational discrepancy over the chosen interface. Further, we develop ChanShadow, which reuses noise fingerprints of commonly used short program fragments to analyse noisy execution of whole programs and provides a uniform finite-sample error bound. We construct working examples showing how fingerprints support program analysis. We evaluate fingerprint precision, representation cost, measurement requirements, and behaviour under noise drift. On a synthetic benchmark, fingerprints retain $(99 \pm 1)\%$ of the noise strength information of a full noise model. On simulated noise drift, reusing earlier measurements reduces the number of fresh measurement rounds needed to reach an error tolerance of $0.10$ by a factor of $2.3$ at $95\%$ confidence and by a factor of $27$ under the median-error criterion.
