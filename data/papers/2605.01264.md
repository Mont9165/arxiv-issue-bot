# FeedbackLLM: Metadata driven Multi-Agentic Language Agnostic Test Case Generator with Evolving prompt and Coverage Feedback

- arXiv ID: `2605.01264v1`
- Authors: Kushal Jasti, Tejamani Prashanth Sahu, Rishitha Pentyala, Muvvala Mohit, Vivek Yelleti
- Published: 2026-05-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.01264v1) | [pdf](https://arxiv.org/pdf/2605.01264v1)

## Abstract

Traditional approaches to test case generation often involve manual effort and incur significant computational overhead. Additionally, these approaches are not scalable, and hence, unsuitable for complex software systems. Recently, Large Language Models (LLMs) have been applied to software testing. However, single-shot prompt engineering-based approaches tend to hallucinate and generate redundant test cases, resulting in fewer branches. To handle the above-mentioned limitations, in this paper, we propose FeedbackLLM, a novel automated language-agnostic test case generation framework based on tightly coupled two-stage approach. In the first stage, FeedbackLLM extracts the input constraints by parsing source code and generates the possible test cases. The quality of the test cases is evaluated in the second stage by the following two specialized LLM feedback agents: (i) Line Feedback Agent: extracts the metadata related to missed line executions and (ii) Branch Feedback Agent: extracts the metadata of the unexecuted branch conditions. The above agents operate in a two-stage process, communicating in tandem, and this procedure is repeated for k-steps. Further, we also introduced a redundancy prevention cache to avoid duplicate API requests and avoid unnecessary execution cycles. The performance of the proposed architecture is evaluated on the standard benchmark programs related to C and Python programs. FeedbackLLM demonstrated more line and branch coverage than baseline tools while scaling linearly in execution time.
