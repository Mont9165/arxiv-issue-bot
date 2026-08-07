# Knowledge-Enhanced Agentic Vulnerability Repair

- arXiv ID: `2607.00820v1`
- Authors: Sicong Cao, Hao Ma, Le Yu, Kangyi Ding, Xiaolei Liu, Terry Yue Zhuo, Bo Wang, Xingwei Lin, Xiaobing Sun, Linzhang Wang, David Lo
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00820v1) | [pdf](https://arxiv.org/pdf/2607.00820v1)

## Abstract

Frontier foundation models have changed the math on vulnerability discovery, but the bigger challenge is how the remediation side keeps up. Despite recent progresses in Automated Vulnerability Repair (AVR), current solutions struggle to reliably identify the root causes of vulnerabilities, and insufficiently utilize the prior fix knowledge to guide the patch generation process, thus undermining their effectiveness in practice.
  To address this gap, we propose KeaRepair, a novel agentic AVR approach that grounds patch generation in verified program facts and high-level vulnerability knowledge. Specifically, KeaRepair first extracts multi-dimensional vulnerability knowledge from historical vulnerability-patch pairs from dual complementary views, and constructs dedicated retrieval knowledge bases. It then employs a tool-augmented agent that performs ReAct-style reasoning to collect verified program facts for vulnerability diagnosis. Finally, based on the diagnostic results, KeaRepair performs knowledge-level retrieval-augmented patch generation and iteratively refines patches through a closed-loop validation process involving compilation, PoC replay, and test-suite execution. Experimental results show that KeaRepair significantly outperforms existing AVR approaches on 55 reproducible C/C++ vulnerabilities. When paired with Gemini-3.1-Pro, KeaRepair successfully repairs 46 vulnerabilities, achieving a repair rate of 83.64%. Moreover, KeaRepair fixes six unique vulnerabilities that none of the baselines can address, and further demonstrates strong cross-language generalizability.
