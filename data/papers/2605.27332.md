# EdgeFlow: Edge-Map Augmented VLM-Based Flowchart Processing for Industrial Requirements Engineering

- arXiv ID: `2605.27332v1`
- Authors: Zhifei Dou, Shabnam Hassani, Ou Wei
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CV`
- Links: [abs](http://arxiv.org/abs/2605.27332v1) | [pdf](https://arxiv.org/pdf/2605.27332v1)

## Abstract

Flowcharts are widely used in industrial requirements, but usually remain embedded as static images. Vision Language Models (VLMs) show promise in the conversion of these flowcharts into machine-readable models for RE activities, yet, when directly applied to flowchart conversion, they often fail on topology-critical visual details. To address this, we propose EdgeFlow that augments a VLM's original input with a deterministically extracted Canny edge map-acting as a structural prior-to improve flowchart-to-Mermaid conversion, without requiring annotated training data or domain-specific model fine-tuning.
  We evaluate EdgeFlow on IndusReqFlow, a dataset sourced from real-world requirements. Compared with off-the-shelf VLMs, EdgeFlow improves node-level F1 by 17.39 percentage points and edge-level F1 by 16.94 percentage points. At the path level, EdgeFlow improves path F1 by 11.06 percentage points, enabling better support for model-based testing. These results demonstrate that EdgeFlow provides a practical, training-free means to improve topology-preserving flowchart-to-Mermaid conversion for industrial RE. Cross-dataset evaluation results on a public synthetic benchmark show no significant improvement; this highlights the need for diverse benchmarks incorporating industrial data for the comprehensive evaluation of future VLM-based RE tools.
