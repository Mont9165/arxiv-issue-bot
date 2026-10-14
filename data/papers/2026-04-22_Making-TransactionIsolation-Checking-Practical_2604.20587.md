# Making TransactionIsolation Checking Practical

- arXiv ID: `2604.20587v1`
- Authors: Jian Zhang, Shuai Mu, Cheng Tan
- Published: 2026-04-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.20587v1) | [pdf](https://arxiv.org/pdf/2604.20587v1)

## Abstract

Checking whether database transactions adhere to isolation levels is a crucial yet challenging problem. We present Boomslang, the first general-purpose checking framework capable of verifying configurations that were previously uncheckable. Boomslang advances beyond prior work in three key aspects: (1) it supports arbitrary operation types provided by modern transactional key-value stores, (2) it requires no knowledge of database internals, and (3) it offers a modular, extensible pipeline amenable to customization and optimizations.
  Boomslang adopts a front-/back-end separation. As the front-end, it parses a database trace into an Abstract Semantic Graph, which is then lowered -- via semantic analysis -- into a low-level intermediate representation (IR). The back-end converts this IR to a set of constraints for SMT solving. This design is enabled by a key abstraction in the IR, called superpositions, which capture the uncertainty and complexity caused by arbitrary operations and missing information. Our experiments show that with just 271--386 lines of code, the core logic of three prior checkers can be reimplemented as Boomslang modules, achieving comparable or superior performance. Using Boomslang, we also identify a new bug in TiDB, audit the metadata layer of the JuiceFS file system, check vendor-specific behavior in MariaDB, support five previously unchecked isolation levels, and confirm a theoretical result on the correctness of strict serializability.
