# Robust Mutation Analysis of Quantum Programs Under Noise

- arXiv ID: `2605.13279v1`
- Authors: Sophie Fortz, Eñaut Mendiluze Usandizaga, Shaukat Ali, Paolo Arcaini, Mohammad Reza Mousavi
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.13279v1) | [pdf](https://arxiv.org/pdf/2605.13279v1)

## Abstract

Mutation analysis has long been used in classical software testing and has recently been adopted for assessing the robustness of quantum software testing techniques. However, existing studies assume ideal, noiseless execution, overlooking the impact of quantum hardware noise. In this paper, we present an empirical study of noise-aware mutation analysis for quantum programs. We analyze how noise affects mutant detection using 41 quantum programs, executed on noiseless and noisy simulators emulating three IBM devices with different noise profiles. We compare several distance metrics and thresholding strategies to evaluate mutant detection under realistic noise. Our results show that noise significantly alters the behavioral distance between programs and mutants, making equivalent mutants harder to distinguish from real faults. Density-matrix metrics achieve the best discrimination, with misclassification rates up to 16.77%, but are not accessible on real hardware. Among practical alternatives, output-distribution metrics reach up to 73.03% accuracy and 74.89% F1-score. Noise-specific thresholds further improve detection compared to noiseless thresholds. We also find that noise effects correlate more with algorithm and circuit characteristics than with mutation types. Overall, our results highlight the need to adapt mutation analysis, and more generally quantum program comparison, to the noise profiles of target quantum devices.
