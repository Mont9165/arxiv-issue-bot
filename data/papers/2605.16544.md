# TARIPlay: A Test Framework for AR Applications based on Interactive Area Tracking in Playback Videos

- arXiv ID: `2605.16544v1`
- Authors: Seyed Amir Mousavi, Xiaoyin Wang
- Published: 2026-05-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.GR`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2605.16544v1) | [pdf](https://arxiv.org/pdf/2605.16544v1)

## Abstract

As Augmented Reality (AR) becomes more and more embedded in daily life, ensuring the quality, safety, and reliability of AR applications is increasingly important. However, AR apps present unique challenges for automated testing. Unlike static GUI layouts in traditional mobile apps, AR apps acquire their interaction interface from the surrounding environment, which is volatile and non-deterministic. Recent advancements like ARCore Playback and ARKit Replay allow developers to reuse real-world scenarios by recording and playing back enriched videos, enabling more feasible automated AR testing. However, using playback videos introduces two major challenges: test inputs must be timed precisely, and interactive areas in the video are dynamic, irregular, and difficult to identify. To address these challenges, we propose TARIPlay, a framework that analyzes playback videos to detect, track, and filter proper interactive areas over time for automated testing. In particular, TARIPlay identifies viable test opportunities based on criteria like stability and visibility, then feeds this information to an automated testing engine to simulate user interactions. We perform an experiment with four open-source AR apps and nine playback videos. Evaluation results show that TARIPlay significantly outperforms the existing tool Monkey in test coverage (55.8% over 41.98% on branch coverage) of AR-related code, and can also be used to assess the quality of playback videos for testing suitability.
