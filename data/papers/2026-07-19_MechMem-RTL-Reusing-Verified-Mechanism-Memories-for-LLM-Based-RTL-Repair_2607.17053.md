# MechMem-RTL: Reusing Verified Mechanism Memories for LLM-Based RTL Repair

- arXiv ID: `2607.17053v1`
- Authors: Mingyu Cheng, Junjie Gao, Jinhua Cui, Kuncai Zhong
- Published: 2026-07-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AR`
- Links: [abs](http://arxiv.org/abs/2607.17053v1) | [pdf](https://arxiv.org/pdf/2607.17053v1)

## Abstract

Large language models (LLMs) can automatically repair register-transfer-level (RTL) designs. However, fixing complex sequential logic errors requires reusing past debugging experience. Existing retrieval-augmented generation (RAG) relies on task-text similarity to provide this experience. This text-based approach often misguides the model because natural language poorly reflects cycle-level hardware execution semantics. To address this, we present MechMem-RTL, a repair framework that reuses verifier-confirmed repair records instead of text similarity. Each stored record strictly links trigger evidence, a diagnosed failure mechanism, a local repair action, preservation constraints, and a verification summary. For a new failure, MechMem-RTL injects a past record only when deterministic verifier evidence is strictly compatible with the stored trigger. Otherwise, the system uses only current verifier evidence. We evaluate MechMem-RTL on 48 public sequential RTL tasks across six repair models. With at most two repair attempts per task, MechMem-RTL successfully resolves 180 out of 288 task-model pairs, outperforming standard feedback repair (109 pairs) and task-similarity RAG (107 pairs).
