# A four-level executable validation protocol for evaluating LLM-generated topology specifications of physics-based HVAC digital twins

- arXiv ID: `2611.25471v1`
- Authors: Younghwan Joo, Jeonghoon Han, Sanghyun Oh, Soosik Bang, Sung-il Kim
- Published: 2026-11-19
- Primary category: `eess.SY`
- Categories: `eess.SY`, `cs.AI`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.25471v1) | [pdf](https://arxiv.org/pdf/2611.25471v1)

## Abstract

Physics-based digital twins of air conditioning, a principal energy consumer in manufacturing and buildings, can be generated automatically from a declarative specification of its equipment, connections, and sizing. Large language models (LLMs) now write such specifications from plain-language descriptions. Evaluations of these specifications stop at parse success, completed runs, or textual similarity, and cannot reject a model that converges in simulation but is physically wrong. In this study, a four-level protocol is proposed that tests whether an LLM-written specification not only executes but also yields a physically valid digital twin. Each specification is executed through static validity, model build, simulation convergence, and behavioral equivalence with a hidden reference model within bands calibrated by $\pm$20% sizing perturbations. The protocol was applied to eight LLMs and fourteen HVAC topologies, five describing an existing low-humidity test chamber. To test for authorship bias, engineers and a second model family also described six topologies. Within three repairs, seven of eight models built in 98.6 to 100% of trials, with simulations converging in at least 80.0%, but reached behavioral equivalence in only 50.0 to 98.6%. About half of the failed trials converged, but not to the reference steady state, mostly in desiccant rotor systems. Pooled pass rates varied by under five percentage points across description authors. These results imply that the physics hardest to model in each field, here the desiccant rotor, must enter the generation framework as validation levels. The protocol can be adapted to other fields that generate executable digital twins from declarative specifications.
