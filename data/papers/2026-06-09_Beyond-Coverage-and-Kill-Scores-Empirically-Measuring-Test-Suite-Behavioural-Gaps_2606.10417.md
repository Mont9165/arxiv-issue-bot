# Beyond Coverage and Kill Scores: Empirically Measuring Test Suite Behavioural Gaps

- arXiv ID: `2606.10417v1`
- Authors: Partha Protim Paul, Reid Holmes
- Published: 2026-06-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.10417v1) | [pdf](https://arxiv.org/pdf/2606.10417v1)

## Abstract

Traditional test adequacy metrics measure a system's implementation, not whether it adheres to its expected behaviour. While developers rely heavily on code coverage and mutation testing to assess test suite quality, these metrics are fundamentally implementation-centric and cannot detect gaps between what the code is expected to do and what it actually does. Unfortunately, there has been no way to reliably detect these discrepancies; in this paper we introduce an automated proof-of-concept approach to investigate these gaps. The approach extracts expected method-level behaviours from natural language documentation and source code, maps them to existing test cases, and identifies gaps between expected and validated behaviours. We evaluate the approach across ten popular open-source Java libraries comprising 8,922 methods, extracting 20,729 behaviours with 93.1% precision. Our empirical analysis conservatively estimates that 17.5% of detected expected behaviours remain entirely untested, which we term as the test suite's behavioural gap. To determine if these gaps are merely an artifact of human-driven testing, we evaluate state-of-the-art automated test generators (EVOSUITE / ASTER), finding that they similarly fail to validate at least 20.6% / 27.1% of detected expected behaviours. We further demonstrate that behavioural gaps are not predicted by traditional structural metrics: the majority of untested behaviours occur in methods that already have high line coverage, and over half persist in methods with high mutation kill score. These results suggest behavioural coverage acts as an independent dimension of test suite adequacy that can complement traditional structural metrics.
