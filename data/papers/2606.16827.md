# No Resource, No Benchmarks, No Problem? Evaluating and Improving LLMs for Code Generation in No-Resource Languages

- arXiv ID: `2606.16827v1`
- Authors: Alessandro Giagnorio, Alberto Martin-Lopez, Gabriele Bavota
- Published: 2026-06-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.16827v1) | [pdf](https://arxiv.org/pdf/2606.16827v1)

## Abstract

Large Language Models (LLMs) have significantly advanced the automation of software engineering tasks. One prominent example is code generation, where an LLM produces code in a specified programming language based on a natural language description. Most research in this area has focused on high-resource languages, such as Python or Java, which benefit from abundant training data. A smaller body of work has explored low-resource languages, which are underrepresented in training corpora. In contrast, no-resource languages for which LLMs have seen virtually no training data remain largely unstudied. These languages often emerge in industry, where organizations develop proprietary or domain-specific languages unsupported by commercial tools like GitHub Copilot. This results in the need for companies to deploy their own in-house code recommenders. To investigate possible solutions in this context, we build and release three code generation benchmarks for no-resource languages, based on two recently proposed programming languages for which very little training data is available. Using these benchmarks, we experiment several solutions to teach LLMs about no-resource languages, including prompt-based techniques as well as pre-training and fine-tuning exploiting the little data available. While further pre-training gives the largest performance gains for no-resource languages, applying it directly to instruction-tuned models harms their ability to follow instructions. To address this, we start from a base model, further pre-training it on the target language, and then inject instruction-following capabilities via weight diff transfer from an instruction model. Such an approach significantly improves code generation capabilities in no-resource settings, allowing companies to cheaply deploy a specialized instruct model without dealing with the computational cost of instruction fine-tuning.
