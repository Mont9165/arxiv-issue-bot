# One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics

- arXiv ID: `2611.34925v1`
- Authors: Shuaijun Liu, Qifu Wen, Xingwei Chen, Xinwen Hu, Feiyang You, Sijia Chen, Ningxin Su
- Published: 2026-11-25
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.34925v1) | [pdf](https://arxiv.org/pdf/2611.34925v1)

## Abstract

Simulation is essential for marine robotics, yet existing platforms often trade off between visually realistic worlds, high-throughput experimentation, and ocean-condition realism grounded in real data. We present OneOcean, a data-grounded simulation suite and benchmark built around a unified spatiotemporal ocean-environment product that harmonizes bathymetry with data-driven currents and tides, with optional pollution fields for cleanup-related evaluation. On top of this environment representation, OneOcean defines a task ladder spanning navigation and station-keeping under currents, waypoint and route following, depth-profile tracking, area scanning, pipeline inspection, and multi-agent coordination, including formation transit, fish protection and patrol (herding), and surface pollution localization, containment, and cleanup. The suite supports multi-agent settings with 2-10 vehicles. Our simulator supports three to six Degrees of Freedom (DoF) and produces standardized metrics and reproducible run manifests, enabling consistent aggregation across tasks, difficulties, and scaling settings. Experiments across dataset variants and scenes systematically stress planning and control under data-grounded disturbances and reveal trade-offs among heuristic baselines, Behavior Cloning (BC), and a Large Language Model (LLM)-based planner.
