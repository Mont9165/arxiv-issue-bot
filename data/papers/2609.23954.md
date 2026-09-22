# Djinnlang: Higher-Level Programming by Unambiguous Specification with an LLM in the Compiler

- arXiv ID: `2609.23954v1`
- Authors: Simon Henniger, Stephen Chong, Nada Amin
- Published: 2026-09-21
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.23954v1) | [pdf](https://arxiv.org/pdf/2609.23954v1)

## Abstract

Programmers write formal specifications, and LLMs implement them, proving that each implementation matches its spec. Taken to its extreme, this makes specification languages the new programming languages. We argue that an unambiguity constraint is key: in addition to proving that its implementation satisfies the specification, the LLM must also prove that any other implementation satisfying it must produce the same outputs on the same inputs, i.e. that the relation formed by the constraints is deterministic. This leaves the LLM no leeway on program semantics: as with a conventional compiler, the generated code never needs to be read and can be regenerated from the spec at any time. Under this constraint and with a powerful LLM, the difference between a specification language and a programming language becomes essentially meaningless, and the LLM essentially becomes a part of the compiler toolchain. The arrangement doubles as a strong form of AI control: an untrusted model writes the code, yet its work is tightly checked by a verifier.
  To demonstrate that our LLM-in-the-compiler paradigm is feasible when supported by our unambiguity constraint, we present Djinnlang, a high-level specification language built for this future. A Djinnlang program consists only of specifications --- the programmer never writes executable code. In place of a traditional compiler, a symbolic translator lowers each spec to Dafny stubs and proof obligations, and a driver harness orchestrates an LLM that fills in implementations and proofs, all checked by the Dafny verifier. We evaluate our language and implementation on multiple examples and we show that it is self-hosting: an LLM can implement the Djinnlang translator from its specification and the reimplementation can verify itself.
