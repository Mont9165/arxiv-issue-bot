# LLM-based Hardware Development with Hierarchical IRs and End-to-End Multi-Agent Workflow

- arXiv ID: `2608.30659v1`
- Authors: Chenyang Yin, Agasthi Haputhanthri, Aditya Anirudh Jonnalagadda, Zhenyu Bai, Yuanming Song, Saranyu Chattopadhyay, Mohammad Fadiheh, Tom Zelazny, Subhasish Mitra, Tulika Mitra
- Published: 2026-08-31
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30659v1) | [pdf](https://arxiv.org/pdf/2608.30659v1)

## Abstract

Large language models (LLMs) are increasingly used in software development, but their use in complex hardware design remains limited. This gap stems from both the scarcity of public hardware training data and the fundamentally different methodologies used in hardware design. In particular, applying LLMs to hardware requires more than direct RTL generation: the model must understand module boundaries, inter-module connections, and verification requirements. In this paper, we present an LLM-based hardware development framework with hierarchical intermediate representations (IRs) and an end-to-end multi-agent workflow. The core idea is to provide an abstraction of hardware design to LLMs through two structured IRs: Architectural Sketch, which captures module topology and interconnection, and Operational Specification, which defines per-module functionality and interfaces. Our framework uses these IRs to decompose a complex design into sub-modules, specify the per-block functionality, and derive how each module should be tested and verified. We incorporate a multi-agent debug loop in the framework, allowing agents to get the error feedback and control the debug details such as the signals to be probed for simulation. We evaluate our framework on Verilog-Eval benchmark, achieving a pass@5 rate of 95.5%, which surpasses current state-of-the-art LLM generation frameworks. To better assess performance on complex, realistic designs, we introduce a new case study spanning applications from general-purpose processors to digital signal processing systems. Experimental results indicate that such complex designs exceed the capabilities of existing approaches, whereas our framework is the only one capable of producing functional end-to-end design. Our generated RTL follows all industry-standard design rules, is lint-clean, functionally correct and fully synthesizable.
