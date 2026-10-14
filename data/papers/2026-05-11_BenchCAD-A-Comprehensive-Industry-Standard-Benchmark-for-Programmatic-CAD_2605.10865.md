# BenchCAD: A Comprehensive, Industry-Standard Benchmark for Programmatic CAD

- arXiv ID: `2605.10865v1`
- Authors: Haozhe Zhang, Kaichen Liu, Miaomiao Chen, Lei Li, Shaojie Yang, Cheng Peng, Hanjie Chen
- Published: 2026-05-11
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CV`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.10865v1) | [pdf](https://arxiv.org/pdf/2605.10865v1)

## Abstract

Industrial Computer-Aided Design (CAD) code generation requires models to produce executable parametric programs from visual or textual inputs. Beyond recognizing the outer shape of a part, this task involves understanding its 3D structure, inferring engineering parameters, and choosing CAD operations that reflect how the part would be designed and manufactured. Despite the promise of Multimodal large language models (MLLMs) for this task, they are rarely evaluated on whether these capabilities jointly hold in realistic industrial CAD settings. We present BenchCAD, a unified benchmark for industrial CAD reasoning. BenchCAD contains 17,900 execution-verified CadQuery programs across 106 industrial part families, including bevel gears, compression springs, twist drills, and other reusable engineering designs. It evaluates models through visual question answering, code question answering, image-to-code generation, and instruction-guided code editing, enabling fine-grained analysis across perception, parametric abstraction, and executable program synthesis. Across 10+ frontier models, BenchCAD shows that current systems often recover coarse outer geometry but fail to produce faithful parametric CAD programs. Common failures include missing fine 3D structure, misinterpreting industrial design parameters, and replacing essential operations such as sweeps, lofts, and twist-extrudes with simpler sketch-and-extrude patterns. Fine-tuning and reinforcement learning improve in-distribution performance, but generalization to unseen part families remains limited. These results position BenchCAD as a benchmark for measuring and improving the industrial readiness of multimodal CAD automation.
