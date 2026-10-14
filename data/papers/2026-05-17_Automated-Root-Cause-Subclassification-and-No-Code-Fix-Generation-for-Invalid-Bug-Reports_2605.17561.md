# Automated Root-Cause Subclassification and No-Code Fix Generation for Invalid Bug Reports

- arXiv ID: `2605.17561v1`
- Authors: Mahmut Furkan Gon, Emre Dinc, Tevfik Emre Sungur, Eray Tuzun
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2605.17561v1) | [pdf](https://arxiv.org/pdf/2605.17561v1)

## Abstract

Issues faced when using software are reported in the form of bug reports. However, many bug reports are invalid, meaning they do not require code changes, and are resolved with a no-code fix. Manually determining the root cause of the invalid bug reports and providing actionable resolutions by the customer support causes a serious waste of resources. Our goal is to introduce a standardized taxonomy for root-cause oriented invalid bug report subclassification, and perform experiments to test the accuracy of various approaches on invalid subclassification and no-code fix generation. We study how different configurations perform on a gold-standard benchmark we have created. Using a manually curated benchmark for higher quality analysis, we experimented with vanilla LLMs, Retrieval Augmented Generation, and agentic web search to identify invalid subclasses and generate no-code fixes. We evaluated the results against manually labeled ground truth data that includes the invalid subclass and no-code fixes from the original bug reports. We measured subclass detection performance with weighted F1-Score, and assessed no-code fix suggestions using BERTScore and Judge LLM success rates. For subclassification, retrieval augmented generation achieves the highest overall performance with 0.66 weighted F1, slightly outperforming vanilla LLMs at 0.65 and agentic web search at 0.64. At the subclass level, performance peaks at 0.85 F1 for Non-reproducibility and 0.79 for Feature Request and Question, while Wrong Version remains the most challenging with scores between 0.00 and 0.29. For no-code fix generation, agentic web search achieves the highest overall Judge LLM success rate at 68.9%, compared to 64.4% for RAG applications and 64.9% for vanilla LLMs, with subclass-level peaks of 87.4% for Working as Designed and 72.2% for Question.
