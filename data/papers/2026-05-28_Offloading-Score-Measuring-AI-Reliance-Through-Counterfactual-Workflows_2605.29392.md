# Offloading Score: Measuring AI Reliance Through Counterfactual Workflows

- arXiv ID: `2605.29392v1`
- Authors: Vishakh Padmakumar, Lujain Ibrahim, Zora Zhiruo Wang, Jennifer Wang, Q. Vera Liao, Diyi Yang
- Published: 2026-05-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.CY`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2605.29392v1) | [pdf](https://arxiv.org/pdf/2605.29392v1)

## Abstract

AI tools are increasingly integrated into real-world workflows. However, existing measures of reliance on these tools focus on AI output adoption or on self-reported indicators, rather than how task effort is distributed between users and tools. Here, we introduce offloading score, a measure of reliance that quantifies the fraction of cognitive effort offloaded to an AI tool. Offloading Score is simulation-based -- we construct a counterfactual workflow by estimating how the user would have completed the task without the tool, and then computing the fraction of steps saved by using the tool. We validate offloading score through intrinsic evaluations of metric validity, and a controlled user study ($n=40$) with developers performing programming tasks using AI tools. We vary time pressure to test whether reliance measures capture the known increase in reliance under time pressure. We show that offloading score detects significantly higher reliance in time-constrained settings ($+43\%$, $p=0.018$), while usage-based and self-reported baseline measures of reliance do not distinguish the conditions. We complement this with descriptive insights showing that higher reliance manifests as greater delegation of subtasks to the tool and more direct reuse of AI outputs. Finally, we demonstrate an approach of using offloading score in combination with target outcomes of a task (e.g., code understanding) to identify when reliance may be (in)appropriate. Our framework offers two contributions: an instrument users can apply to measure and reflect on their own reliance, and a quantitative signal that agent designers can utilize to mitigate overreliance.
