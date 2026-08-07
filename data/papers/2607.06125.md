# Evaluating Fine-Tuning and Metrics for Neural Decompilation of Dart AOT Binaries

- arXiv ID: `2607.06125v1`
- Authors: Raafat Abualazm, Ayman AboElhassan, Amr G. Wassal
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.06125v1) | [pdf](https://arxiv.org/pdf/2607.06125v1)

## Abstract

Neural decompilation is increasingly studied as a code-generation problem, yet its evaluation methodology remains underdeveloped for modern languages. We present a systematic empirical study of fine-tuning effectiveness and metric validity for Dart Ahead-of-Time (AOT) neural decompilation. We evaluate six fine-tuned model variants across three base architectures (4B-8B parameters) using three metrics: CodeBLEU, compile@k, and pass@k on a new 154-task HumanEval-Dart benchmark. Our study yields three principal findings grounded in paired task-level statistical tests. First, no fine-tuning configuration produces a statistically significant pass@k improvement. The sole positive case yields +0.71 pp (McNemar p=0.21), while fine-tuning the strongest base (Qwen3-8B) causes a highly significant regression of -5.65 pp (p<0.001). This capacity-dependent trend is consistent across architectures but needs broader scale sweeps. Second, cross-lingual interference from Swift training is highly significant at 4B (-2.66 pp, p<0.001) but statistically indistinguishable from zero at 8B, consistent with the scaling hypothesis. Third, we demonstrate metric divergence: CodeBLEU and compile@k can improve significantly while pass@k moves in the opposite direction. This has implications for any LLM code generation task where fine-tuning targets superficial similarity. Error analysis reveals assembly sequence length is the strongest predictor of task difficulty (p=0.001), with a capability cliff at 200 instructions. We contribute the HumanEval-Dart benchmark, a Dart-adapted CodeBLEU, and empirical evidence that pass@k must be the primary evaluation metric for neural decompilation.
