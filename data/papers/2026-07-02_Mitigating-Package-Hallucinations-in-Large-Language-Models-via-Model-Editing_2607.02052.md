# Mitigating Package Hallucinations in Large Language Models via Model Editing

- arXiv ID: `2607.02052v1`
- Authors: Shuhan Liu, Yukai Zhao, Xing Hu, Kui Liu, Xiaohu Yang, Xin Xia
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.02052v1) | [pdf](https://arxiv.org/pdf/2607.02052v1)

## Abstract

Large language models (LLMs) have demonstrated strong capabilities in software engineering tasks, such as code generation, library recommendation, and dependency configuration. However, recent studies show that LLMs may suffer from package hallucination, where they generate non-existent or invalid package names. These hallucinations can be exploited in software supply chain attacks, as attackers may register malicious packages under hallucinated names. Therefore, mitigating package hallucination is important for improving the reliability and security of LLM-assisted software development. In this paper, we introduce BOUND, a lightweight localized model editing framework for mitigating package hallucinations in LLMs. BOUND formulates package hallucination mitigation as a package-validity boundary editing problem, where the boundary refers to the model's ability to distinguish valid packages from hallucinated package names under a given task context. It first locates modules related to package hallucination through a risk-aware localization strategy, and then edits these modules with lightweight LoRA adapters using a boundary-aware objective that reinforces valid packages, suppresses hallucinated packages, and preserves locality behavior. Experimental results show that BOUND effectively reduces package hallucinations while preserving valid package recommendations. In the package recommendation task, BOUND reduces package-level hallucination rate (Package-HR) by 79.9% on edit prompts and by 65.4% on unseen prompts. The learned package-validity boundary further generalizes to other package-related tasks, reducing Package-HR by 12.8% in code generation and by 34.0% in pip install recommendation. These results show that BOUND refines the package-validity boundary of LLMs and improves the reliability of package-related outputs.
