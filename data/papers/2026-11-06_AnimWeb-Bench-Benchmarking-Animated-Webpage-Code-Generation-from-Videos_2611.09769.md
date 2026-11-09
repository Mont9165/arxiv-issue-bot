# AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos

- arXiv ID: `2611.09769v1`
- Authors: Zhongyi Zhang, Jingyu Xiao, Shuqing Li, Michael R. Lyu
- Published: 2026-11-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CV`
- Links: [abs](http://arxiv.org/abs/2611.09769v1) | [pdf](https://arxiv.org/pdf/2611.09769v1)

## Abstract

Animation is pervasive on the Web, the CSS animation property alone appears on over three-quarters of webpages. Yet existing webpage code generation benchmarks target static screenshots, user-triggered interactions, or isolated motion graphics, leaving the ability of multimodal large language models (MLLMs) and coding agents to reconstruct complete animated webpages largely unexplored. To fill this gap, we introduce AnimWeb-Bench, the first benchmark for animated webpage code generation from videos. It comprises 124 real-world webpages spanning 7 application domains and 33 animation types, with 91.9% of pages combining multiple types, each paired with a reference video and the static assets of the original webpage. We further propose a human-aligned, two-dimensional evaluation protocol: Static Appearance Fidelity measures structure, text, color, and visual similarity on aligned keyframes, while Animation Fidelity tracks UI components across frames and compares their position, size, velocity, and appearance with those in the reference video. Evaluating 14 MLLMs and three coding agents reveals: (1) reproducing webpage animations is substantially more difficult than reproducing static appearance; (2) explicit frame inspection and render feedback improve the reconstruction quality of coding agents; and (3) rapid, continuous changes are harder to reproduce than discrete state transitions. Our code and dataset are available at https://starry1001.github.io/AnimWeb-Bench-website/ .
