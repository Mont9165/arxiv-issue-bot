# RosettaBitcoin: An Artifact-Backed Experience Report on Verification Infrastructure for Agent-Assisted Consensus Validators

- arXiv ID: `2609.01702v1`
- Authors: Donavon Guyot
- Published: 2026-09-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.01702v1) | [pdf](https://arxiv.org/pdf/2609.01702v1)

## Abstract

Agent-assisted software projects are often reported through demonstrations or aggregate benchmarks that conceal how correctness claims were admitted. This experience report studies RosettaBitcoin, a single-developer project that built twelve separately implemented Bitcoin testnet4 consensus validators, through its immutable 17 June 2026 software snapshot (DOI 10.5281/zenodo.20738249). We analyze the snapshot's tracked SQLite evidence database, curated artifact index, conformance fixtures, validation scripts, blocker records, and version history. At the snapshot, all twelve ports had port-owned 45/45 script-corpus proofs and strict 5,000-block baselines. Nine had canonical clean 50,000-block, 100,000-block, and post-100,000 validation lanes. Java had one 19.86-second near-tip maintenance artifact. No port had an empty-state-to-tip proof, and no port satisfied the project's binary full-node gate; Docker and live-node capability gaps remained.
  The artifact history also records a 3 h 17 min 57 s Zig scaffold-to-50,000 span, but the observed intervals describe non-equivalent tasks and cannot estimate effort, productivity, or causality. A separate diagnostic supplement preserves evidence that a pure-Mojo cryptographic backend validated fresh state to height 100,000 and resumed to 140,234, agreed on a 45-case shadow comparison, rejected six crafted invalid classes, and was killed by three targeted mutations. That evidence is noncanonical, noncomparable, and class-bounded. The case suggests that explicit failure records, fixtures, port-owned proofs, and validating imports can make agent-assisted systems more auditable. Controlled ablations and external replications are needed to test whether such infrastructure causally improves development outcomes.
