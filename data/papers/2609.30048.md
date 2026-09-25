# Style, Not Self: Surface Cues Explain Zero-Shot Code Attribution by Large Language Models

- arXiv ID: `2609.30048v1`
- Authors: Ehsan Barkhordar, Surendrabikram Thapa
- Published: 2026-09-24
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.30048v1) | [pdf](https://arxiv.org/pdf/2609.30048v1)

## Abstract

If a language model can recognize code it wrote, it may favor that code as a judge, and instances of one model monitoring each other could collude. We test this zero-shot on current commercial models. Five LLMs generate solutions to MBPP, HumanEval, and DS-1000, seven more to MBPP, and models act as evaluators in four tasks: picking their own solution from a pair, judging whether a single solution is their own, identifying which of two solutions a named model wrote, and judging quality blind. In the single-solution task, balanced accuracy is 49-58% for all 15 model-benchmark combinations, while raw accuracy (38-67%) mostly reflects how readily a model claims authorship. In the pairwise task, accuracy across 14 evaluator-opponent combinations correlates at r=0.93 with how often the evaluator's solution is longer. Attribution to a named model succeeds on some pairs and is consistently inverted on others. A rule-based normalization that strips docstrings, comments, type hints, and local names preserves Pass@1 and leaves ten of twelve re-tested results at chance; the other two follow a length difference it leaves, although a trained classifier still separates most normalized pairs. Claude Haiku's self-preference also disappears. We recommend reporting balanced accuracy, heuristic baselines, and label consistency.
