# Trust the Spec, Not the Code - A Specification-First, AI-Assisted Case Study in Online Banking

- arXiv ID: `2609.07365v1`
- Authors: Eitan Farchi
- Published: 2026-09-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.07365v1) | [pdf](https://arxiv.org/pdf/2609.07365v1)

## Abstract

Formal specification promises early error detection, explicit invariants, and correctness by design, yet its notational cost has kept it out of mainstream practice. We argue that AI removes much of that cost: natural language enriched with lightweight mathematics, written in \LaTeX, can serve as an intermediate specification language that is precise enough to reason over and prove, while a large language model (LLM) reviews it for ambiguity, drafts proofs, and generates the implementation. The specification becomes the artifact one authors, reviews, proves, and refines; the code becomes regenerable output. This paper is a follow-on to a prior study that established the discipline on an organizational-knowledge-growth simulation~\cite{predecessor2026}. Here we replicate the discipline in a different domain---an online-banking fund-transfer service---and extend it. The two domains share one spine: a conservation invariant (knowledge in the prior study, money here), which suggests the approach generalizes across domains. We contribute: (i) a second, independent case study of the method; (ii) a stress-test of the method on a richer problem---\emph{scheduled/recurring} transfers---whose generated code grows substantially while the invariant and its proof do not; (iii) an \emph{AI-proposed runtime coverage model} for invariants (``never violated $\neq$ covered''); and (iv) a Z formalization, including paired success/failure operation schemas and an invariant proved over the inductive set of all reachable configurations, together with an experiment in which the AI proposes the Z interfaces itself. We are explicit about the method's limits: the proofs and runtime checks live at the specification level and do not establish that the generated code refines the specification---that step is delegated to the AI. This is a case study, not a controlled experiment.
