# Separation Logic for Verifying Physical Collisions of CNC Programs

- arXiv ID: `2605.10437v1`
- Authors: Yeonseok Lee
- Published: 2026-05-11
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.10437v1) | [pdf](https://arxiv.org/pdf/2605.10437v1)

## Abstract

Safety verification in Computer Numerical Control (CNC) machining has traditionally relied on simulation-based methods that require repetitive tests when requirements change. This paper introduces a formal verification framework that conceptualizes the physical CNC workspace as a Spatial Heap, treating physical occupancy as a managed logical resource. Central to our approach is a Parser-Prover Handshake that decouples machine kinematics from formal logic. By mapping tool trajectories and safety buffers into a discrete spatial model prior to evaluation, the framework enables the use of Separation Logic (SL) to verify safety via formal triples. Within this model, physical collisions are redefined as logical Spatial Data Races, detected through the failure of the separating conjunction to establish disjointness. Furthermore, we extend the methodology to collaborative environments using Concurrent Separation Logic (CSL), where physical hand-offs are verified as formal ownership transfers. This approach provides a scalable, mathematically grounded alternative to geometric simulation, offering a foundation for autonomous, zero-collision manufacturing.
