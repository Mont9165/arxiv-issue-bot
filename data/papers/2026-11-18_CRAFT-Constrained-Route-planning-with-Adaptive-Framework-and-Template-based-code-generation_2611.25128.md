# CRAFT: Constrained Route planning with Adaptive Framework and Template-based code generation

- arXiv ID: `2611.25128v1`
- Authors: Shahd Elmahallawy, Ahmed Eldawy
- Published: 2026-11-18
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.25128v1) | [pdf](https://arxiv.org/pdf/2611.25128v1)

## Abstract

Everyday routing requests are rarely a point-to-point shortest path. A driver may need to visit stops, sometimes in a fixed order, under time budgets or distance limits, and perhaps recharge their EV car along the way. Each combination is a distinct routing problem that classically requires its own algorithm, so no fixed solver covers the space of queries users may ask. This paper presents CRAFT, which takes a constrained routing query as free text and returns a route that satisfies the user's requirements on a real road network. An LLM parses the query and generates four search functions, which a generic graph-search engine executes on the road network. We formalize the underlying problem as State-Expanded RCSP (SE-RCSP), which extends resource-constrained shortest paths (RCSP) with non-additive state such as node-dependent resets and discrete progress tracking. We evaluate CRAFT on 2,600 natural-language queries over California road networks against two baselines, analyzing correctness, constraint violations, long-distance scalability, and semantic POI filtering.
