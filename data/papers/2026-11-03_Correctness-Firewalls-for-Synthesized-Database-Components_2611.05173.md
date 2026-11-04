# Correctness Firewalls for Synthesized Database Components

- arXiv ID: `2611.05173v1`
- Authors: Mohammad Javad Amiri, Carsten Binnig, Andreas Kipf, Tim Kraska, Ryan Marcus, Johannes Wehrstein, Chenyuan Wu, Geoffrey X. Yu, Zijie Zhao
- Published: 2026-11-03
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.05173v1) | [pdf](https://arxiv.org/pdf/2611.05173v1)

## Abstract

For the first time in history, high-performance code is cheap. Today's coding agents can generate bespoke, instance-optimized data systems with excellent performance, and such agents will continue to improve as LLMs advance. But a purely agentic approach, even when validated with strong testing techniques, does not automatically inherit the correctness guarantees our community has spent decades building. We propose a middle ground between hand-crafted and agent-crafted systems: correctness firewalls, lightweight design patterns under which a synthesized component can affect a system's performance but never its results. Behind a correctness firewall, agents are free to synthesize fast components while the overall system remains correct. We present three case studies, each demonstrating a different type of firewall: cardinality estimation (advisory), searching sorted data (guarded), and data compression (certified). In early experiments, synthesized components search sorted data up to 3x faster than human-designed learned indexes and can compress text 1.5x smaller than Zstd. Drawing on these case studies, we outline a research agenda for how data management systems can exploit coding agents without giving up their hard-won correctness guarantees, from protecting synthesized code to measuring the cost of correctness.
