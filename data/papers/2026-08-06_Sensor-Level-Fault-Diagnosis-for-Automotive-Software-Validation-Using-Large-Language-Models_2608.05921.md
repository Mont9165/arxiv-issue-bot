# Sensor-Level Fault Diagnosis for Automotive Software Validation Using Large Language Models

- arXiv ID: `2608.05921v1`
- Authors: Mohammad Abboush, Hamza Ouarrad, Andreas Rausch
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.05921v1) | [pdf](https://arxiv.org/pdf/2608.05921v1)

## Abstract

The pre-series validation of automotive software on hardware-in-the-loop (HIL) platforms produces large volumes of multivariate sensor recordings whose assessment against functional safety requirements exceeds what manual review can sustain at campaign scale. Threshold-based tooling reports that a deviation has occurred but neither identifies its nature nor locates its source, while data-driven classifiers, although accurate, rely on large labelled datasets and return opaque decisions that sit uneasily with the traceability demanded by ISO 26262. This study examines whether open-source instruction-tuned large language models (LLMs), given a textual description of sensor behaviour, can serve as data-efficient and interpretable engines for fault detection and diagnosis inside the validation loop. A two-phase framework is proposed: automated requirement checking on a dSPACE real-time platform first isolates the recordings that violate a safety requirement, and only these are inspected, with sliding windows of the signals reduced to statistical, relational, and contextual descriptors, embedded in a fixed prompt, and mapped by a 4-bit low-rank-adapted LLM to a fault location accompanied by a written justification. Four model families ranging from two to eight billion parameters were adapted and tested on a gasoline-engine case study spanning six injected fault classes. The smallest model matched the largest at 81.6\% accuracy, whereas a comparably sized model failed to converge, indicating that diagnostic competence under task-specific adaptation follows convergence rather than parameter count, with the entire adapt-and-evaluate cycle fitting on a single commodity accelerator.
