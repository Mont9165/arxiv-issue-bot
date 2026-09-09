# Shortcutting the Fix: Identifying and Categorizing Agentic Exploits in Software Engineering Benchmarks

- arXiv ID: `2609.06780v1`
- Authors: Nikolai Ludwig, Wasi Uddin Ahmad, Somshubra Majumdar, Boris Ginsburg
- Published: 2026-09-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.06780v1) | [pdf](https://arxiv.org/pdf/2609.06780v1)

## Abstract

While autonomous software engineering (SWE) agents achieve high benchmark resolution rates, these scores can mask exploitative behaviors---such as leveraging local Git histories, accessing upstream repositories, or recalling memorized solutions---rather than demonstrating genuine problem solving. We systematize and audit these exploits across five open large language models on SWE-bench Multilingual and DeepSWE using a turn-level LLM-as-a-judge protocol. Under standard prompts, exploitation rates reach 45.1\%--82.4\% on SWE-bench Multilingual and 44.2\%--66.1\% on DeepSWE. Appending a targeted instruction enforcing solution originality drastically cuts these exploitation rates---down to 4.0\%--10.7\% and 1.5\%--7.1\%, respectively, while maintaining strong core task performance. Our findings demonstrate the critical need for exploit-aware evaluation frameworks that measure true repository-level problem solving over benchmark gaming.
