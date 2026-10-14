# Provably Lossless Acceleration of DNN Mutation Testing via Memoization

- arXiv ID: `2607.18582v1`
- Authors: Ali Ghanbari, Ben Greenman, Sasan Tavakkol, Shibbir Ahmed
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.18582v1) | [pdf](https://arxiv.org/pdf/2607.18582v1)

## Abstract

Mutation analysis has recently reemerged in the context of deep neural networks (DNNs) as a promising, but notoriously costly, approach for assessing test dataset adequacy. Existing techniques speed up DNN mutation testing through lossy approximations that trade efficiency for mutation score accuracy. This paper introduces Mure, the first provably lossless framework for accelerating DNN mutation testing via memoization. Mure is based on the idea that DNN mutants and the original model share substantial redundant computation, so during mutation testing, it executes only the mutated suffixes of each mutant and reuses the common prefix from the original model, which is computed only once. We give a formal account of memoized mutation testing, and prove that Mure is sound, i.e., it produces results equivalent to exhaustive vanilla mutation testing, and identify basic conditions under which speed-up is guaranteed. We have implemented Mure and evaluated it on 15 DNN models of various architectures, complexities, and sizes ranging from a few thousands to millions of parameters. This provides empirical evidence that Mure reduces the computational cost of mutation testing by 44.54%, on average. We also observed that while state-of-the-art techniques tend to yield higher acceleration (up to 88.97%, on average), they come at the cost of some error in mutation score. We further analyze the effect of mutation generation selection ratio on the effectiveness of Mure and observed predictable reductions in memoization opportunities with increasing the percentage of mutated neurons. We observed that Mure offers more than 20% speed-up even when as high as 5% of the neurons are mutated.
