# Validation Evidence in LLM Repair Agents: How Much of What Passes Actually Tests the Bug?

- arXiv ID: `2607.28871v1`
- Authors: Xiaonan Xu, Wenjing Wu
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.28871v1) | [pdf](https://arxiv.org/pdf/2607.28871v1)

## Abstract

When a repair agent runs a test and sees it pass, the result is treated as evidence about the reported defect. We measure how often that treatment is warranted. BSG-VA (buggy-state/candidate-state/gold-fix validation analysis) captures each validation command at its exact working-tree state, extracts a test-only patch, and replays the command on the original buggy code (B), the candidate state (S), and the developer gold fix (G). The captured outcome and the replay results assign every event an evidence role, from gold-aligned bug-discriminating through regression-only to misleading. Across 3,730 events in 643 rollouts on 110 tasks, 46.0% of positive comparable events carry no bug-discriminating information; 23.8% of baseline rollouts, with no feedback injected, close with a patch whose entire positive evidence base is of this kind. A three-arm experiment tests whether returning the B-replay outcome to the agent changes this pattern. Bug-contrast feedback reduces evidence-inadequate closure by 7.8 percentage points relative to an attention-matched reminder (p = 0.0029) and raises bug-discriminating evidence by 7.4 points (p = 0.011), with no detectable cost to repair success. Both estimates fall below the prespecified 10-percentage-point smallest effect size of interest, so practical magnitude remains uncertain. Roughly a third of the improvement traces to the reminder alone; across two exploratory replications, varying the scaffold and the model, the B-replay content adds a detectable increment only with gpt-5.6-sol under the unconstrained tool-use loop. BSG-VA applies post hoc to any replayable repair trajectory that preserves the required code states and execution environment.
  Keywords: program repair agents, validation evidence, test adequacy, large language models, software quality, controlled experiment.
