# Environment Steering: Using Data Flow Control to Improve Agent Utility and Safety

- arXiv ID: `2609.35807v1`
- Authors: Charlie Summers, Prajwal Raghunath, Aaditya Pai, Mayur Kulkarni, Zhuo Zhang, Oliver Kennedy, Eugene Wu
- Published: 2026-09-19
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.35807v1) | [pdf](https://arxiv.org/pdf/2609.35807v1)

## Abstract

LLM agents can make unsafe tool calls even when instructed to behave safely. Existing defenses constrain agents before execution, modify tool inputs/outputs, or rely on LLM judges; these approaches may depend on model behavior or block unsafe actions without helping the agent recover. We argue that the execution environment should instead enforce safety as the agent runs and steer it toward safe alternatives when violations occur---we call this Environment Steering. We implement this by modeling the agent and harness execution state as database tables, track the record-level data flows, and check these data flows against declarative policies during runtime. When violations are detected, policy- and context-specific feedback steers the agent toward safe trajectories. On AgentDyn, this enables the agent to improve task success rate over no-defense while achieving 0% attack success rate.
