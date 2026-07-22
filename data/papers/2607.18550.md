# Semantic Drift in Bug Resolution: How Behavioral Signals Propagate from Reports to Tests and Patches

- arXiv ID: `2607.18550v1`
- Authors: Wendkûuni C. Ouédraogo, Yinghua Li, Xueqi Dang, Paweł Borsukiewicz, Liang Xiao, Lingfeng Bao, Anil Koyuncu, Jacques Klein, David Lo, Tegawendé F. Bissyandé
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.18550v1) | [pdf](https://arxiv.org/pdf/2607.18550v1)

## Abstract

Bug resolution is a cross-artifact process: natural-language reports must expose actionable behavioral cues that can be reproduced by tests and corrected by patches. Yet the extent to which these signals are preserved across artifacts remains largely unquantified. We introduce Desc2Fix, a framework for measuring semantic alignment between bug reports, triggering tests, and developer-written fixes. Alignment is operationalized through structured behavioral anchors (e.g., reproduction steps, API/exception cues, expected vs. actual behavior), deterministic similarity metrics (ROUGE, SBERT, CodeBERT, OpenAI embeddings), and LLM-based judgments grounded in coverage, correctness, and specificity. We analyze 2,857 report-test-patch triplets from Defects4J and SWT-Bench using GPT-4o and DeepSeek-Chat. LLMs reliably extract structured signals (up to 90% completeness) and exhibit strong cross-model consistency, yielding a stable semantic input contract for downstream reasoning. However, alignment is highly representation-sensitive: lexical similarity alone is insufficient; full diffs provide the most stable basis for judging report-patch correspondence; and structured summaries trade surface similarity for predicate-level salience. Across more than 182,000 LLM alignment ratings, both models show systematic optimism relative to humans (1-2 points on 5-point scales) and only modest rank agreement, motivating bias-aware evaluation. Our results demonstrate that behavioral alignment is measurable but not reducible to similarity, and that structured anchors combined with embedding-based proxies provide reproducible signals for ranking and filtering tests and candidate patches. By transforming alignment into a controllable engineering signal, Desc2Fix enables more reliable test generation, semantics-aware fault localization, principled patch ranking, and improved bug report authoring.
