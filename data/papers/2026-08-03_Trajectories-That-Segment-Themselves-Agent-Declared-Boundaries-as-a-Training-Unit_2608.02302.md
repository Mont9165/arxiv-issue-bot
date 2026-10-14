# Trajectories That Segment Themselves: Agent-Declared Boundaries as a Training Unit

- arXiv ID: `2608.02302v1`
- Authors: Jingxi Wei
- Published: 2026-08-03
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.02302v1) | [pdf](https://arxiv.org/pdf/2608.02302v1)

## Abstract

Long-horizon coding-agent trajectories are poorly matched to the credit units available to train on: a single action has no stable value, an episode label merges productive exploration with abandoned directions, and a fixed window cuts where the logging mechanics fall. We introduce collection-time semantic self-segmentation, in which a declarative contract has the acting agent expose its own boundaries while the trajectory is generated. Instantiated with falsifiable causal hypotheses, successive adoptions expose variable-length semantic phases, and no milestone vocabulary, gold patch, environment replay, teacher logits, or retrospective segmenter places a boundary. Because the agent names its conjecture, a reviewer can negate it by name, which lets our protocol manufacture wrong-cause-then-correction transitions that recorded work rarely contains; one collection then yields four supervised targets, including audit supervision from exactly the failed regions an episode label discards. We then ask what survives deleting the declaration. Given the cut points but not the hypothesis, a model attributes action blocks to their governing hypothesis at over twice chance, beating equal-length blocks over the same trajectories (paired sign test $p = 0.0002$), surviving a lexical control and collapsing under label permutation. Asked instead to place boundaries, a code-blind annotator matches 24 of 40 where random placement matches 11.5, while a mechanical test-event rule beats chance at neither end of a strict-to-permissive sweep. The segments are therefore coherent and not cheaply reproducible. Downstream, DPO on 2,551 phase-boundary pairs changes no decision on 91 adversarial held-out items, while four of 60 change on matched-construction items, all wrong to right, where two controls change none: with 1,825 pairs from one generator, the variable to vary next is corpus diversity, not the boundary.
