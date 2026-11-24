# POMA: Beyond Final Flags -- Process-Level Evaluation of Base LLMs in Vulnerability Exploitation

- arXiv ID: `2611.30590v1`
- Authors: Gufeng Zhang, Yiru Zhao, Shengyu Liu, Weichen Yan, Xingwang Xiang, Yiran Ma, Benxiao Tang, Lei Zhao, Jinxin Ma
- Published: 2026-11-23
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.30590v1) | [pdf](https://arxiv.org/pdf/2611.30590v1)

## Abstract

As large language models (LLMs) evolve from text generation to autonomous software-engineering execution, automated vulnerability exploitability verification has emerged as a vital frontier in software quality assurance and security validation. Existing security benchmarks, however, largely judge models by binary pass/fail outcomes or coarse stage milestones. Such outcome-centric scoring obscures fine-grained failure dynamics across long-horizon execution and conflates the intrinsic capability of a base LLM with external agent scaffolding. We present POMA (Pwn-Oriented Model Assessment), a process-level evaluation methodology and platform that isolates base LLMs under a unified execution baseline -- fixing task inputs, tool interfaces, target environments, feedback formats, and execution budgets -- while measuring intermediate states and transitions from runtime evidence. Evaluating four frontier base LLMs across 55 CTF Pwn challenges and 10 real-world vulnerability reproduction tasks exposes persistent capability attrition along the exploitation chain: from vulnerability knowledge to executable implementation, from client-side actions to verified target states, from failure localization to precise repair, and across iterative revisions. In real-world software, models further struggle to satisfy format, semantic, differential, and crash-identity constraints simultaneously. By pinpointing where execution chains break down, POMA provides an empirical foundation for trustworthy capability assessment and principled vulnerability-agent design. Our benchmark catalogs, process-measurement evaluator, and sample harness are publicly available at https://github.com/maple-pwn/poma-release .
