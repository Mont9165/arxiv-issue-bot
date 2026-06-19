# CoRaCommit: A VS Code Extension for Commit Message Generation with Exemplar Retrieval

- arXiv ID: `2606.19814v1`
- Authors: Chaoran Cai, Bo Xiong, Chong Wang, Lulu He, Peng Liang
- Published: 2026-06-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.19814v1) | [pdf](https://arxiv.org/pdf/2606.19814v1)

## Abstract

Commit messages are essential textual artifacts that describe the intent behind code changes, and play a critical role in version control, code review, and historical tracking. However, in practice, commit messages are primarily authored manually, which is time-consuming and often results in inconsistent quality and non-uniform expression. Existing VS Code extensions for commit message generation typically directly invoke large language models based on the code diff, without leveraging similar commit exemplars as references, and rarely support user feedback-driven LLM recommendation. To address these limitations, this paper presents CoRaCommit, a VS Code extension that enhances commit message generation by retrieving similar commit exemplars as prompt context, invoking multiple LLMs in parallel for candidate commit message comparison, and dynamically recommending LLMs based on user feedback. Experimental results on 945 commits from the ApacheCM dataset show that CoRaCommit outperforms existing VS Code extensions across BLEU, CIDEr, METEOR, and ROUGE-L metrics, demonstrating the effectiveness of retrieval-augmented context for commit message generation.
