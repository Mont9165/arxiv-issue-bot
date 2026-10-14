# SHIA: A Direct SysML-Hardware Interface Architecture for Model-Centric Verification

- arXiv ID: `2605.11248v1`
- Authors: Charles Lewis, Amal Elsokary, Siyuan Ji
- Published: 2026-05-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2605.11248v1) | [pdf](https://arxiv.org/pdf/2605.11248v1)

## Abstract

Model-Based Systems Engineering (MBSE) is widely treated as the backbone of digital engineering, with languages such as the Systems Modeling Language (SysML) providing the means to capture system structure, behaviour, and verification intent. Yet once verification moves to hardware, the system model is routinely left behind. Domain-specific simulation environments, model transformations, and bespoke tool integrations take over, and the model that began as the authoritative reference drifts out of sync with the implementation it was meant to govern. This paper introduces the SysML Hardware Interface Architecture (SHIA), which keeps an executable SysML model directly inside the verification loop, exchanging messages with physical hardware without intermediate transformation chains, co-simulation platforms, or broker-mediated plugins. SHIA is realised through a SysML side server, written in embedded C++ within IBM Rhapsody, and a hardware side server running on a Raspberry Pi, together establishing a bidirectional link between the digital model and the physical system. A logic gate case study demonstrates the approach end-to-end, from hardware model construction and prototype assembly to test harness design, behavioural statechart control, and staged verification of each component before integration. The integrated system exchanged messages correctly in both directions, and Karnaugh map comparison between the SysML-generated and hardware-generated outputs showed zero discrepancy. The result shows that, when paired with a suitable interface, SysML need not remain a static description that informs downstream tools; it can serve as the executable layer through which hardware behaviour is stimulated, observed, and verified. The work demonstrates a route to model-governed verification and a shorter digital thread between system architecture and the hardware that realises it.
