# Carbon-Taxed Transformers: A Green Compression Pipeline for Overgrown Language Models

- arXiv ID: `2604.25903v1`
- Authors: Ajmain Inqiad Alam, Palash Roy, Chanchal K. Roy, Banani Roy, Kevin A. Schneider
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2604.25903v1) | [pdf](https://arxiv.org/pdf/2604.25903v1)

## Abstract

The accelerating adoption of Large Language Models (LLMs) in software engineering (SE) has brought with it a silent crisis: unsustainable computational cost. While these models demonstrate remarkable capabilities in different SE tasks, they are unmanageably large, slow to deploy, memory-intensive, and carbon-heavy. This reality threatens not only the scalability and accessibility of AI-powered SE, but also its long-term environmental sustainability. The research challenge is clear: we must go beyond accuracy and address efficiency and environmental cost as first-class design constraints. To meet this challenge, we introduce Carbon-Taxed Transformers (CTT), a systematic multi-architectural compression principled pipeline ordering inspired by economic carbon taxation principles. Drawing from the economic concept of carbon pricing, CTT operationalizes a computational carbon tax that penalizes architectural inefficiencies and rewards deployment-ready compression. We evaluate CTT across three core SE tasks: code clone detection, code summarization, and code generation, with models spanning encoder-only, encoder-decoder, and decoder-only architecture. Our results show that CTT delivers on inference: (1) up to 49x memory reduction, (2) time reduction up to 8-10x for clone detection, up to 3x for summarization, and 4-7x for generation, (3) up to 81% reduction in CO2 emissions and (4) CTT retains around 98% accuracy on clone detection, around 89% on summarization, and up to 91% (textual metrics) and 68% (pass@1) for generation. Two ablation studies show that pipeline ordering and individual component contributions are both essential, providing empirical justification for CTT's design and effectiveness. This work establishes a viable path toward responsible AI in SE through aggressive yet performance-preserving compression.
