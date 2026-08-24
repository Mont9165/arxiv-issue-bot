# On the Time and Frequency Domain Representations of Signals for CPS Specification

- arXiv ID: `2608.21167v1`
- Authors: Claudio Mandrioli, Drishti Yadav, Domenico Bianculli
- Published: 2026-08-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.21167v1) | [pdf](https://arxiv.org/pdf/2608.21167v1)

## Abstract

Specification languages are instrumental to the Verification \& Validation of Cyber-Physical Systems (CPSs). Most state-of-the-art specification languages use the time-domain representation of signals, which is not always suitable for describing signal shapes and dynamic behaviours. Instead, fields like control and robotics use the frequency-domain representation to characterise these behaviours. Time-frequency representations combine the capabilities of both domains. We investigate the use of time-frequency representations to specify CPS requirements. We analyse existing taxonomies of CPS requirements to identify which requirement classes can benefit from time-frequency representations. We derive the desiderata for a specification language that uses time-frequency representations and propose Signal-Spectrum Temporal Logic (S2TL), a language enabling assertions over frequency intervals and relations between frequency components. We operationalise the S2TL semantics for monitoring CPS traces, and implement a monitor. We define specification templates for the identified requirement classes and compare time- and time-frequency-domain formulations in terms of applicability, expression fidelity, and noise tolerance of monitoring. We observe that, while time-domain specifications are applicable only to input traces containing step-like changes or using constant interpolation, time-frequency specifications extend their evaluation to traces generated through linear interpolation, and improve tolerance to offset and high-frequency noise, while achieving comparable fidelity to the intended system properties.
