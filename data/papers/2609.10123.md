# If It's Not Buggy, Don't Fix It: On the Dynamics of Iterative Bug-fixing with LLMs

- arXiv ID: `2609.10123v1`
- Authors: Xietao Wang-Lin, Anton Isopoussu, Louis Mahon
- Published: 2026-09-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2609.10123v1) | [pdf](https://arxiv.org/pdf/2609.10123v1)

## Abstract

Large language models (LLMs) have become ubiquitous in software development, with LLM-based automated program repair tools increasingly used during code review. In this report, we explore the iterative blind use of LLMs as bug-fixers. Across multiple models and repair environments, we find that LLMs consistently claim to detect bugs in entirely bug-free programs while the rate of repair of buggy programs is less than that of the damage to correct programs. We also explore the long-term dynamics of this iterative process, and find that this frequently reaches a pseudo-bug-fixing cycle where the same changes are added and removed again ad infinitum. Lastly, via mechanistic probing, we unveil the existence of a steering vector which controls the editing propensity, suggesting that LLMs have an internal representation of ``buggy code", and that this representation is what is falsely activated to induce pseudo-bug fixing. These results provide insight towards the dynamics of fully autonomous bug-fixing systems, as well as stopping conditions under ambiguous goals.
