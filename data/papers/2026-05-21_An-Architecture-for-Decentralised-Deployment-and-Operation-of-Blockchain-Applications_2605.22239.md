# An Architecture for Decentralised Deployment and Operation of Blockchain Applications

- arXiv ID: `2605.22239v1`
- Authors: Fabian Stiehle, Kirill Inozemtsev, Ingo Weber
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.22239v1) | [pdf](https://arxiv.org/pdf/2605.22239v1)

## Abstract

Blockchains and distributed ledger technologies allow the operation of manifold decentralised applications (dApps). Such applications are based on smart contracts, a programmable abstraction that is executed in a decentralised manner. To ensure the correctness of smart contracts, blockchain application developers rely on DevOps practices such as automated testing and continuous integration and deployment. However, such infrastructure is often controlled by single entities. For larger blockchain applications, this issue is resolved by relying on concepts of Decentralised Autonomous Organisations (DAOs), which allow proposals to be autonomously executed once they reach a pre-defined quorum. Such a governance architecture is complex and requires integration with existing patterns for contract discovery and upgradeability. In this paper we integrate these concepts considering DevOps best-practices into a novel architecture that remains agnostic to different governance and upgrade implementations. We extend the known registry pattern to support deterministic deployments and present a decentralised deployment framework, including integration and deployment pipelines, user-interfaces, and version control integration. In our approach, each party implements and verifies their own tests before engaging in the use of a (newly deployed) smart contract. We provide a reference implementation, available as open-source, and evaluate the proposal thoroughly. Our architecture can serve as a reference for future integrations, while our open-source framework is aimed at reducing the complexity of adopting such a process in practice.
