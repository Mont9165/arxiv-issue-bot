# LLMCrater: Lifecycle-Aware FAIR Metadata Generation using Large Language Models

- arXiv ID: `2608.23158v1`
- Authors: Dani Termaat, Nafiseh Soveizi, Zhiming Zhao, Marios Avgeris
- Published: 2026-08-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.23158v1) | [pdf](https://arxiv.org/pdf/2608.23158v1)

## Abstract

FAIR (Findable, Accessible, Interoperable, and Reusable) metadata is essential for the discovery, interoperability, and reuse of scientific research assets. However, creating and maintaining FAIR metadata remains largely manual, making the process time-consuming for heterogeneous research artifacts generated throughout the research lifecycle. Existing approaches primarily generate metadata at publication time, missing opportunities to capture contextual information as it becomes available. To address this limitation, we present \emph{LLMCrater}, a lifecycle-aware metadata generation framework that combines Large Language Models (LLMs) with stage-specific RO-Crate metadata profiles. The framework progressively enriches metadata across four research lifecycle stages (Design, Development, Deployment, and Execution \& Provenance) while remaining compatible with RO-Crate~1.1 and EOSC metadata recommendations. It automatically extracts metadata from heterogeneous artifacts, generates and validates machine-actionable RO-Crates, and supports publication to FAIR repositories and PID services (e.g., Zenodo). We demonstrate the approach using two representative use cases: a 5G experimentation environment within SLICES-RI and an experiment on GreenDIGIT's EcoJupyter platform. Results show that LLMCrater progressively enriches metadata throughout the research lifecycle and generates valid RO-Crates conforming to the RO-Crate~1.1 specification.
