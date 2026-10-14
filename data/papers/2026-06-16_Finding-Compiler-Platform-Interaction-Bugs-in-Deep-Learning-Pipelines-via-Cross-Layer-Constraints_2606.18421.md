# Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints

- arXiv ID: `2606.18421v1`
- Authors: Yuxin Qiu, Jiyuan Wang, Ronak Badhe, Ben Limpanukorn, Miryung Kim, Qian Zhang
- Published: 2026-06-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.18421v1) | [pdf](https://arxiv.org/pdf/2606.18421v1)

## Abstract

The growing deployment of artificial intelligence (AI) necessitates robust deep learning (DL) compilers, such as TVM and ONNX-MLIR. These compilers take as input high-level AI models, lower them through multi-layer transformations, and specialize them to diverse hardware. Testing such compilers is uniquely challenging as correctness depends on implicit constraints embedded throughout the compilation stack. Existing testing approaches largely take type constraints to restrict input model generation and therefore emphasize type validation and monitor compilation crashes or coverage gains. This focus overlooks compiler-platform interaction bugs that arise from interleaved effects across compilation and execution environments.
  In this work, we propose a scalable, automated DL compiler testing framework for, in tandem, (1) finding compiler-platform interaction bugs and (2) enabling behavior equivalence partitioning. Our key insight is that these bugs are caused by violated assumptions arising from interactions across compilation passes and hardware platforms. Therefore, we move beyond constraining input generation and derive full-stack constraints. Our approach is three-fold. First, we design an automated approach to extract full-stack constraints that jointly guide model generation and characterize compilation behaviors. Second, we prioritize constraints that expose interaction-sensitive behaviors, so our generated models are capable of exercising deep compilation logic. Third, we enable behavior equivalence partitioning by automatically inserting assertions to monitor distinct compilation symptoms that coverage or pass/fail signals miss.
  We evaluated our tool, XCheck, on three widely-used DL compilers and found 2,034 bug-revealing cases, including memory overflows, integer overflows, and silent unexpected compilations that were rooted in compiler-platform interactions.
