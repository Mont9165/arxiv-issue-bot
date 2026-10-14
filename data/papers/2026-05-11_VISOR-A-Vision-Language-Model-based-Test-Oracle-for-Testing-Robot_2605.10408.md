# VISOR: A Vision-Language Model-based Test Oracle for Testing Robot

- arXiv ID: `2605.10408v1`
- Authors: Prasun Saurabh, Pablo Valle, Aitor Arrieta, Shaukat Ali, Paolo Arcaini
- Published: 2026-05-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.RO`
- Links: [abs](http://arxiv.org/abs/2605.10408v1) | [pdf](https://arxiv.org/pdf/2605.10408v1)

## Abstract

Testing robots requires assessing whether they perform their intended tasks correctly, dependably, and with high quality, a challenge known as the test oracle problem in software testing. Traditionally, this assessment relies on task-specific symbolic oracles for task correctness and on human manual evaluation of robot behavior, which is time-consuming, subjective, and error-prone. To address this, we propose VISOR, a Vision-Language Model (VLM)-based approach for automated test oracle assessment that eliminates the need of expensive human evaluations. VISOR performs automated evaluation of task correctness and quality, addressing the limitations of existing symbolic test oracles, which are task-specific and provide pass/fail judgments without explicitly quantifying task quality. Given the inherent uncertainty in VLMs, VISOR also explicitly quantifies its own uncertainty during test assessments. We evaluated VISOR using two VLMs, i.e., GPT and Gemini, across four robotic tasks on over 1,000 videos. Results show that Gemini achieves higher recall while GPT achieves higher precision. However, both models show low correlation between uncertainty and correctness, which prevents using uncertainty as a correctness predictor.
