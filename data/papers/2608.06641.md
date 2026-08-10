# From Documentation to Zero-day Vulnerabilities: LLM-Driven Fuzzing of JavaScript Engines in PDF Readers

- arXiv ID: `2608.06641v1`
- Authors: Suyue Guo, Stijn Pletinckx, Tianle Yu, Yigitcan Kaya, Saad Ullah, Wenbo Guo, Christopher Kruegel, Giovanni Vigna
- Published: 2026-08-06
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.06641v1) | [pdf](https://arxiv.org/pdf/2608.06641v1)

## Abstract

Existing fuzzers for PDF readers rely on simple test cases that involve only individual API calls, leading to limited coverage and potentially missing vulnerabilities that require sequences of API calls. To address these limitations, we propose PDFuzzer, a novel PDF engine fuzzer that automatically generates complex and meaningful API call sequences. PDFuzzer first uses a Large Language Model (LLM) to construct context-free grammars and infer the relationships between individual API calls from specifications extracted from JavaScript API manuals and execution traces. Based on the grammars and relationships, PDFuzzer employs a constraint solver to generate concrete API call sequences for fuzzing. Our experiments show that PDFuzzer significantly outperforms state-of-the-art PDF fuzzers (TypeOracle, Favocado, and Cooper) and LLM-based fuzzers (Fuzz4All, naive LLM) on three mainstream PDF readers: Adobe Acrobat Reader, Foxit PDF Reader, and PDF-XChange Editor. PDFuzzer achieves up to 48% higher coverage than existing tools and identifies 31 zero-day vulnerabilities in these readers, from information leakage to arbitrary code execution. Our ablation study validates the necessity of each component, including LLMs, which achieve high accuracy across all pipeline stages (93-98%). We disclosed all vulnerabilities to the vendors via a coordinated vulnerability disclosure process and received bug bounties.
