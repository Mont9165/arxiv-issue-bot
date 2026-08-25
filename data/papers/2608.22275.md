# CodeMechanic: Bug-Property-Guided Program Mitigation

- arXiv ID: `2608.22275v1`
- Authors: Han Zheng, Rafaila Galanopoulou, Ilia Shumailov, Tianqi Fan, Aiden Hall, Dominik Maier, Mathias Payer
- Published: 2026-08-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2608.22275v1) | [pdf](https://arxiv.org/pdf/2608.22275v1)

## Abstract

Automated testing discovers vulnerabilities faster than developers can investigate and repair them, leaving an interval in which known memory corruptions remain exploitable. End- to-end LLM repair agents can shorten this interval, but they synthesize open-ended code changes and commonly validate them only by replaying a proof of concept (PoC). This weak oracle accepts patches that silence the observed crash by changing unrelated behavior, making unintended deployment risky.
  We present CodeMechanic, a bug-property-guided system for generating constrained mit- igations for spatial memory corruption. Instead of asking an LLM to generate a permanent repair, CodeMechanic reconstructs the violated memory-safety property from the crash, validates the dereferenced pointer and its buffer range, and inserts a local fail-stop guard before the dangerous access. The guard terminates execution when the boundary check fails. The resulting mitigation deliberately trades availability for security: it can convert potential remote code execution into controlled termination while developers investigate the root cause and prepare a permanent repair. CodeMechanic combines a two-dimensional static and dynamic context extractor with in-prompt debugging knowledge and stepwise val- idation to limit the effect of LLM errors. On 101 real-world ARVO bugs, the first attempt of CodeMechanic produces 47.6% more plausible patches (i.e., patches that pass PoC- replay validation) than the best baseline while using 91% fewer tokens. Manual audit further shows that CodeMechanic produces 3.4x - 4.3x more patches semantically equivalent to developer-written repairs.
