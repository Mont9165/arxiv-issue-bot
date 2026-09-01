# Agent-Driven Verification of Memory Safety for liblzma Decoder Components with VST

- arXiv ID: `2608.29716v1`
- Authors: Prokhor Shlyakhtun, Alexander Gryzlov, Vladimir Kukharenko, Vasilii Nesterov, Nikolai Vasiliev, Kirill Ziborov, Eugene Zolotarev, Alex Pokras
- Published: 2026-08-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29716v1) | [pdf](https://arxiv.org/pdf/2608.29716v1)

## Abstract

We report on the verification of memory safety for decoder components of liblzma, the compression library underlying xz-utils: the LZMA2 state machine, the LZMA1 decoder it controls, the outer decoding path, and the shared sliding-window dictionary. Built with the Verified Software Toolchain (VST), machine-checked body theorems establish memory safety and partial functional correctness. Across 27 completed body proofs, the largest covers lzma decode, whose 338 source lines expand to 1,934 lines of C after preprocessing; its proof comprises 183,268 lines of proof script over 775,768 lines of mechanically extracted goal statements. The verification exposed undefined behavior in raw LZMA1 zero-input handling, where range-decoder macros add zero to a null pointer and subtract two null pointers. Unlike similar work that synthesizes verified code, we verify pre-existing, production-scale C. AI agents complete proof goals and propose refinements; humans write and review models and specifications, and approve semantic changes; the Rocq kernel checks the proof terms. With agents constructing the proof scripts, the main engineering problems lay in translating and modeling production C, building a robust harness for driving Rocq, and providing feedback for proving agents. VST's assertion logic expressed every contract required by the development. We describe the pipeline, coordination mechanisms, and proof-engineering techniques that resolved these frictions.
