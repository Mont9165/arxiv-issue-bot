# Balancing Usefulness and Naturalness: An LLM-based Curation Pipeline for Code Review Comments

- arXiv ID: `2607.09524v1`
- Authors: Oussama Ben Sghaier, Martin Weyssow, Houari Sahraoui
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09524v1) | [pdf](https://arxiv.org/pdf/2607.09524v1)

## Abstract

Code review is a cornerstone of software development, where reviewers provide feedback through written comments to ensure code quality, maintainability, and correctness. The effectiveness of this process hinges on the quality of review comments. As large language models (LLMs) gain traction in automating code review tasks, the utility of these systems is directly limited by the quality of the datasets on which they are trained. Unfortunately, existing code review datasets are often noisy, inconsistent, or poorly structured, which hinders the ability of LLMs to learn to generate accurate, helpful, and human-like review comments.
  To overcome these limitations, we propose two different curation pipelines designed to improve both the quality and the utility of large-scale code review datasets. In the first pipeline, all review comments are systematically reformulated by an LLM to improve their clarity, conciseness, and civility while preserving their semantic intent. The curated dataset resulting from this approach, called CuREV, offers cleaner, higher-quality, and easier-to-learn-from comments that lead to measurable improvements in downstream automation tasks, namely review comment generation and code refinement. Building on this, we propose an improved pipeline, guided by high-quality exemplars, that enhances the realism and diversity of curated review comments. This method first separates the dataset into high-quality and low-quality reviews, based on a systematic quality assessment using an evaluation framework. High-quality comments are preserved in their original form and further used as in-context exemplars to inspire the reformulation of low-quality comments. By varying the exemplars provided, the reformulated comments are not only clearer and more actionable but also exhibit a broader range of writing styles, making them more realistic and human-like.
