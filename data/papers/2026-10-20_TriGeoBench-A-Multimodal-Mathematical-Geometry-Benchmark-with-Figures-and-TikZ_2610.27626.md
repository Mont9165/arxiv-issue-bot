# TriGeoBench: A Multimodal Mathematical Geometry Benchmark with Figures and TikZ

- arXiv ID: `2610.27626v1`
- Authors: Jing Wang, Yitong Yang, Hao Dou, Yaomin Wu, Shuting He, Tingfei Shen, Jia Wu, Jiaqi Li, Yinglin Wang
- Published: 2026-10-20
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.27626v1) | [pdf](https://arxiv.org/pdf/2610.27626v1)

## Abstract

Multimodal Large Language Models show strong vision-language capabilities, yet their geometry-centric reasoning remains insufficiently understood. Existing mathematical benchmarks typically rely on rasterized figures and cover limited geometric knowledge areas and response formats, making it difficult to assess whether models reason over geometric structures or exploit superficial visual patterns. We introduce TriGeoBench, a geometry-centric multimodal benchmark constructed from Chinese middle- and high-school mathematics examinations. TriGeoBench contains 7,000 question-answer pairs and 12,235 geometric figures with TikZ code, spanning plane geometry, solid geometry, analytic geometry, function, and vector geometry across diverse response formats. Each instance forms a {question-answer pair, image, TikZ} triplet: question-answer pairs are stored in LaTeX, images as RGB figures, and TikZ preserves geometric topology, symbolic annotations, and relational structure. We evaluate representative open- and closed-source MLLMs through image-to-TikZ and multimodal reasoning probes. Results reveal persistent fine-grained structure and image-text alignment challenges. Oracle experiments with human-curated reference TikZ suggest that accurate executable representations provide complementary geometric cues; they do not evaluate an end-to-end conversion pipeline. TriGeoBench offers a testbed for structure-aware mathematical reasoning.
