# Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors

- arXiv ID: `2608.20896v1`
- Authors: Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju
- Published: 2026-08-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2608.20896v1) | [pdf](https://arxiv.org/pdf/2608.20896v1)

## Abstract

Programming error messages are critical for software development, yet they remain difficult for novice programmers to interpret. While Large Language Models (LLMs) can rewrite these errors into clearer explanations, it remains unclear whether increased readability improves objective debugging performance or how explanation styles should align with programmer skill. We present a multi-stage crowdsourced study N=103 evaluating skill-targeted, LLM-generated Python error messages. Using a custom proficiency assessment, we categorized participants by skill level and tested standard interpreter messages against two LLM-generated styles: pragmatic (action-oriented) and contingent (scaffolded explanations). We measured both objective debugging metrics (fix rate, attempts, time-to-fix) and subjective perceptions (readability, cognitive load, tone). Our results show that while LLM-rewritten messages significantly improved subjective evaluations, with pragmatic messages rated as clearer and less cognitively demanding, these perceived gains did not translate into statistically significant improvements in objective debugging performance. This highlights a critical human-AI complementarity gap: explanations that feel better to users do not necessarily make them more effective debuggers. We discuss design implications for adaptive AI feedback systems, arguing that future tools should pivot from static skill-targeted rewriting toward dynamic adjustments based on a user's real-time repair trajectory.
