# Divide-then-Diagnose: Weaving Clinician-Inspired Contexts for Ultra-Long Capsule Endoscopy Videos

- arXiv ID: `2604.21814v1`
- Authors: Bowen Liu, Li Yang, Shanshan Song, Mingyu Tang, Zhifang Gao, Qifeng Chen, Yangqiu Song, Huimin Chen, Xiaomeng Li
- Published: 2026-04-23
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.21814v1) | [pdf](https://arxiv.org/pdf/2604.21814v1)

## Abstract

Capsule endoscopy (CE) enables non-invasive gastrointestinal screening, but current CE research remains largely limited to frame-level classification and detection, leaving video-level analysis underexplored. To bridge this gap, we introduce and formally define a new task, diagnosis-driven CE video summarization, which requires extracting key evidence frames that covers clinically meaningful findings and making accurate diagnoses from those evidence frames. This setting is challenging because diagnostically relevant events are extremely sparse and can be overwhelmed by tens of thousands of redundant normal frames, while individual observations are often ambiguous due to motion blur, debris, specular highlights, and rapid viewpoint changes. To facilitate research in this direction, we introduce VideoCAP, the first CE dataset with diagnosis-driven annotations derived from real clinical reports. VideoCAP comprises 240 full-length videos and provides realistic supervision for both key evidence frame extraction and diagnosis. To address this task, we further propose DiCE, a clinician-inspired framework that mirrors the standard CE reading workflow. DiCE first performs efficient candidate screening over the raw video, then uses a Context Weaver to organize candidates into coherent diagnostic contexts that preserve distinct lesion events, and an Evidence Converger to aggregate multi-frame evidence within each context into robust clip-level judgments. Experiments show that DiCE consistently outperforms state-of-the-art methods, producing concise and clinically reliable diagnostic summaries. These results highlight diagnosis-driven contextual reasoning as a promising paradigm for ultra-long CE video summarization.
