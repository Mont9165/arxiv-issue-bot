# Towards Safety-Aware Mutation Testing for Autonomous Driving Systems

- arXiv ID: `2606.26456v1`
- Authors: Donghwan Shin
- Published: 2026-06-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.26456v1) | [pdf](https://arxiv.org/pdf/2606.26456v1)

## Abstract

Simulation-based testing is essential for ensuring the safety of Autonomous Driving Systems (ADS), yet the community lacks a systematic criterion for determining when we can safely stop additional test scenario generation. Existing coverage metrics typically focus on individual component reliability or treat the ADS as a black box, failing to capture certain component interactions that cause most ADS accidents. While traditional mutation testing provides a falsifiable measure of test adequacy, directly porting code- and deep learning model-level mutations to the corresponding modules of ADS is insufficient.
  In this vision paper, we propose a paradigm shift toward Safety-Aware Mutation Testing (SAMT). Unlike traditional mutation testing, which creates mutants (i.e., faulty versions of the software under test) by injecting artificial faults into individual components, SAMT systematically injects temporally bounded faults into the messages exchanged between ADS modules to simulate realistic interaction failures. To ensure these mutants represent genuine hazards, we propose deriving mutant generation rules directly from top-down safety engineering frameworks, such as System-Theoretic Process Analysis (STPA). By embedding systems thinking into the mutation testing pipeline, SAMT provides a rigorous mechanism for evaluating test adequacy, enabling automated scenario generation, and guiding ADS repair. We also outline critical open challenges.
