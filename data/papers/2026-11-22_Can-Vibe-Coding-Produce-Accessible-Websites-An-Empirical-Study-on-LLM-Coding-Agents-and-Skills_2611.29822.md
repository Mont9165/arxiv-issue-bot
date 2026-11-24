# Can Vibe Coding Produce Accessible Websites: An Empirical Study on LLM Coding Agents and Skills

- arXiv ID: `2611.29822v1`
- Authors: Syed Fatiul Huq, Md. Asif Haider, Abu Jafar Saifullah, Thomas Zimmermann, Sam Malek
- Published: 2026-11-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.29822v1) | [pdf](https://arxiv.org/pdf/2611.29822v1)

## Abstract

Large language model (LLM) coding agents increasingly allow developers and non-professionals to create websites through natural-language instructions, with limited inspection of the generated source code. Although this ``vibe coding'' workflow lowers barriers to software creation, it may also propagate accessibility defects at scale. We investigate the accessibility of websites generated end-to-end by contemporary coding agents and whether agent-level accessibility interventions improve their output. We generated 90 websites for three projects using combinations of three coding agents, four language models, and multiple reasoning-effort levels. We evaluated complete interaction journeys using axe-core, IBM Equal Access Accessibility Checker, and QualWeb, and converged reports to observe violation prevalence and violated WCAG Success Criterion (SC). None of the 90 baseline websites was fully accessible, with an average of 80.43 violated interface elements. 13 WCAG SCs were violated at least once across the runs. Color contrast was the most prevalent issue, followed by labeling, semantic-structure, keyboard, and visualization failures. We reran 24 matched configurations with a general accessibility Skill and a contrast-specific Skill. Both significantly improved accessibility scores, but neither eliminated violations. User testing with blind individuals corroborated the experiential effects of the detected inaccessibilities. Moreover, functional correctness decreased with the inclusion of Skills. Our findings show that accessibility does not reliably emerge from vibe coding, and agentic interventions can both improve some accessibility issues and introduce new functional ones.
