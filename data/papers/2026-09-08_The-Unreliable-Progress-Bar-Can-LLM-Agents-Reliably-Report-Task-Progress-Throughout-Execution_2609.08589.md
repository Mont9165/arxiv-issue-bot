# The Unreliable Progress Bar: Can LLM Agents Reliably Report Task Progress Throughout Execution?

- arXiv ID: `2609.08589v1`
- Authors: Boyang Wang, Yunhan Wang, Yalun Wu
- Published: 2026-09-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2609.08589v1) | [pdf](https://arxiv.org/pdf/2609.08589v1)

## Abstract

Recent large language models can emit task-progress signals that agent frameworks use to decide whether a task should continue or stop, yet whether a model can reliably report its task progress at every stage of a task, and where and how its reports fail, has not been studied systematically. We evaluate this ability on the public benchmark $τ^2$-bench and on StageIF, a controlled testbed in which reporting checkpoints are placed across the task's lifecycle. Both settings require reports at multiple task stages. We find that reporting reliability depends on the stage a task has reached, and that almost every deployed model we test is reliable at some stages and unreliable at others. Where reporting breaks down is not the same everywhere. Most deployed models lose accuracy once work is under way and recover once the task is done. The newest generation closes that mid-task drop and instead grows conservative at the finish line. Our study exposes a capability gap in task-progress reporting and provides an evaluation protocol that spans the whole course of task execution for this ability on which agent operation depends. The findings indicate that agent frameworks should not control task flow on the strength of the model's state reports alone.
