# Probabilistic Condition, Decision and Path Coverage of Circuit-based Quantum Programs

- arXiv ID: `2604.26609v1`
- Authors: Daniel Fortunato, José Campos, Rui Abreu
- Published: 2026-04-29
- Primary category: `quant-ph`
- Categories: `quant-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26609v1) | [pdf](https://arxiv.org/pdf/2604.26609v1)

## Abstract

Coverage criteria play a central role in assessing test adequacy in classical software, yet their effectiveness for quantum programs remains poorly understood and largely unexplored. In this paper, we propose six quantum-tailored criteria - condition, decision, and path coverage, and their probabilistic variants - adapted from their classical counterparts. We present QaCoCo, a tool that computes these criteria for circuit-based quantum programs. We empirically evaluate these criteria on a large and diverse set of 540 circuits and analyze the coverage achieved. Our results show that while circuits frequently achieve high condition and decision coverage (97.56% and 97.63%, on average), path coverage remains limited (71.84%), particularly in the presence of multi-controlled gates, which induce extreme path explosion and coverage imbalance. Moreover, to account for the probabilistic nature of quantum circuits, we introduce probabilistic coverage, which augments structural coverage with a confidence measure (88.87%, 88.65%, and 37.18% for condition, decision, and path coverage, respectively, on average). Finally, through mutation testing, we find weak or no correlation between fault detection and structural coverage, consistent with observations in classical computing.
