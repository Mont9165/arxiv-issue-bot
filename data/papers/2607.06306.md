# UI2App: Benchmarking Visual Interaction Inference in Executable Web Application Generation

- arXiv ID: `2607.06306v1`
- Authors: Grace Man Chen, Litao Guo, Yifan Wu, Yiyu Chen, Yenchi Tseng, Sicheng Liu, Yuyu Luo, Ying-Cong Chen
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CV`
- Links: [abs](http://arxiv.org/abs/2607.06306v1) | [pdf](https://arxiv.org/pdf/2607.06306v1)

## Abstract

Large language models (LLMs) have demonstrated growing competence in web page generation. However, existing text-driven approaches rely on complex prompts that impose substantial demands on users and offer limited expressivity for page layout and cross-page visual coherence. Image-driven paradigms, which take UI screenshots as input, align more closely with real development workflows. However, current benchmarks focus primarily on visual fidelity and lack a systematic evaluation of the interaction capabilities in generated artifacts. To address this gap, we introduce UI2App, the first benchmark targeting interaction inference, the ability to recover application behavior from screenshots alone, without any textual or behavioral guidance. UI2App comprises 327 screenshots grouped into 45 state-coherent screenshot sets for runnable multi-route web applications. We design an end-to-end pipeline that evaluates each artifact along four dimensions: executability, navigation reachability, visual fidelity, and interaction inference. The interaction metric (IIS) assesses inferred interactions by functional correctness and state-management complexity, crediting any valid implementation rather than matching a single reference. Experiments on six frontier vision-language models reveal a marked capability mismatch between visual reconstruction and interaction realization: the visual-fidelity leader scores only 7.5 on IIS, ranking fourth and trailing the IIS leader by 5.2x. High-complexity interactions such as cross-page state remain a pervasive bottleneck, with half of the evaluated models scoring exactly zero on this dimension. Overall, the results indicate that inferring complete interaction behavior from static screenshots remains a key challenge for models.
