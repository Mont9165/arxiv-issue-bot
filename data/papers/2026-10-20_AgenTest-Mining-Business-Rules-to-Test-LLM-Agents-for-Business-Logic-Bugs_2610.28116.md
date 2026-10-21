# AgenTest: Mining Business Rules to Test LLM Agents for Business Logic Bugs

- arXiv ID: `2610.28116v1`
- Authors: Lili Quan, Longtian Wang, Yuelin Wang, Mingfei Cheng, Chao Shen, Sen Chen, Xiaofei Xie
- Published: 2026-10-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.28116v1) | [pdf](https://arxiv.org/pdf/2610.28116v1)

## Abstract

Large language model (LLM) agents increasingly execute business operations through tools and interact directly with application data and services. Beyond completing user requests, these agents must obey domain-specific business rules that constrain when actions are permitted and what data or resources may be affected. Violating such rules can lead to business logic bugs, even when a task appears successful. Detecting these bugs is difficult because the rules are rarely available as explicit, testable specifications. They are distributed across system prompts and tool definitions, while others remain implicit in domain knowledge. Existing agent testing approaches typically evaluate task success, predefined policies, or known attack scenarios. This limits their ability to systematically uncover previously unspecified business-rule violations.
  We present AgenTest, which mines business rules from system prompts, tool definitions, and domain knowledge, refines them into Given-When-Then specifications, and systematically tests each specification. For each extracted specification, AgenTest instantiates its Given conditions by constructing a satisfying environment state and simulated user, exercises the agent through multi-turn interactions, and checks its Then conditions over messages, tool calls, and state changes using a hybrid oracle. On the airline, retail, and telecom agents of tau2-bench with two underlying models, AgenTest produces 551 refined specifications, and detects violations of 89 and 121 distinct specifications, respectively -- 3.4X and 2.5X as many as all baselines combined. Only AgenTest detects cases where an agent improperly accesses or modifies another user's data. Moreover, about 60% of bug-triggering runs cannot be detected from the final state alone, highlighting the need to check the full interaction against explicit business rules.
