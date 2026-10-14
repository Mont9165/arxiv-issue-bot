# RepairFormer: Automated Repair of Structured Inputs Using Transformers

- arXiv ID: `2608.05060v1`
- Authors: Ovi Paul, Tom J King, Ali Shokri
- Published: 2026-08-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.05060v1) | [pdf](https://arxiv.org/pdf/2608.05060v1)

## Abstract

Structured input files such as JSON, DOT, OBJ, INI, S-expression, and TinyC are widely used in software systems, but small corruptions can cause parsers to reject otherwise useful data. Repairing such inputs is important because malformed configuration, program, and data files can interrupt testing, analysis, deployment, and downstream automation even when most of the original content remains intact. Existing repair techniques can produce structurally valid inputs, but they often rely on deletion or repeated search, which may lose original content and result in semantic incorrectness. This paper presents RepairFormer, a transformer-based framework for structured input repair. The approach formulates repair as a supervised sequence generation task and uses format tags, oracle validation, and boundary-localized repair to generate valid outputs while preserving content. The boundary workflow focuses generation on the detected fault region, reducing the input size, and supporting repair of longer files. In evaluation, RepairFormer achieves a 88% in repair and 94% in recovery, showing strongest content preservation when repairs are successful. Additional experiments on our benchmark shows RepairFormer repairs 97.57% and recovers 94.29% with 5x faster runtime compared to state of the art.
