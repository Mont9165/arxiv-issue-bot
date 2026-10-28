# An EVM-Cosmos Bridge for Atomic, Semantic-Preserving Transfer of Environmental Tokens

- arXiv ID: `2610.37663v1`
- Authors: Sebastian Pandolfi, Guzmán Llambías, Laura González
- Published: 2026-10-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.37663v1) | [pdf](https://arxiv.org/pdf/2610.37663v1)

## Abstract

Transferring semantically typed tokens between heterogeneous blockchains (e.g. EVM and Cosmos ecosystems) raises two problems: semantic mixing, the loss of a token's domainspecific meaning in transit (e.g., CO2 removals issued under different methodologies), and atomicity despite divergent consensus and timing assumptions. We propose a bridge that addresses both. A deterministic indicator identity derived from cryptographic commitments, mirrored in class registries on both chains and checked at mint time, preventing semantic mixing by construction. For atomicity, we extend hash time-locked contracts (HTLCs) from two-party exchange to single-owner transfer with an automatic callback that burns the source escrow after a destination claim, and a protocol-minimum bounty that makes the fallback burn incentive-compatible even against adversarial senders. We machine-check the protocol's invariants with TLC (supply conservation fails without the rational-monitor assumption and holds with it) and validate a bidirectional prototype on Polygon and Neutron mainnets over Axelar GMP: fully automatic transfers with a median end-to-end latency of 97 s over 50 Polygon to Neutron transfers across 7 days (all completed by the on-chain automatic callback) and 93 s in the reverse direction, and semantic-validation overhead below 0.4% of messaging cost. We also document the integration failure modes of Cosmos originated messaging, whose dominant operational risk proves to be relay eligibility rather than latency.
