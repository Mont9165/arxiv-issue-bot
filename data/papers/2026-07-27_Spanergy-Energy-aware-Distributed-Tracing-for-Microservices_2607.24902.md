# Spanergy: Energy-aware Distributed Tracing for Microservices

- arXiv ID: `2607.24902v1`
- Authors: César Perdigão Batista, Denis Conan, Sophie Chabridon
- Published: 2026-07-27
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.24902v1) | [pdf](https://arxiv.org/pdf/2607.24902v1)

## Abstract

Cloud computing is gaining popularity by giving access to seemingly unlimited virtual resources. However, Cloud data centres are built with physical resources and their electricity consumption has been continuously growing over the past decades. Microservices are an important building block of Cloud applications, calling for new solutions to observe their energy consumption. Distributed tracing is widely deployed to diagnose latency and failures in microservice-based applications, yet it does not expose the energy cost of individual end-user requests. Such a gap limits energy-aware debugging, accountability, and control. This paper presents Spanergy, an energy-aware distributed tracing approach that correlates per-microservice power measurements with traces and that attributes measured energy consumption to request segments, i.e. trace spans. We showcase Spanergy with synchronous request chains and asynchronous interactions across microservices. We present a rigorous experimental protocol and statistical analysis plan to quantify overhead and to validate conservation and coverage properties on realistic configurations. Enabling OpenTelemetry tracing increased total experiment energy by 59.1% relative to the uninstrumented baseline, and Spanergy post-processing added 15.2% of the baseline energy. Hence, Spanergy's incremental energy cost is smaller than the energy overhead of enabling tracing itself, making the approach lightweight in practice. Spanergy also reveals that a non-negligible fraction of request energy comes from spans outside the latency-critical path. These results show that energy-aware tracing is feasible at modest overhead and provides actionable insights for energy-efficient microservices.
