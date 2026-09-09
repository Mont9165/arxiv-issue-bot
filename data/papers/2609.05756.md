# Concord: A Video Relational Algebra for Cross-Modal Query Optimization

- arXiv ID: `2609.05756v1`
- Authors: Sultan Muratbek, Charisse Ivana Yeung, Chanwut Kittivorawong, Alvin Cheung
- Published: 2026-09-04
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.05756v1) | [pdf](https://arxiv.org/pdf/2609.05756v1)

## Abstract

Semantic video queries let users embed natural language prompts and use multimodal large language models (MLLMs) to interpret the video. Such queries are increasingly popular for querying video data. However, their expressiveness comes at a steep cost: an MLLM may process hours of media to return only seconds of relevant output, making naive execution slow, expensive, and inaccurate.
  We propose Concord, a system for expressing and optimizing semantic video queries. We makes three contributions. First, we introduce Video Relational Algebra (VRA), a nested algebra over videos, transcripts, frames, and object tracks that captures common semantic video operations. Second, we derive a set of approximate optimizations that rewrite VRA queries to reduce MLLM usage while improving result quality. For narrated video, Concord either processes transcripts instead of video or uses them to identify video clips for MLLM processing. For cross-camera queries without narration, detection and tracking replace a whole-video MLLM join with a track-level relational join.
  Third, we evaluate Concord on real-world videos. Across 4.59 hours of soccer broadcasts and 3.92 hours of lectures, transcript-to-video queries send only 5.32% and 2.47% of source-video duration to the MLLM and reduce MLLM cost by up to 87%. In two five-second highway clips with 18 manually adjudicated cross-camera vehicles, a Detect-Track-Join query improves F1 from .364 to .813 while making no MLLM calls. See our project at https://concord-db.github.io/.
