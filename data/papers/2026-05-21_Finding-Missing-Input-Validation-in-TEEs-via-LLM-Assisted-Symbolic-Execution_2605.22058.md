# Finding Missing Input Validation in TEEs via LLM-Assisted Symbolic Execution

- arXiv ID: `2605.22058v1`
- Authors: Chengyan Ma, Jieke Shi, Ruidong Han, Ye Liu, Yuqing Niu, David Lo
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.22058v1) | [pdf](https://arxiv.org/pdf/2605.22058v1)

## Abstract

Trusted Execution Environments (TEEs) provide hardware-enforced isolation that protects sensitive code and data from untrusted software. Despite their strong security guarantees, analyzing TEE applications remains challenging due to the high cost and complexity of configuring complete TEE build and runtime environments, as well as the limited observability imposed by hardware isolation. This paper presents SymTEE, a novel large language model (LLM)-assisted symbolic execution framework for detecting missing input validation issues in TEE applications without requiring real TEE setups. SymTEE begins by leveraging Abstract Syntax Tree (AST) analysis to extract TEE code slices that may lack sufficient input validation, and then employs an LLM (GPT-5 in our case) to automatically convert the extracted slices into KLEE-compatible harness programs containing lightweight mock execution environments for symbolic analysis. Evaluations on 26 vulnerabilities (11 real-world and 15 synthetic) show that SymTEE achieves 100% precision and 92.3% recall in detecting missing input validation vulnerabilities while incurring an average analysis cost of only $0.05. These results demonstrate the effectiveness and practicality of SymTEE's pioneering paradigm of LLM-assisted symbolic execution, where LLMs autonomously generate mock environments to enable automated security analysis without complex setup, providing a more accessible and scalable framework for trusted computing systems.
