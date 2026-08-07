# Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs

- arXiv ID: `2607.12650v1`
- Authors: Junyu Ren
- Published: 2026-07-14
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CY`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12650v1) | [pdf](https://arxiv.org/pdf/2607.12650v1)

## Abstract

Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions need not hold up under formal scrutiny. We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts. Every verified output structurally descends from an attested tool call (Thm. 3.1) and a kernel-checked chain of valid inference (Thm. 3.2); residual outputs are honest Abstain with a replayable audit trail. On a subcollection of TableBench numerical reasoning (n=120), EG-VAR attains 120/120 versus a 95% same-tool baseline; on counterfactual stress tests (5 domains x 2 models), EG-VAR stays 100% source-faithful while same-tool drops to 80-90% (no-tool 50-80%). With the LLM as deployment-time formalizer, residual semantic-formalization error is 3.3% on Sonnet and 1.7% on Opus. We position EG-VAR as a technical-governance interface for high-stakes empirical claims: a formal sidecar makes the target proposition, source scope, evidence boundary, proof obligation, and abstention condition auditable, eliminating unsupported Verified outputs today while turning formalization errors, lift and source-authority disputes, ambiguities, and abstentions into explicit audit targets. Over time, typed sidecars in datasets, APIs, public records, and AI-generated documents can amortize this formalization burden into reusable infrastructure.
