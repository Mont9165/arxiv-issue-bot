# DIG: Oracle-Guided Directed Input Generation for One-Day Vulnerabilities

- arXiv ID: `2606.13037v1`
- Authors: Andrew Bao, Haochen Zeng, Peng Chen, Stephen McCamant, Pen-Chung Yew
- Published: 2026-06-11
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.13037v1) | [pdf](https://arxiv.org/pdf/2606.13037v1)

## Abstract

One-day vulnerabilities pose significant risks due to delayed or incomplete patch adoption. Generating proof-of-concept (PoC) inputs is therefore essential for assessing real-world impact. The key challenge is identifying necessary constraints for triggering the vulnerability and solving them effectively. Existing directed fuzzing approaches prioritize inputs toward target locations, but neither explicitly identify necessary constraints nor solve them effectively, relying instead on target-distance feedback and random mutation. Agentic approaches show strong potential through code reasoning and structured input generation, but goal drift in long-horizon reasoning limits their effectiveness.
  DIG addresses this challenge by exploiting a key property of one-day vulnerabilities: patches often reveal necessary preconditions for triggering. DIG uses an LLM to analyze the patch and synthesize an oracle making these conditions explicit. The oracle supports effective PoC generation at two levels. At the high level, DIG performs oracle-guided generator evolution, where an agent infers and solves constraints to satisfy the oracle. At the low level, DIG instruments the oracle into the target program and uses branch-distance feedback to guide random mutation in directed fuzzing. Evaluation shows DIG outperforms 2 state-of-the-art agents and 10 fuzzers across 138 real-world CVEs. DIG triggers 80 vulnerabilities, surpassing prior results and outperforming the best baseline by 40% (57 vs. 80 CVEs). Notably, DIG exclusively triggers 9 vulnerabilities no existing technique can trigger. Compared to the average of other tools, DIG triggers vulnerabilities faster in 92.9% of cases, achieving over 100x speedup in 48.8% of cases, with a maximum speedup of 3,664x. Beyond one-day PoC generation, DIG uncovers 6 previously unknown vulnerabilities in widely deployed libraries, enabling zero-day discovery.
