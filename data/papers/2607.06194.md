# Claimed or Attested? A Commit-Signature Dataset and Identity Trust Tiers across the World of Code

- arXiv ID: `2607.06194v1`
- Authors: Audris Mockus
- Published: 2026-07-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06194v1) | [pdf](https://arxiv.org/pdf/2607.06194v1)

## Abstract

An author string in a git commit is free text the committer typed, so identity resolution over a global commit corpus rests on a claim that nothing in the commit verifies. A cryptographically signed commit is different: it binds the commit to a key the committer controls, and when that key ties back to a real-world identity the git identity becomes attested rather than merely claimed. We release the first commit-signature axis for the World of Code (WoC), extracted for the V2604 collection. The signature travels in the commit object's gpgsig header and is already carried, unparsed, in the commit-message field of the WoC commit tables, so the axis is a scan over existing tables rather than a re-read of the object database. Over the V2604 corpus of 5,866,595,698 commits, 17.59% carry a signature (PGP dominant at 98.96%, with a growing minority of SSH and X.509/sigstore signatures), or 1,031,721,316 signed commits. We release the per-commit signature map c2sigFull, a key-to-author graph gated so that shared organization and continuous-integration keys are separated from person keys, and A2trust, a per-identity attestation tier (unsigned, signed, real-world-bound, cross-corpus attested) that extends the published A2cls identity-class dataset. The signature axis is a precision anchor, not a coverage layer: signed commits skew toward recent and security-conscious developers, a population that overlaps the scholarly authors a bibliography join targets. We use the person keys to build a cryptographically grounded alias gold that calibrates the heuristic WoC alias map independently of hand-labeled pairs, and to attach an attestation provenance to science-to-software identity links. All artifacts are released as a self-contained, in dependently hosted replication package keyed to the WoC V2604 collection.
