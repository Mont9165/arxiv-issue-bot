# Distilling Reasoning Traces into Advisory Prompts for Software Engineering Tasks

- arXiv ID: `2608.00437v1`
- Authors: Faizan Faisal, Prem Devanbu, Toufique Ahmed
- Published: 2026-08-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.00437v1) | [pdf](https://arxiv.org/pdf/2608.00437v1)

## Abstract

Language models are widely used for generating and otherwise processing code (e.g., identifying code hallucinations, possible inputs, or predicting outputs); however, LLMs can make mistakes, which can be serious. One key issue is that models are trained on (still) largely human-written, and thus imperfect, code; it's not easy to find sufficiently large code corpora that are entirely free of bugs. Thus, other inference-time ways of reducing LLM errors, without additional training, are desirable. "Reasoning" or "thinking" modes, exposed as a togglable feature by hybrid reasoning models, do reduce errors; however, reasoning consumes additional resources. This paper asks if better performance can be achieved without always incurring the cost of reasoning. Human students of programming learn to avoid mistakes by (a) identifying them, (b) reflecting upon the cognitive lapses that led to them (essentially, "thinking through" the errors), (c) inferring general rules or lessons from these reflections, and (d) internalizing these lessons into rules. In tutorial sessions with an instructor, this is a common Socratic interaction. Examples of such internalizable rules might include the nugget "Before coding, restate the requirements to clarify them." Inspired by this process, this paper describes an approach where we first identify examples in which "thinking mode" in a (low-resource) LLM avoids errors. These errors, and their avoidance via "thinking" in the same LLM, are then examined by a bigger LLM to generate summary explanations; these are then summarized by a large LLM into brief advisory prompts. This approach works on many modest-sized models; in some cases, the "advisory prompts" thus learned can also be gainfully transferred to other models. We also present investigations into the nature of coding errors that language models make, and a characterization of when this approach can be helpful.
