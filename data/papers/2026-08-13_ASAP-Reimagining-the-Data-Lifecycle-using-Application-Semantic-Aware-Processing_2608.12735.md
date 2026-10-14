# ASAP: Reimagining the Data Lifecycle using Application Semantic-Aware Processing

- arXiv ID: `2608.12735v1`
- Authors: Milind Srivastava, Zeying Zhu, Yajie Zhou, Yancheng Yuan, Fenghao Dong, Peilin Xin, Zaoxing Liu, Vyas Sekar
- Published: 2026-08-13
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.12735v1) | [pdf](https://arxiv.org/pdf/2608.12735v1)

## Abstract

Across many domains (e.g., observability, networking, security), data processing pipelines face what we refer to as the CSP problem: achieving low Cost at large Scale, while maintaining high Performance. In response, we see several efforts to tackle CSP in various stages of the Collect-Transmit-Store-Analyze data lifecycle; such as approximate query processing in databases or sketches in network routers. Our work is driven by the simple insight: "seeing the forest for the trees". These proposed solutions (e.g., AQP, sketching, compression, rollups) addressing CSP share a common property - they exploit semantic-preserving opportunities to support application needs. In this paper, we make a case for ASAP, a paradigm that makes Application Semantic-Aware Processing (ASAP) a first-class design principle in data processing pipelines. We argue that by taking a unified view across ASAP primitives developed in different domains, across the entire data lifecycle, we can unlock new opportunities to tackle the CSP problem. In particular, we can: (i) enable novel cross-lifecycle optimizations such as analytics run directly on sketches computed at the source; (ii) leverage primitives developed in other application domains; and (iii) enable widespread adoption of these powerful techniques. We discuss research challenges in socializing the benefits of the ASAP paradigm, and show preliminary evidence that adopting ASAP can yield up to 3 orders of magnitude improvements in the CSP tradeoff for many application domains.
