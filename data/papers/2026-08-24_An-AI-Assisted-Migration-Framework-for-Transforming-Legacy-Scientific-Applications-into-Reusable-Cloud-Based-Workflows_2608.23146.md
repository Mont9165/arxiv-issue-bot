# An AI-Assisted Migration Framework for Transforming Legacy Scientific Applications into Reusable Cloud-Based Workflows

- arXiv ID: `2608.23146v1`
- Authors: Nafiseh Soveizi, Sven Tesselaar, Hero Robinson Brouwer, Zhiming Zhao
- Published: 2026-08-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.23146v1) | [pdf](https://arxiv.org/pdf/2608.23146v1)

## Abstract

Legacy scientific applications remain valuable research assets but are often tightly coupled to project-specific execution environments, limiting their reuse, reproducibility, and deployment within modern scientific workflow systems and cloud-native Virtual Research Environments (VREs). Existing migration approaches primarily target individual artifacts, such as notebooks or containers, and provide limited support for systematically transforming heterogeneous legacy applications into reusable cloud-native workflows. This paper presents an AI-assisted migration framework that combines the Reference Model of Open Distributed Processing (RM-ODP)-guided architectural analysis, Large Language Models (LLMs), and Design Structure Matrix (DSM) analysis. The framework first uses RM-ODP to guide an LLM in identifying reusable workflow components, their interfaces, and execution dependencies from heterogeneous legacy applications. The resulting workflow structure is then iteratively evaluated and refined using DSM analysis. Finally, an LLM-based workflow generator implements the validated workflow components and produces containerized execution environments and executable workflow definitions for deployment in cloud-native workflow systems, including VREs. The framework was evaluated on two legacy scientific applications from different scientific domains. In both cases, the applications were successfully transformed into reusable cloud-native workflows while preserving their original functionality, demonstrating the feasibility of the proposed approach for modernizing legacy scientific software.
