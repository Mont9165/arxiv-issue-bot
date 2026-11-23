# Which Data-Center Load Models Can Be Trusted? An Evidence-Graded Review of Dynamic Modeling and Validation for Large Computational Loads

- arXiv ID: `2611.27169v1`
- Authors: Dileep Cheerla
- Published: 2026-11-20
- Primary category: `eess.SY`
- Categories: `eess.SY`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.27169v1) | [pdf](https://arxiv.org/pdf/2611.27169v1)

## Abstract

Grid operators now require dynamic models of data centers and other large computational loads, and new ride-through rules assume that these models predict how facilities respond to disturbances. This review asks what evidence supports that assumption. We coded 160 documents, screened from 1,424 de-duplicated database and seed records plus 65 added documents, by the strongest reference object each presents, from grid-side records to simulation only. Across 19 field-evidence entries, 15 requirement documents from three continents and nine model classes, we find two comparisons of a standard library model with measured data-center events: with default parameters the model failed both, and refitting it to each event separately reduced the error but was never tested on an unseen event. Among the sources reviewed, we found no successful held-out validation of a frozen, facility-specific data-center model against an independent measured disturbance, and 25 of the 33 model-phenomenon combinations with any evidence involve no electrical measurement. The features that distinguish the new rules (memory of repeated dips, recovery within 0.5-3 s, proportional power reduction during the sag, overvoltage response) are those current phasor models cannot represent or have never been tested against. In the operator procedures examined, simulations and model-to-model benchmarks are accepted as evidence of model fidelity, unlike the measured validation required of generators, and proposed mitigations have mostly been evaluated on unvalidated facility models. We propose context-of-use gates that separate calibration from validation, release labels for model claims, a minimum validation protocol with acceptance criteria, and a research agenda.
