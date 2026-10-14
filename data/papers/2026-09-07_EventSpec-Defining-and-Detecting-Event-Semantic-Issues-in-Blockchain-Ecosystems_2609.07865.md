# EventSpec: Defining and Detecting Event-Semantic Issues in Blockchain Ecosystems

- arXiv ID: `2609.07865v1`
- Authors: Yixuan Liu, Yuxin Dong, Ye Liu, Yin Wu, Chengxuan Zhang, Xiapu Luo, Yi Li
- Published: 2026-09-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.07865v1) | [pdf](https://arxiv.org/pdf/2609.07865v1)

## Abstract

In recent years, smart contracts have become the backbone of decentralized applications (DApps), and off-chain systems such as bridges, wallets, and indexers rely heavily on event logs to track contract execution and state changes. However, the Ethereum Virtual Machine (EVM) does not validate or enforce event semantics, so logs can diverge from on-chain state, misleading off-chain systems into accepting incorrect state transitions. Existing smart contract vulnerability detection tools focus on logic bugs, with limited support for detecting event-semantic defects. To address this gap, we collect audit reports and incident cases and apply open card sorting to define five classes of event-semantic defects: event collision, state-event mismatch, unauthorized event emission, event emission mismatch, and event parameter mismatch. We propose EventSpec, which infers event specifications from a contract corpus via behavior inference and semantic-constraint extraction and applies differential checking to identify event-semantic defects in target contracts. We run EventSpec on 6,617 real-world contracts and evaluate detection effectiveness based on manually labeled results; EventSpec achieves an overall comprehensive precision of 90.17%. We further provide an off-chain evaluation harness that reproduces two off-chain attack vectors on any EVM-compatible chain: event origin confusion caused by unintended emitters and event-state desynchronization where events lack matching state updates. Using this harness, we demonstrate the feasibility of these attacks on bridge relayers, blockchain explorers, and NFT marketplaces, and report six wallet issues, four of which were confirmed (including a $600 bounty), with two remaining pending.
