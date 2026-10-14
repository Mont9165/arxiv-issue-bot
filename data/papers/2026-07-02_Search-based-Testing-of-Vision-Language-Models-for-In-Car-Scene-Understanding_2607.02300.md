# Search-based Testing of Vision Language Models for In-Car Scene Understanding

- arXiv ID: `2607.02300v1`
- Authors: Lev Sorokin, Chen Yang, Ken E. Friedl, Andrea Stocco
- Published: 2026-07-02
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.02300v1) | [pdf](https://arxiv.org/pdf/2607.02300v1)

## Abstract

In the automotive domain, in-car scene understanding (ISU) enables the detection of safety-critical events, such as driver distraction, and supports drivers or passengers by analyzing the in-car scene and adapting the environment (e.g., ambient lighting). The industry is increasingly exploring vision-language models (VLMs) to interpret camera-recorded in-car scenes and extract information for downstream reasoning tasks. However, VLMs may generate incomplete, erroneous, or misleading scene descriptions, highlighting the need for systematic testing. Collecting real in-vehicle data is costly, difficult to scale, and often infeasible, particularly in early design stages. In this paper, we present ISU-Test, an automated testing approach that combines rendering-based scene generation with search-based testing to evaluate ISU systems. By framing testing as an optimization problem and systematically modifying scene parameters, our method generates diverse in-car scenarios and explores a wide range of configurations. We evaluate ISU-Test on both an industrial prototype and open-source VLMs across two case studies: question answering and captioning, comparing against randomized scenario generation. Results show that ISU-Test significantly outperforms the baseline, achieving up to 10 times higher failure rates and up to 3.6 times higher failure coverage.
