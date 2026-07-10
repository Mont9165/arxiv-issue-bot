# REFORGE: A Method for Benchmarking LLMs' Reverse Engineering Capabilities in Decompiled Binary Function Naming

- arXiv ID: `2607.07738v1`
- Authors: Nicolas Koller, Andreas u. Schmidt
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.07738v1) | [pdf](https://arxiv.org/pdf/2607.07738v1)

## Abstract

Large language models (LLMs) are increasingly applied to reverse-engineering tasks, and recent threat-intelligence reporting shows them operating inside live offensive-security workflows. Claims about their capability, however, outpace our ability to measure it. Existing benchmarks for LLM-assisted binary analysis treat the construction of function-level ground truth as a solved pre-processing step and report accuracy without disclosing how many functions were reliably evaluable. We argue that the principal obstacle to fair evaluation is not model capability but the reliability of binary-to-source alignment under compiler optimization. This paper presents Reforge, a provenance-tracked pipeline that constructs function-level ground truth from C source through compilation, DWARF and syntactic extraction, alignment, and decompilation, and that operationalizes alignment uncertainty as an eight-gate confidence funnel with three-tier stratification. On a controlled micro-benchmark, high-confidence yield falls from 87.2% to 65.9% across optimization levels, and unpaired comparisons overstate optimization-induced performance decay through survivorship bias. A proof-of-concept evaluation of seven contemporary LLMs on function naming demonstrates the substrate and motivates uncertainty-aware benchmarking practice
