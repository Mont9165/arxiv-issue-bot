# Back to the Future: Regressing Readability Features from LLMs

- arXiv ID: `2610.04641v1`
- Authors: Tairan Wang, Earl T. Barr
- Published: 2026-10-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.04641v1) | [pdf](https://arxiv.org/pdf/2610.04641v1)

## Abstract

Code readability supports software understanding, review, and maintenance. As AI coding agents become more widely used, readable code helps both humans review agent-generated output and agents maintain code within limited context windows. Yet existing readability models do not consistently agree with human judgements across datasets.
  We introduce BTTF (Back To The Future), pairing linear regression with information-theoretic features. Rather than using language models as black-box judges, BTTF uses them as measurement instruments. It combines traditional code measurements, embedding-based semantic organisation, and causal-LM predictability to capture source structure, semantic coherence, and contextual surprise.
  We evaluate BTTF on five publicly available human-rated readability benchmarks and our manually annotated MBJP development set, totalling 1,100 samples. BTTF improves average Spearman correlation over the strongest baseline by up to 0.101. Across 13 controlled readability-reducing transformations on production code, it achieves response rates of 93.8% in Java and 87.6% in Python, outperforming Dorn by 14% and 19.2%. It performs best among local models and trails the strongest cloud-LLM response by 1.7% in Java and 5.1% in Python. The direct-LLM baselines require an average of 1,083 prompt tokens per evaluation while remaining opaque. BTTF combines state-of-the-art benchmark performance and strong transformation robustness with feature-granular interpretability: every feature coefficient matches its theoretical directional effect across all evaluated model configurations.
