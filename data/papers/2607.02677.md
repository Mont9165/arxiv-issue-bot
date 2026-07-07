# SpendableStore: A UTXO-based Decentralized Data Store

- arXiv ID: `2607.02677v1`
- Authors: Yinan Zhou, Faisal Nawab
- Published: 2026-07-02
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.02677v1) | [pdf](https://arxiv.org/pdf/2607.02677v1)

## Abstract

The literature on blockchain-based databases is divided into permissioned blockchains and permissionless account-based blockchains. However, the former is not fully decentralized, and the latter suffers from challenges in scalability and practicality. We propose SpendableStore, a hybrid on/off-chain database that operates on top of permissionless UTXO-based blockchains as a novel approach to the problem of data decentralization. Our design integrates atomic data units into individual UTXOs to create a new blockchain concept called Spendable Data Objects that perform traditional CRUD operations. The integrity, immutability, and ownership of these Spendable Data Objects are safeguarded directly by the blockchain peer nodes, thus constraining the power of database administrators to achieve true data decentralization. We further support database transactions and propose an isolation mechanism called Future Now Snapshot Isolation to reason about transactional correctness in SpendableStore. We performed experiments on a major blockchain's Mainnet and observed up to 16x better throughput compared to a state-of-the-art blockchain-based database.
