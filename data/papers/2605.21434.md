# Agentic Model Checking

- arXiv ID: `2605.21434v1`
- Authors: Youcheng Sun, Jiawen Liu, Daniel Kroening, Jason Xue
- Published: 2026-05-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21434v1) | [pdf](https://arxiv.org/pdf/2605.21434v1)

## Abstract

Verifying LLM-generated systems code is hard: bugs are prevalent, formal specifications are missing, and safety contracts are encoded implicitly at call sites rather than enforced at function boundaries. We propose agentic model checking, a paradigm that couples LLM agents with a bounded model checking backend under the principle agents propose, solvers verify: agents handle tasks requiring semantic judgment (spec inference, check selection, counterexample classification, refinement proposal) while BMC discharges every soundness-relevant decision. The paradigm rests on three commitments. Specifications are inferred top-down from caller context in a restricted DSL that translates deterministically into the backend's assume/assert primitives, with optional functional-correctness clauses lifting verification from panic-freeness to behavioural faithfulness. Verification is compositional: each function is checked in isolation against its spec with callees replaced by postcondition-constrained stubs, so per-query cost scales with a single function's state space and refinements propagate automatically to callers. Counterexamples are not bug reports: they pass through a validation pipeline (reachability, callee feasibility, dynamic replay, realism audit) that distinguishes active in-tree crashes from latent public-API failures, while modelling artifacts drive a refinement loop rather than being suppressed. We instantiate the approach in BMC-Agent and evaluate it on LLM-generated kernel and compiler code in C and Rust alongside mature OSS-Fuzz-hardened libraries, confirming real defects, producing bounded clean verifications on heavily-fuzzed surfaces, and establishing functional equivalence on selected algorithmic functions.
