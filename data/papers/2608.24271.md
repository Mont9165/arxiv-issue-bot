# Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering

- arXiv ID: `2608.24271v1`
- Authors: Zahra Seyedghorban, Egor Klimov, Arie van Deursen, Annibale Panichella, Burcu Kulahcioglu Ozkan
- Published: 2026-08-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.24271v1) | [pdf](https://arxiv.org/pdf/2608.24271v1)

## Abstract

Large Language Model-based multi-agent systems are increasingly explored for software engineering tasks, but they remain difficult to inspect, debug, and evaluate under controlled failures. We present llmmas-otel, a lightweight and framework-agnostic tool that combines OpenTelemetry-based distributed tracing with fault injection for LLM-based multi-agent systems in software engineering workflows. The tool instruments agent executions with trace-aligned telemetry across workflow phases, agent steps, inter-agent communication, tool calls, and LLM invocations, and supports targeted fault injection at selected interaction points. This makes it possible to compare baseline and faulty executions in a reproducible way and inspect the effects through aligned traces and run artifacts. We describe the motivation, architecture, implementation, current capabilities, and initial validation of the tool on a minimal demo workflow and a real LLM-based multi-agent system for software development.
