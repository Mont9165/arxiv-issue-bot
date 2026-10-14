# Token-Native Storage: Read and Write in your Agent's Language

- arXiv ID: `2608.02376v1`
- Authors: Kumar Shivendu
- Published: 2026-08-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.02376v1) | [pdf](https://arxiv.org/pdf/2608.02376v1)

## Abstract

Search and database engines still store text as UTF-8, a format built for humans. But the systems that increasingly read and write that text (embedders, rerankers, and language-model agents) work in token IDs, not characters, so every access pays to translate between the two. As agents become the primary readers and writers of stored text, we argue for token-native storage: keep the text as the model's own byte-pair-encoding (BPE) token IDs. This is both smaller and faster. Packing r50k IDs as uint16 already beats UTF-8 by 2.25x on English with no compression, and an entropy coder reaches 3.30x. Across six tokenizers and three corpora (English, code, Hindi), compressing token IDs matches or beats every byte codec, even a corpus-trained zstd dictionary. Two findings sharpen the case. BPE numbers tokens by merge order, not frequency, and re-ranking by frequency lets a plain integer codec (streamvbyte) recover most of the entropy coder's ratio while decoding ~7x faster, a one-line change we ask AI labs to make when they publish vocabularies. And because a model reads token IDs, not text, a token-native store hands them over directly instead of re-tokenizing on every read, ~10-600x faster. The only barrier is that sharing token IDs requires a common tokenizer, which is not always true across model families yet, so we argue for standardization: a published, shared vocabulary, the way ASCII and UTF-8 standardized text.
