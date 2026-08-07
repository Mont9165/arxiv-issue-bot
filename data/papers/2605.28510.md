# Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets

- arXiv ID: `2605.28510v1`
- Authors: Andrea Gurioli, Davide D'Ascenzo, Federico Pennino, Maurizio Gabbrielli, Stefano Zacchiroli
- Published: 2026-05-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2605.28510v1) | [pdf](https://arxiv.org/pdf/2605.28510v1)

## Abstract

Large language models (LLMs) for code completion and generation are increasingly used in software development, yet they may reproduce training examples verbatim and without authorship attribution, raising legal and ethical concerns around plagiarism and license compliance. Classical fingerprint-based plagiarism detectors based on fingerprinting, such as Winnowing, remain highly effective, yet the inspection requires comparing fragments of code to the entire training set, and their linear-time search makes them impractical for the billion-scale corpora used to train modern code LLMs. To bridge this gap, we introduce SOURCETRACKER, a 300M-parameter encoder tailored for code retrieval, together with a hybrid two-stage provenance-tracking pipeline HYBRIDSOURCETRACKER (HST). HST first narrows down a small set of candidate snippets via vector search, then re-ranks those candidates using Winnowing on exact fingerprints. We train and evaluate our system on a 10M-snippet subset of the THESTACKV2 dataset, with both verbatim and adapted snippets that emulate realistic identifier renaming. On an in vitro 100k-snippet search space with adapted queries, our hybrid approach reaches a mean reciprocal rank on par with Winnowing for 30-token fragments. Then, starting from windows >= 60 tokens, it consistently over-performs by up to 5.4% while preserving logarithmic-time query complexity. In a complementary evaluation using an LLM-based judge, we find that many retrieved snippets not labeled as ground truth are still highly similar to the expected sources, particularly with longer context windows, and thus remain useful for end users. Overall, our results demonstrate that integrating vector search with fingerprinting enables scalable, high-precision provenance tracking for code produced by LLMs.
