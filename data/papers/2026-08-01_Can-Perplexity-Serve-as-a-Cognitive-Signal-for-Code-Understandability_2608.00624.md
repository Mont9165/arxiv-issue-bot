# Can Perplexity Serve as a Cognitive Signal for Code Understandability?

- arXiv ID: `2608.00624v1`
- Authors: Xiaokai Rong, Mohammadali Sefidi Esfahani, Aashish Yadavally, Rigby Peter, Tien N. Nguyen
- Published: 2026-08-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.00624v1) | [pdf](https://arxiv.org/pdf/2608.00624v1)

## Abstract

Recent work suggests that token-level perplexity from large language models can align with localized human confusion during code comprehension. This raises a natural question: can perplexity also serve as a snippet-level signal for code understandability? We conduct an empirical study of this question across multiple human-grounded datasets, including method-level understandability judgments, output-prediction tasks, and accepted understandability-improvement patches. Despite prior token-level evidence, we find that simple snippet-level aggregations of token perplexity, such as average, median, or peak perplexity, do not reliably correlate with human understandability. We then investigate why this happens. First, token perplexity is highly skewed and heavy-tailed across code structures; extreme spikes arise not only from semantically meaningful constructs, but also from identifiers, literals, types, separators, and tokenization artifacts. Second, human understandability labels often lack consensus, making whole-snippet difficulty a noisy target. Third, perplexity distributions and their alignment with human difficulty vary substantially across models and tokenizers. These findings explain why prior token-level perplexity--confusion alignment does not directly transfer to snippet-level understandability. Overall, our study positions perplexity as a promising but delicate cognitive signal: useful for localized code confusion, but requiring code-aware aggregation, consensus-aware evaluation, and model-sensitivity analysis before it can support reliable code-understandability measurement.
