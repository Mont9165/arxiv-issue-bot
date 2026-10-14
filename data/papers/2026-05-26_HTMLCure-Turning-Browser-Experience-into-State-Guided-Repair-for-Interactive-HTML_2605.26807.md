# HTMLCure: Turning Browser Experience into State Guided Repair for Interactive HTML

- arXiv ID: `2605.26807v1`
- Authors: Jiajun Wu, Jian Yang, Tuney Zheng, Wei Zhang, Haowen Wang, Yihang Lou, Xianglong Liu
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.26807v1) | [pdf](https://arxiv.org/pdf/2605.26807v1)

## Abstract

LLMs can now produce full HTML pages, but many of those pages are only superficially correct: they render once, then fail under scroll, hover, click, resize, or gameplay. Evaluation from screenshots can miss these failures, and filtering discards many pages that are still repairable. We introduce HTMLCure, a browser experience framework that evaluates HTML after the system has interacted with it. The evaluator executes the page across viewports and interaction states, records deterministic browser evidence, and gives the VLM curated keyframes from the executed trajectory rather than isolated screenshots. The same state signal drives a closed loop repair engine: HTMLCure diagnoses the current page, chooses a state specific repair family, runs each candidate again, and exports quality cleared pages for SFT. On a 97K prompt corpus, this expands the directly usable seed into a candidate pool of 63703 quality cleared pages, from which we construct the final refined SFT set of 40K pages. Under the same backbone and training recipe, HTMLCure-27B-Refined reaches 50.6 on HTMLBench-400 with 45.2% deterministic test case pass, placing it in the same performance band as strong reference rows such as Kimi-K2.6 and GPT-5.4. On the released MiniAppBench validation split, it reaches 81.2 average, improving raw 27B SFT by 15.3 points and approaching the level of strong reference systems.
