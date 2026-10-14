# Can MCP Clients Decide What to Do After Failure? A Result-Only Actionability Audit

- arXiv ID: `2609.00072v1`
- Authors: Rishabh Mehan
- Published: 2026-08-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.00072v1) | [pdf](https://arxiv.org/pdf/2609.00072v1)

## Abstract

A client that receives isError:true knows that something went wrong. It may still have no machine-readable basis for deciding whether to fix an argument, authenticate, wait, choose another tool, or stop. This paper studies what deterministic software can learn from a completed MCP failure result alone; request arguments, schemas, discovery history, authen- tication state, transport metadata, host policy, and ap- plication state are outside that boundary. We introduce a six-part actionability profile and apply it with record- level evidence. In a small illustrative study of 21 safely induced failures from ten reachable sampled servers, typed fields expose failure in 18 cases and a broad policy in 8, yet expose no specific cause, target, executable repair, or replay constraint. Prose often carries more cause and target information, at the price of making semantic interpretation part of the recovery path. A lexical source audit finds the same text-centered pat- tern. Finally, a fail-closed prototype demonstrates how a separate experimental control plane could support deterministic branching. The result is deliberately nar- rower than an ecosystem survey or an agent benchmark: completed MCP results often make failure observable, sometimes make a broad response possible, and rarely make concrete recovery or safe replay self-contained in this sample.
