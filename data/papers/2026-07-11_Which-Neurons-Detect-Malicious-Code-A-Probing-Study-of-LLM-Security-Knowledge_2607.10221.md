# Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge

- arXiv ID: `2607.10221v1`
- Authors: Lam D. Dao, Vang T. Nguyen, Anh M. T. Bui, Phuong T. Nguyen
- Published: 2026-07-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.10221v1) | [pdf](https://arxiv.org/pdf/2607.10221v1)

## Abstract

Background. Large language models (LLMs) have become increasingly capable of understanding and generating source code, leading to their widespread adoption in software engineering tasks such as code completion, repair, and vulnerability detection. However, despite their strong empirical performance, the internal mechanisms through which LLMs recognize malicious or vulnerable code patterns remain poorly understood. Aim. We investigated where the malware detection behavior is encoded inside LLMs Feed Forward Network (FFN) neurons and verified the attribution with causal interventions on the neurons identified. This aims to identify the most important neurons in detecting malicious code. Methods. We applied mechanistic interpretability methods to locate the neurons being responsible for malware-detection behavior in three instruction-tuned LLMs: Llama3.1-8B-Instruct, Mistral-v0.3-7B-Instruct, and Qwen2.5-7B-Instruct. Using 1,500 malicious and 1,500 benign PyPI packages from the PyPI Malregistry, we attribute the behavior to a set of neurons. Results. The experimental results reveal that amplifying facilitating neurons for malware detection while suppressing inhibiting ones can boost accuracy, while the reverse collapses predictions toward a single class, although the magnitude and consistency is heavily model-dependent. We demonstrated that the guardrail detection mechanism varies across models, each represents its malware detection behavior differently within its FFN layers. Conclusions. Probing the neurons associated with security-relevant knowledge helps us gain insights into how LLMs encode malicious programming concepts, identify potentially harmful memorized behaviors, paving the way toward more reliable defense mechanisms, such as neuron-level editing, selective unlearning, and security-aware alignment for code-focused LLMs.
