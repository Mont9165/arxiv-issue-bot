# Testing Agentic Workflows with Structural Coverage Criteria

- arXiv ID: `2605.26521v1`
- Authors: Nafiseh Kahani, Mojtaba Bagherzadeh
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.26521v1) | [pdf](https://arxiv.org/pdf/2605.26521v1)

## Abstract

Multi-agent systems increasingly expose explicit workflow structure: agents, tools, tool-access rules, restrictions, and delegation paths. Existing evaluations rely largely on end-to-end task success, benchmark scores, final-response quality, or prompt-level checks, which provide limited evidence that this declared coordination structure has actually been exercised. This makes it difficult to assess test-suite adequacy or detect structural regressions in tool access, restrictions, and inter-agent delegation. We address this gap with a structural testing approach for multi-agent workflow specifications. The approach represents each workflow as a typed coordination graph, derives coverage obligations over reachable agents, allowed tool edges, restricted tool edges, and delegation edges, and uses coverage-driven generation with DSPy-based scenario realization to produce executable tests. The graph fixes what must be covered; DSPy realizes those obligations as natural-language scenarios whose witnesses are checked at runtime. We implement the approach for OpenAI Agents SDK-style workflows and evaluate it on ten SDK-derived benchmarks comprising 49 reachable agents, 47 tools, and 403 structural obligations. Generated scenarios witness 54/75 allowed-tool obligations and 36/48 delegation obligations within a bounded refinement budget. The adversarial restricted-tool criterion elicits 23/248 restricted-call violations, separating workflows whose restrictions hold under probing from workflows with concrete misrouting failures. These results show that structural coverage provides a useful adequacy layer for multi-agent workflow testing: it does not replace semantic or end-to-end evaluation, but reveals whether declared agents, tool-access rules, restrictions, and delegation paths have been exercised.
