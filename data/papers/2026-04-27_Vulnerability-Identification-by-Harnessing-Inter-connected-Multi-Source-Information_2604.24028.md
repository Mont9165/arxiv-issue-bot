# Vulnerability Identification by Harnessing Inter-connected Multi-Source Information

- arXiv ID: `2604.24028v1`
- Authors: Liyou Chen, Hailong Sun, Xiang Gao, Lin Shi, Yixin Yang, Yi Xu
- Published: 2026-04-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.24028v1) | [pdf](https://arxiv.org/pdf/2604.24028v1)

## Abstract

The utilization of third-party open-source libraries is widespread in modern software development. Due to the dependency relationships, vulnerabilities within open-source libraries pose significant security threats to downstream software. However, the library vulnerabilities are usually implicitly reported and patched, without explicit notification to dependent software, leaving the downstream software vulnerable to potential attacks. Existing research efforts primarily focus on identifying vulnerability patches according to bug reports, commit messages, or code changes, overlooking the rich semantic connections among various sources of information. In this paper, our main insight is that various sources of information, including the vulnerability descriptions (e.g., bug reports) and its fixing strategies (e.g., commit messages and code changes), are highly interconnected. They express the high-level semantic information about the symptom, root cause and fixing strategies of the bugs. Hence, we propose an approach that involves training an AI model to integrate multiple sources, thus enhancing the effectiveness of vulnerability identification and vulnerability type classification. We introduce VPFinder, a tool that utilizes multi-head attention mechanisms to extract high-level semantic information from diverse sources. Evaluation results demonstrate that VPFinder achieves remarkable 0.941 F1-score in vulnerability identification task and 0.610 F1-score in vulnerability type classification task, outperforming state-of-the-art approaches by 5.4%.
