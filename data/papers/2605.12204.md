# Graph-Grounded Optimization: Rao-Family Metaheuristics, Classical OR, and SLM-Driven Formulation over Knowledge Graphs

- arXiv ID: `2605.12204v2`
- Authors: Madhulatha Mandarapu, Sandeep Kunkunuru
- Published: 2026-05-12
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.NE`
- Links: [abs](http://arxiv.org/abs/2605.12204v2) | [pdf](https://arxiv.org/pdf/2605.12204v2)

## Abstract

We propose graph-grounded optimization: a paradigm in which the decision variables, constraints, and objective coefficients of a real-world optimization problem are sourced from a property knowledge graph (KG) via Cypher queries, rather than supplied as free-form natural-language text or static tabular input. We motivate the paradigm by surveying recent LLM/SLM-driven optimization systems -- OptiMUS, Chain-of-Experts, LLMOPT, OPRO, FunSearch, Eureka -- none of which consume property graphs as the primary input modality. We instantiate the paradigm in the open-source samyama-graph database and evaluate seven real-world public-domain KG-backed problems spanning drug repurposing (245K-node biomedical KG), clinical-trial site selection (7.78M-node trial registry), Indian supply-chain rerouting (5.34M-node OSM road graph), healthcare equity allocation (WHO/GAVI/IHME KG), economic-environmental grid dispatch, antimicrobial-resistance stewardship (NCBI AMRFinderPlus, 10.4K resistance genes), and wildfire evacuation routing (OSM Paradise, CA). We compare a portfolio of Rao-family metaheuristics (BMWR, Jaya, SAMP-Jaya, EHR-Jaya, Rao-1) against Google OR-tools (CP-SAT and GLOP) reference solvers. We find that (i) no single Rao variant dominates: BMWR wins on discrete-with-tradeoff and high-dim-with-hard-constraint problems while Rao-1 wins on continuous low-/mid-dim problems, empirically supporting a portfolio approach; (ii) OR-tools dominates on small linear/MILP-friendly sub-problems but cannot encode the non-linear objectives that emerge in several of the real-world settings; (iii) graph-grounded formulations surface data-quality issues (missing properties, degenerate aggregates) that purely text-formulated optimizations would silently mask
