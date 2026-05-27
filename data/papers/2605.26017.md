# Trustworthy Software Project Generation : a Case Study with an Interactive Theorem Prover

- arXiv ID: `2605.26017v1`
- Authors: Jian Fang, Yingfei Xiong
- Published: 2026-05-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.26017v1) | [pdf](https://arxiv.org/pdf/2605.26017v1)

## Abstract

Generating code from natural-language requirements has become a primary route for LLM-assisted software development. Although LLMs can successfully complete small programming tasks, generating an entire complex project remains unreliable because subtle errors may survive compilation and testing. Verified programming can reduce this risk by requiring generated implementations to satisfy machine-checked specifications. Existing explorations mostly target verification-oriented languages and toolchains such as Dafny and Frama-C, but directly generating project-scale verified code with these systems remains difficult. This paper studies whether interactive theorem provers (ITPs) can support large-scale software generation. Because ITPs handle pure total functions but not effects such as I/O, our agent separates effectful code from pure logic: it implements the effects in the target language, proves the pure logic in an ITP, and extracts it for integration into the final project. We study this route through the fully automatic development of a CPU interpreter for all 47 instructions of the unprivileged RISC-V RV32I base: after the requirements are supplied, no human intervenes in synthesis, proof repair, extraction, or integration. With Rocq as the backend, the agent completes the project within 30 minutes, producing 1,859 lines of verified Rocq and extracting 2,848 lines of C++. The resulting interpreter passes all 265 LLM-generated tests covering the 47 instructions and exhibits zero crashes and zero hangs during 12 hours of AFL++ fuzzing. Under the same configuration, a Dafny-based backend fails to complete verification. Our observation is that Rocq exposes a concrete proof state when a proof attempt fails, giving the agent actionable feedback for repair. These results provide empirical evidence that ITP-based verified programming is a feasible route for LLM-generated software projects.
