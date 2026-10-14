# Understanding Verification Vulnerabilities in Cross-chain Bridges: An Empirical Study

- arXiv ID: `2610.13170v1`
- Authors: Yuying Wang, Yi Guo, Jiachi Chen, Hanwen Zhang, Yi Sun
- Published: 2026-10-09
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.13170v1) | [pdf](https://arxiv.org/pdf/2610.13170v1)

## Abstract

With the rapid development of blockchain technology, numerous heterogeneous blockchains have emerged, each featuring distinct architectures, consensus mechanisms, and application ecosystems. Cross-chain bridges have consequently become a critical infrastructure component, typically relying on smart contracts to facilitate message passing and asset transfers across heterogeneous blockchains. Unlike single-chain contracts, bridge contracts introduce additional verification logic to validate external-chain data, such as state proofs, message sender identities, and signatures. However, correctly implementing such logic is challenging. We refer to vulnerabilities that violate the security guarantees of cross-chain verification as Cross-chain Verification Vulnerabilities (CVVs). To characterize CVVs, we conduct the first systematic empirical study of this vulnerability class. By analyzing 588 security audit reports from 36 real-world cross-chain bridge projects, we derive 11 CVV patterns and organize them into 5 high-level categories according to the affected verification properties. Following this taxonomy, we construct a CVV dataset containing 830 vulnerability instances across 786 contract files. The dataset establishes mappings among audit reports, audited source-code versions, affected source files, and CVV-pattern labels. We then assess existing detection approaches. Current tools provide limited documented coverage of CVV patterns, while only two of four evaluated LLMs outperform an all-pattern constant baseline of 29.3% Macro-F1; the best reaches 51.2%. Together, the limited tool coverage and inconsistent LLM gains motivate detection methods tailored to cross-chain verification semantics.
