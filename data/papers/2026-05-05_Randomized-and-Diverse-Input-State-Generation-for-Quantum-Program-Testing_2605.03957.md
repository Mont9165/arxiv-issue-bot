# Randomized and Diverse Input State Generation for Quantum Program Testing

- arXiv ID: `2605.03957v1`
- Authors: Maryse Ernzer, Seung Yeob Shin, Fabrizio Pastore, Domenico Bianculli
- Published: 2026-05-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03957v1) | [pdf](https://arxiv.org/pdf/2605.03957v1)

## Abstract

With the accelerating development of quantum technologies and their growing computational potential, quantum systems are being adapted for simulations and other critical tasks across diverse domains, making the reliability of the corresponding quantum software an essential concern. Although recent efforts have started to incorporate quantum-specific properties such as magnitude, phase, and entanglement under the form of input-coverage criteria into software testing, the unique structure of the quantum state space demands for more comprehensive testing. In particular, the notion of complete state-space exploration has so far received little attention.
  To address this gap, we propose a framework for evaluating test circuit generators with respect to their coverage of the quantum state space. Our contribution is threefold: we develop a set of diversity scores that capture both local and global indicators of the extent to which the state space is explored; we propose a test circuit generator that produces test input states via a Brick-Circuit (BC) construction designed to approximate ideal random states using hardware-compatible gates; we compare the proposed construction with existing generators based on their ability to generate uniformly distributed random test input states.
  Our extended diversity scores quantify the local correlations and global spread of magnitude, phase and entanglement. Using these scores, we evaluate the expressibility, defined as the capability to span the quantum state space uniformly, and entangling capabilities of existing generators relative to the BC generator. Our results show that the hardware-compatible BC generator achieves higher expressibility and entanglement performance at shallower depths than existing circuit generators.
