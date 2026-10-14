# When Model Release Meets Model Reuse: Producer-Consumer Misalignment in Hugging Face

- arXiv ID: `2607.21738v1`
- Authors: Adekunle Ajibode, Oussama Ben Sghaier, Bram Adams, Ahmed E. Hassan
- Published: 2026-07-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.21738v1) | [pdf](https://arxiv.org/pdf/2607.21738v1)

## Abstract

Pre-trained Language Models (PTLMs) are increasingly reused as dependencies in modern software systems, even though prior work has documented persistent structural problems in PTLM supply chains, such as inconsistent release practices, incomplete metadata, and divergence between Hugging Face and GitHub repositories. One previously unexplored angle on these problems is that misalignment between PTLM producers' release practices and consumers' model reuse needs may explain several of these challenges, yet the human expectations, processes and interactions underneath this misalignment have never been studied. As such, we conducted the first dual-perspective survey of 50 Hugging Face producers and 95 GitHub consumers to examine producer-consumer misalignments across four AI supply chain dimensions: model discovery, documentation practices, lineage tracing, and model governance adoption. We find that, although producers and consumers rely on the same documentation artifacts, they disagree on where critical metadata should be recorded. Even though 27.9% of producers and 31.4% of consumers trace lineage beyond the immediate parent model, producers primarily trace model lineage for provenance and reproducibility, whereas consumers are mainly driven by quality and reliability concerns. Furthermore, producers believe that governance mechanisms that streamline model release would have the greatest positive impact, whereas consumers prioritize documentation and dependency transparency. These findings highlight opportunities to improve model documentation conventions, lineage visibility, and governance support in PTLM supply chains.
