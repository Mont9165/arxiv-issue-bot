# Formal-Method-Guided Vibe Coding: Closing the Verification Loop on AI-Generated Safety-Critical Software Through Model-Driven Engineering

- arXiv ID: `2606.22413v1`
- Authors: Ran Wei, Le Zhu, Haochi Wang, Jim Woodcock, Fang Yan, Simon Foster, Xiangyang Ji
- Published: 2026-06-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.FL`
- Links: [abs](http://arxiv.org/abs/2606.22413v1) | [pdf](https://arxiv.org/pdf/2606.22413v1)

## Abstract

Vibe coding -- accepting LLM-generated source from natural-language intent with minimal review -- is fast and may be adequate for low-criticality consumer software. But for safety-critical systems governed by DO-178C, IEC 61508, or ISO 26262, it offers no path to certification: large language models (LLMs) provide no formal correctness guarantees, and existing remedies target verification-aware languages (Dafny, Verus, Lean) that are scarce in pretraining data and absent from industrial toolchains.
  This paper closes the gap. We present Forge (Formal method Oriented Refinement loop for GEnerated code): a closed-loop pipeline that guides vibe coding through formal verification using established Model-Driven Engineering (MDE) infrastructure. Through vibe coding, we generate Java source code; our pipeline then extracts -- via model transformations -- formal artefacts in three different formalisms, each checked by a complementary verifier: deductive verification (Dafny), Communicating Sequential Processes (CSP) refinement via the Failures-Divergences Refinement checker (FDR4), and theorem proving using Z-Machines in Isabelle; every verification failure becomes a structured correction prompt that drives the next code-generation iteration. The LLM is the draft generator, the MDE chain is the discriminator, and the developer never has to read the formal models.
  Empirically, we find that the pipeline produces standards-relevant verification evidence for LLM-generated Java -- a step toward certification.
