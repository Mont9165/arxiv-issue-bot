# Tensor Algebraic Property Skeletons: Amplifying Property-Based Testing for AI Compilers

- arXiv ID: `2606.06747v1`
- Authors: Yuxin Qiu, Ben Limpanukorn, Seongmin Lee, Jiyuan Wang, Qian Zhang, Miryung Kim
- Published: 2026-06-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.06747v1) | [pdf](https://arxiv.org/pdf/2606.06747v1)

## Abstract

Deep learning (DL) compilers such as TVM and ONNX-MLIR lower tensor computation graphs into optimized executables for target backends. Testing these AI compilers has made substantial progress in generating well-formed inputs in the context of fuzzing; however, such generation alone does not catch semantic drifts from algebraic invariants that graph transformations and optimizations are expected to preserve. While tensor algebra has been studied for decades, it has not been transformed into executable property-based tests (PBTs) for DL compilers because doing so requires jointly constructing operators, inputs, and test oracles. The central challenge is no longer generating well-formed inputs for fuzzing DL compilers, but bootstrapping executable PBTs with such inputs and oracles based on tensor algebra.
  We realize this vision in Propilot, an LLM-driven agentic property-based testing framework for DL compilers with GPT 5.5. First, Propilot represents tensor algebra knowledge as reusable property skeletons, each coupled with operator constraints, shape and value rules, and oracle templates. Second, given a target compiler, Propilot instantiates these skeletons into executable PBTs by generating paired tensor computation graphs, concrete tensor inputs, and expected semantic relations as oracles. Next, to prevent generated tests from degenerating into invalid or uninformative PBTs, Propilot validates each PBT candidate before execution for applicability and safety. Validation feedback, execution results, and coverage signals guide subsequent generation.
  We evaluate Propilot on TVM with 212 operators and 20 property skeletons, generating 4,579 PBTs. Compared with direct LLM-based PBT generation, Propilot reduces redundancy by 49% and eliminates invalid tests through explicit property skeletons. This effectiveness translates into finding semantic errors and numerical discrepancies.
