# GenOS: Compositional Certificates for Semantic Robustness in AI Code Generation

- arXiv ID: `2608.03588v1`
- Authors: Corrado Priami
- Published: 2026-08-04
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03588v1) | [pdf](https://arxiv.org/pdf/2608.03588v1)

## Abstract

AI coding agents are stochastic workflows: prompts are interpreted, artifacts are sampled, validators produce observations, and orchestrators commit or repair. Small prompt or specification changes can therefore alter program-behavior distributions even when the texts appear synonymous. Existing systems evaluate correctness, but lack a compositional criterion for safely replacing a prompt, contract, generator, or program inside a complete agentic workflow. We introduce GenOS, a probabilistic operational semantics for this replacement problem. Each layer is modeled as a Markov kernel, and each interface carries an observer-relative equivalence. We prove that equivalence-compatible kernels descend to quotient classes and that quotienting commutes with distributional extension and sequential composition. Hence, equivalent prompts induce equal probabilities for all downstream equivalence-closed events, including verified commit. We also establish workflow bisimulation, guarded-commit safety under sound validation, total-variation non-expansiveness, and an additive robustness bound that attributes approximation error to individual pipeline layers. An executable insertion-sort audit instantiates the theory with natural-language paraphrases, a formal contract, six programs, two observers, and exhaustive execution on 121 inputs. Equivalent prompts yield identical code-class and commit distributions; a prompt assigning 5% probability to an in-place contract is distinguished by a mutation observer, while downstream distances remain within the predicted bound. Across 20,000 randomized finite-kernel trials, no exact or approximate law is violated. GenOS is model-parametric: compatibility is a measurable property to test, not an assumption about language-model behavior.
