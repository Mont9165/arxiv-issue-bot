# Vibenix: Agentic Software Packaging and Maintenance with Nix

- arXiv ID: `2610.24712v1`
- Authors: Martim Monis, Martin Schwaighofer, Nuno Saavedra, Alexandra Mendes, Rene Mayrhofer, João F. Ferreira
- Published: 2026-10-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.24712v1) | [pdf](https://arxiv.org/pdf/2610.24712v1)

## Abstract

Implicit dependencies, uncontrolled network access, and other build-environment impurities create intransparent software supply chains. Identifying every dependency affecting a build is a difficult task. Functional package management addresses this through reproducible packaging, ensuring software relies exclusively on declared, hermetically isolated inputs. However, creating build recipes remains complex and time-consuming, posing a significant barrier to adoption for developers and maintainers. We present Vibenix, an open-source AI-powered agent that bridges this gap by automatically generating Nix packaging expressions. Vibenix uses a large language model (LLM) to iteratively refine recipes through a rule-guided build-repair feedback loop. On 466 packaging tasks from our new NixBench dataset, Vibenix produced buildable packages in 95.3% of cases using Claude Haiku 4.5, compared with 5.6% for a state-of-the-art LLM-based single-shot packaging tool. Manual validation of 100 packages revealed that 47% of the buildable packages were initially functionally correct; a post-build refinement process based on the evaluator-optimizer pattern increased functional correctness by 35 percentage points. On our new NixBench-Repair dataset of package maintenance tasks, Vibenix achieved an 87.6% success rate. These results demonstrate how unreliable LLMs can generate rigorously defined, complete, auditable dependency trees for real-world software, reducing maintainer burden while providing a trustworthy foundation for secure software distribution.
