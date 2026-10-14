# Agents All the Way Down; A Methodology for Building Custom AI Agents from Substrate to Production

- arXiv ID: `2606.11869v1`
- Authors: Marc Alier Forment, Juanan Pereira, Francisco José García-Peñalvo, María José Casañ Guerrero
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.11869v1) | [pdf](https://arxiv.org/pdf/2606.11869v1)

## Abstract

Custom AI agents areagents that live inside their own
  application, talk to their own data and tools, enforce their own security boundaries,
  and carry their own brand and audit trail. What separates them from the general-purpose
  tier is fit, not capability: each is built for one job, by the
  engineer who will maintain it. No published practice sets out how to build one end to
  end. The pieces are everywhere (function-calling APIs, the Model Context Protocol, code
  agents to pair with), but the practice that chains them lives in podcasts, blogs, and
  leaked system prompts. This paper writes that practice down as a methodology, Agents All
  the Way Down: two preconditions crossed once and kept, then three practices repeated
  for the agent's life. The preconditions are (P1) Substrate, the LLM as a software
  component, framed as tools, then system, then messages under prompt-caching; and (P2)
  Building blocks: function calling, MCP, CLI orchestration, the liteshell pattern, the
  agent loop, skills, characters, hooks, and scaffolding. The practices are (P3) prototype
  with a general-purpose agent; (P4) harvest, fold, and ship the result as a CLI, the
  Turtle pattern; and (P5) agent-tests-agent, in which a general-purpose agent drives it
  through behavioural scenarios, a complement to classical testing, not a replacement. The
  working loop is P3 to P4 to P5 and back, and one corollary falls out for free:
  multi-agent orchestration is just CLI composition. The methodology is framework-free by
  construction. It was distilled from the AAC, a custom agent for the open-source LAMB
  platform, built in about ten days by one developer with an AI pair-programmer and in
  production . We present it as a transferable practice, independent of any language or framework.
