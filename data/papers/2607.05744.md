# Unicode TAG-Block Concealment of Tool-Metadata Payloads in the Model Context Protocol: An Approval-View Fidelity Gap Across Three Independent Server Implementations

- arXiv ID: `2607.05744v1`
- Authors: Mohammadreza Rashidi
- Published: 2026-07-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05744v1) | [pdf](https://arxiv.org/pdf/2607.05744v1)

## Abstract

The Model Context Protocol (MCP) is the dominant way coding agents discover and invoke external tools. A server advertises each tool through a tools/list handshake that returns a name, a natural-language description, and a JSON input schema. The client renders this metadata once, in a one-time approval dialog, and then injects it verbatim into the model's context on every subsequent turn. Nothing in the protocol requires the rendered approval view and the bytes delivered to the model to match. We isolate that gap as a single structural mechanism, concealment encoding, and show with a model-free, protocol-free analysis that Unicode's TAG block (U+E0000 to U+E007F) has no assigned glyph in any mainstream terminal, chat, or IDE renderer, so a payload written in it is absent from what a human reviewer sees while surviving byte-for-byte into the model's tokenizer. We then measure whether this mechanism actually defeats today's client-side defenses, building a proof-of-concept that speaks the real MCP JSON-RPC/stdio protocol against a genuine client and server. Across 5 distinct MCP metadata surfaces we implement 8 concrete techniques with a deterministic, protocol-level harness. All 8/8 techniques deliver an attacker-controlled payload into the model's context, 4/8 evade a representative string-matching sanitizer, and exactly as the mechanism analysis predicts, only the TAG-block encoding (1/8) is invisible in the human approval view while still reaching the model verbatim. MCP forces re-approval for 0/8 techniques even under a time-of-check to time-of-use rug-pull. To test whether these outcomes are a property of the protocol or an artifact of one server codebase, we re-implement the catalogue against 3 independently developed Python MCP server libraries and find total agreement across all 32 cross-library outcome cells. The baseline sanitizer flags 0 of 25 benign descriptions.
