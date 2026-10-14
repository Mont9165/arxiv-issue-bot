# Traffic Scenario Orchestration from Language via Constraint Satisfaction

- arXiv ID: `2605.06966v1`
- Authors: Frieda Rong, Chris Zhang, Kelvin Wong, Raquel Urtasun
- Published: 2026-05-07
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.06966v1) | [pdf](https://arxiv.org/pdf/2605.06966v1)

## Abstract

Autonomous vehicles (AVs) require extensive testing in simulation, but test case generation for driving scenarios is laborious. The desired scenarios are often out-of-distribution and have precise requirements on interactions with the AV policy under test. Manually programming scenarios allows for precise controllability but is difficult to scale. On the other hand, statistical models can leverage compute and data, but struggle with precise controllability when out-of-distribution. We cast scenario orchestration as a constraint-solving problem and present a language-in, simulation-out scenario orchestrator for closed-loop testing AVs. Our approach leverages foundation model reasoning to translate general, natural language descriptions into a set of constraints as a scenario representation. This then allows us to leverage off the shelf solvers to solve for actor behaviors which meet precise testing intentions in closed-loop. Under a benchmark of carefully crafted and diverse scenario descriptions, our approach greatly outperforms our baselines in orchestration success rate. We further show that our closed-loop approach is especially important for scenarios which require ego-reactive specifications.
