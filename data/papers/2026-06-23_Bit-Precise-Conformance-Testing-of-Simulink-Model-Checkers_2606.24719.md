# Bit-Precise Conformance Testing of Simulink Model Checkers

- arXiv ID: `2606.24719v1`
- Authors: Daisuke Ishii, Takashi Tomita, Toshiaki Aoki, Hideaki Takai
- Published: 2026-06-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.24719v1) | [pdf](https://arxiv.org/pdf/2606.24719v1)

## Abstract

MATLAB/Simulink provides a practical modeling language and a simulation engine for the development of cyber-physical systems. To ensure the quality of the developed models, there are formal verification tools available, such as Simulink Design Verifier (SLDV) and third-party SMT-based model checkers (SmtMC). However, due to the absence of a semantics of Simulink that covers every element of models and the details of its numerical behavior, the reliability of the model checkers themselves is often doubtful, potentially analyzing models differently from the simulator. This work aims to verify the quality of the Simulink model checkers by addressing the following items. 1) Formalization of the basic block types of Simulink. It involves defining block type feature sets and the bit-precise behavior of the blocks. 2) A method for testing bit-precise conformance relations among the tools for each block type. The pass rate of our test suites measures (i) conformance of model checking results with simulation results by Simulink and (ii) conformance between the results of SmtMC and SLDV. 3) Experiment to perform tests on 10 block types. We confirmed that SmtMC efficiently passed all test cases, while SLDV achieved pass rates of only 94-96% and 80-90% for conformance (i) and (ii), respectively. We analyzed the causes of failed tests, such as errors, corner cases, and timeouts.
