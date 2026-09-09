# Recompilation Is Not Enough: Test-Guided Decompiled-C Repair

- arXiv ID: `2609.07201v1`
- Authors: Yuhan Huang, Puzhuo Liu, Jianlei Chi
- Published: 2026-09-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.07201v1) | [pdf](https://arxiv.org/pdf/2609.07201v1)

## Abstract

Decompiled C often becomes recompilable only after repair, but recompilation alone does not establish test-observed behavior. A recompiled command-line binary can still parse options incorrectly, print different bytes, or return a different exit status. We present a few-step workflow for repairing decompiled C using compiler feedback and related official tests. Compiler and linker diagnostics first guide build repair. Once the repaired C recompiles into a binary, smoke checks and related official tests expose behavioral discrepancies for semantic repair. In a preliminary static-enriched evaluation on 104 Coreutils 9.5 binaries with available decompiler exports and deterministic exact-output smoke comparisons, 91 binaries (87.5%) recompile and pass the test gate; 9 do not recompile within the repair budget, and 4 recompile but still fail the test gate. The result suggests that test-gate feedback can make LLM-assisted repair of decompiled C more auditable than compile-only recovery.
