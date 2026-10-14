# From Driving Videos to Simulatable Scenarios

- arXiv ID: `2606.21993v1`
- Authors: Alexandre Levy, Ernest Valveny Llobet, Antonio Manuel López
- Published: 2026-06-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CV`
- Links: [abs](http://arxiv.org/abs/2606.21993v1) | [pdf](https://arxiv.org/pdf/2606.21993v1)

## Abstract

Autonomous vehicles (AVs) face driving scenarios ranging from routine traffic to rare events. To assess safety it is crucial to reproduce these scenarios in a controllable, repeatable, and scalable manner, with simulation playing a key role. This paper introduces D-V2S, a novel framework that automatically generates simulatable driving scenarios from driving videos. D-V2S operates in two stages: a Driving Record Analyzer (DRA) uses a vision language model (VLM) with our designed prompt to produce natural-language descriptions from input videos, capturing road layouts and dynamic traffic interactions; subsequently, a Scenario Generator (SG) uses a large language model (LLM) and our conditioning context to translate these descriptions into executable scenarios. Using simulations, we show that D-V2S generates scenarios where 90% of the relevant semantic elements of the videos are present. We also provide qualitative results demonstrating D-V2S's capability to transform real-world driving videos into simulatable scenarios. Moreover, we provide both semantic and human driven ablative analyses of D-V2S's modules. In particular, we show how the VLM choice matters for DRA, and how our SG achieves a 75% preference rate over other state-of-the-art methods.
