# TT-SAX: A Two-Track Time Series Symbolization for Natural Language Shape Querying

- arXiv ID: `2610.30593v1`
- Authors: Zhao Tan, Xianglong Bao, Zhipeng Xi, Ming Jin
- Published: 2026-10-22
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2610.30593v1) | [pdf](https://arxiv.org/pdf/2610.30593v1)

## Abstract

Natural language querying for time series databases aims to let users find what they need in long histories of data by asking in plain language. Shape queries ask how a series moves. They are the main challenge of this task. Recent work makes them feasible by using symbolization as a bridge between the query and the long history. However, existing symbolizations were designed for compression, similarity indexing, or classification. What a symbolization should provide for natural language querying has not been systematically studied. We therefore examine the definitions of six classical symbolizations against this task and identify three limitations. (1) Direction is missing from the string, (2) direction is measured at too small a scale, and (3) the letters are arbitrary. Three design principles follow. We follow these principles and make a minimal redesign of SAX called TT-SAX (two-track SAX). The level letters stay. Each segment gains a trend letter. It is measured across neighboring segments rather than inside one, and graded to match the adjectives that queries use. We conduct extensive experiments on the public NLQTSBench benchmark, comparing TT-SAX with the six classical symbolizations across six LLMs. TT-SAX outperforms all six on shape queries, and ablations trace its gains back to the three limitations one by one. This paper is the first systematic study of time series symbolization with natural language querying as the design goal. It provides a foundation for future research on this task. Our code is available at https://github.com/Atlamtiz/tt-sax.
