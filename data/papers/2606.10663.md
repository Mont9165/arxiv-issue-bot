# Reconstructing OPC UA Address Spaces from Time-Series Databases

- arXiv ID: `2606.10663v1`
- Authors: Lukas Lürzer, Hannes Unger, Stefan Huber
- Published: 2026-06-09
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.10663v1) | [pdf](https://arxiv.org/pdf/2606.10663v1)

## Abstract

OPC UA has become the dominant open protocol in operational technology. Time-series databases routinely archive OPC UA telemetry but discard the semantic metadata (node hierarchy, engineering units, and type definitions) which gives sensor values their meaning. Recovering this information from a time-series database is non-trivial: namespace indices recorded at the source are session-local and unstable across restarts, and naive merging across multiple source servers results in identifier collisions. We present opcua-ts, an implemented architecture that persists this semantic information alongside its telemetry in a general-purpose time-series database under a lifecycle-stable join key, and that reconstructs the source address space as a live OPC UA endpoint. We characterize the conditions under which the reconstruction is sound across multi-source deployments and validate the approach with a NodeSet2 XML round-trip against the source server. Initial results from a boiler-simulator round-trip indicate that the approach is feasible.
