# Temporal Adaptive Fine-Tuning for Code Comprehension

- arXiv ID: `2610.19970v1`
- Authors: Alex Wolf, Pooja Rani, Harald C. Gall
- Published: 2026-10-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.19970v1) | [pdf](https://arxiv.org/pdf/2610.19970v1)

## Abstract

Repository-level code comprehension question answering (QA) supports developer reasoning over functionality and usage distributed across codebases. However, repository-specialized large language models (LLMs) can become misaligned as code evolves. We study this challenge as temporal repository adaptation: acquiring new knowledge, suppressing obsolete, retaining still-valid, and preserving semantically neighboring knowledge. Existing retrieval, fine-tuning, and model-editing methods address only parts of this problem. We propose Temporal Adaptive Fine-Tuning (TAFT), a novel adaptation approach that treats repository transitions as supervision. TAFT derives temporally grounded QA data from repository transitions, pairs newly valid with obsolete knowledge through preference optimization, and replays transition-conditioned retention examples to preserve still-valid knowledge. We evaluate TAFT on an augmented temporal SWE-bench dataset comprising 255,295 QA entries across ten temporal slices, comparing deferred (Baseline), per-slice retrained (Baseline-Batched), and variants with knowledge anchors along four dimensions: updated knowledge, obsolete-answer suppression, retention, and neighbor stability. TAFT consistently outperforms both the deferred and batched baselines, with an average relative improvement of 18% in updated/suppressed knowledge accuracy, doubled retention accuracy, and roughly 1.5 times the neighbor accuracy. With directly supplied knowledge anchors, TAFT-KANT further improves mean updated/suppressed, retention, and neighbor accuracy over TAFT by 3.55%, 8.35%, and 13.00%, respectively. Overall, TAFT demonstrates its effectiveness across all evaluated areas, effectively enabling code comprehension QA alignment with repository evolution.
