# Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data

- arXiv ID: `2611.09372v1`
- Authors: Carlos Martín-Abellán, Mark Kröll
- Published: 2026-11-06
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.DB`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2611.09372v1) | [pdf](https://arxiv.org/pdf/2611.09372v1)

## Abstract

Energy management officers and grid operators increasingly rely on smart meter data for anomaly detection, performance monitoring, and strategic decision-making. However, extracting actionable insights from large-scale, heterogeneous telemetry databases requires advanced SQL and data engineering expertise, creating a critical bottleneck for non-technical personnel. Furthermore, the strict data privacy regulations and security constraints inherent to critical energy infrastructure often prohibit the routing of sensitive consumer data through cloud-based Large Language Models (LLMs). To address these challenges, we present OpenMeter, a schema-agnostic Multi-Agent System (MAS) designed to translate natural language queries into executable code and human-readable insights. This architecture lowers the technical barrier for day-to-day utility operations by empowering non-expert personnel to interact with complex databases through intuitive natural language dialogue, transforming raw telemetry into a highly valuable tool for routine grid workflows and strategic decisions. Multi-scenario ablation studies over this environment demonstrate that full multi-agent orchestration shows its largest observed accuracy gains on resource-constrained local hardware (+6.1 pp EX-R over the strongest single-agent configuration); at frontier scale, individual components retain value but should be enabled selectively, indicating that the cost of full orchestration is justified specifically where privacy demands local execution.
