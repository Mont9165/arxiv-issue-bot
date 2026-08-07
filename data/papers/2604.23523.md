# Grammar-Constrained Refinement of Safety Operational Rules Using Language in the Loop: What Could Go Wrong

- arXiv ID: `2604.23523v1`
- Authors: Khouloud Gaaloul, Zaid Ghazal, Madhu Latha Pulimi, Sam Emmanuel Kathiravan
- Published: 2026-04-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.23523v1) | [pdf](https://arxiv.org/pdf/2604.23523v1)

## Abstract

Safety specifications in cyber-physical systems (CPS) capture the operational conditions the system must satisfy to operate safely within its intended environment. As operating environments evolve, operational rules must be continuously refined to preserve consistency with observed system behavior during simulation-based verification and validation. Revising inconsistent rules is challenging because the changes must remain syntactically correct under a domain-specific grammar. Language-in-the-loop refinement further raises safety concerns beyond syntactic violations, as it can produce semantically unjustified refinements that overfit to the observed outcomes. We introduce a framework that combines counterfactual reasoning with a grammar-constrained refinement loop to refine operational rules, aligning them with the observed system behavior. Applied to an autonomous driving control system, our approach successfully resolved the inconsistencies in an operational rule inferred by a conventional baseline while remaining grammar compliant. An empirical large language model (LLM) study further revealed model-dependent refinement quality and safety lessons, which motivate rigorous grammar enforcement, stronger semantic validation, and broader evaluation in future work.
