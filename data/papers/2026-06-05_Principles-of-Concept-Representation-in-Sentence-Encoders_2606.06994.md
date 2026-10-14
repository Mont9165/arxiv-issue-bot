# Principles of Concept Representation in Sentence Encoders

- arXiv ID: `2606.06994v1`
- Authors: Isabelle Mohr, John Dujany, Jonathan Souquet, Andre Freitas
- Published: 2026-06-05
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.06994v1) | [pdf](https://arxiv.org/pdf/2606.06994v1)

## Abstract

What makes a sentence encoder produce good concept representations? We approach this through the lens of representational compositionality: an encoder supports a concept family only when its latent space admits a low-distortion realization of the corresponding semantic operator. This framing predicts both where current encoders succeed and where they are structurally mismatched to their supervision. Through a controlled ablation over encoder conditions trained on 3.3 million synonym and definition pairs from WordNet and Wiktionary, evaluated on three decontaminated splits and a modifier-labeled noun-phrase benchmark, we identify four principles. Fine-tuning recalibrates the latent geometry rather than expanding it (P1). Semantic signal concentrates in the final transformer layer before concept-specific training begins, making cross-layer pooling redundant (P2). Hard negatives improve discrimination and stress-test robustness without improving retrieval ranking, showing that calibration and ranking are independently addressable (P3). Finally, the effectiveness of supervision depends on the composition type of the target concept. Extensional training helps intersective and subsective families while degrading relational and intensional ones, exposing a structural limitation of current training paradigms (P4). We release two new evaluation datasets: a DBpedia semantic-gap benchmark and a modifier-labeled NP paraphrase suite.
