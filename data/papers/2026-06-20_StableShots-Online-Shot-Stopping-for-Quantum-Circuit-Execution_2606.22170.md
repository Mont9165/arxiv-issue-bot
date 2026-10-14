# StableShots: Online Shot Stopping for Quantum Circuit Execution

- arXiv ID: `2606.22170v1`
- Authors: Giuseppe Bisicchia, Alessandro Bocci, Ernesto Pimentel, Antonio Brogi
- Published: 2026-06-20
- Primary category: `quant-ph`
- Categories: `quant-ph`, `cs.ET`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.22170v1) | [pdf](https://arxiv.org/pdf/2606.22170v1)

## Abstract

Quantum circuit execution estimates output distributions by repeated measurements, yet developers commonly choose a fixed shot budget before execution. This static choice is brittle: low budgets can under-sample the distribution, while high budgets waste measurements. In this paper, we present StableShots, a black-box online stopping rule for static quantum circuits. The method executes a fixed circuit in small batches, monitors the total-variation distance between cumulative empirical distributions, and stops after repeated evidence of local stability. We evaluate StableShots on 180 QSimBench traces spanning six circuit families, six sizes from 4 to 14 qubits, and five noisy IBM simulated backends. With validation-only calibration and 100 repeated backend-holdout splits, the selected configuration reaches TVD <= 0.05 on all held-out test evaluations with median 7,650 shots, whereas fixed-shot baselines either fail more often or spend substantially more shots.
