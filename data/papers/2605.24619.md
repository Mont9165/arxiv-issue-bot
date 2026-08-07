# Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models

- arXiv ID: `2605.24619v1`
- Authors: Weining Cao, Guangyuan Wu, Yuan Yao, Hengfeng Wei, Taolue Chen, Xiaoxing Ma
- Published: 2026-05-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.24619v1) | [pdf](https://arxiv.org/pdf/2605.24619v1)

## Abstract

Distributed protocols are notoriously difficult to verify correctly. Proving safety typically requires inductive invariants that both imply the desired property and are preserved by every protocol transition; yet inferring such invariants remains a major bottleneck: existing approaches either restrict the protocol models to a decidable fragment of first-order logic or demand expert-crafted templates.
  We present IC3Syn, a neuro-symbolic framework that synthesizes inductive invariants by executing an IC3-style process over TLA+ states with the assistance of Large Language Models (LLMs). At large, IC3Syn combines a symbolic IC3 controller, which decomposes invariant synthesis into focused blocking tasks and an LLM which provides protocol-level reasoning that IC3 alone lacks for TLA+ specifications. This integration enables a disciplined yet flexible search for invariants without imposing logical restrictions or requiring manual templates.
  We evaluate IC3Syn on 29 distributed protocols spanning consensus, reconfiguration and client-server systems, and compare it against Endive, IC3PO, SWISS and DistAI. IC3Syn discovers candidate invariants for all 29 protocols, including MongoLoglessDynamicRaft (MLDR), an industrial-scale Raft-based reconfiguration protocol for which none of the compared tools reports a solution, as well as one complex Paxos variant. In each case, the invariants synthesized on finite instances are shown in TLAPS to be inductive for the full unbounded protocol, thereby establishing safety.
