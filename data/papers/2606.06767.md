# The Custody Envelope Threshold: Authority-Scaled Admission of External Artifacts in Institutional Infrastructure

- arXiv ID: `2606.06767v1`
- Authors: Amadeus Brandes
- Published: 2026-06-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.06767v1) | [pdf](https://arxiv.org/pdf/2606.06767v1)

## Abstract

Modern infrastructure depends on externally maintained artifacts such as package-registry dependencies, CI/CD actions, container images, Terraform providers and modules, developer extensions, model artifacts, and AI tool servers. These artifacts are easy to fetch but difficult for institutions to admit, govern, and revoke. This paper proposes the Custody Envelope Threshold, an authority-scaled model of artifact admission. It argues that direct institutional admission is defensible only when object identity, ingress path, and revocation capacity are sufficiently closed relative to the execution authority delegated to the artifact. When this threshold is not met, institutions tend to proxy, policy-mediate, vendor-mediate, internalize, quarantine, or reject the artifact. The framework is operationalized as a four-condition ordinal instrument and connected to reference-monitor reasoning, least privilege, and transaction cost economics. It is applied to package dependencies, GitHub Actions, container images, Terraform providers and modules, developer extensions, and open model artifacts, with Model Context Protocol (MCP) servers treated as held-out evidence. The paper also specifies a validation design, deterministic prediction function, and OSF replication package for testing whether high-scrutiny institutions converge toward stronger custody closure for high-authority artifacts.
