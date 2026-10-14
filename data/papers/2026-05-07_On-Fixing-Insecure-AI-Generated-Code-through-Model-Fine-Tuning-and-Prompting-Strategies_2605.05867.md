# On Fixing Insecure AI-Generated Code through Model Fine-Tuning and Prompting Strategies

- arXiv ID: `2605.05867v1`
- Authors: Ali Soltanian Fard Jahromi, Amjed Tahir, Peng Liang, Foutse Khomh
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.05867v1) | [pdf](https://arxiv.org/pdf/2605.05867v1)

## Abstract

The security of AI-generated code remains a major obstacle to its widespread adoption. Although code generation models achieve strong performance on functional benchmarks, their outputs frequently contain bugs and security weaknesses that undermine their trustworthiness. Prior work has explored a range of approaches to mitigate security issues in AI-generated code, e.g., using static analysis-guided generation and prompt engineering. However, their effectiveness varies widely across models and settings. This paper presents a systematic investigation of strategies for hardening model-generated code against a list of Common Weakness Enumeration (CWE). We assess the extent to which these strategies improve security across models and programming languages, using fine-tuning and prompting approaches for model output refinement. Beyond the prevalence of security weaknesses, we analyse the severity of identified CWEs, their co-occurrence, and the unintended consequences of remediation (i.e., whether fixing certain weaknesses introduces new weaknesses elsewhere in the same code). Our results show that security improvements are highly strategy- and model-dependent. Although some approaches reduce specific classes of weaknesses, they often introduce new weaknesses as side effects of the fixes. Moreover, no strategy consistently eliminates weaknesses across all models and scenarios, highlighting the absence of a universally effective "bulletproof" solution for secure AI-generated code.
