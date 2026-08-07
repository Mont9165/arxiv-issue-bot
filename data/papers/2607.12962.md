# Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models

- arXiv ID: `2607.12962v1`
- Authors: Mehmet Iscan
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.12962v1) | [pdf](https://arxiv.org/pdf/2607.12962v1)

## Abstract

Frozen small code LLMs are deployed locally, yet the information guiding a retry after a failed attempt is still measured without placebo controls in the self-repair literature. We treat a failed program as a conjecture and an execution counterexample as an oracle-relative refutation, and introduce PoPE (Popperian Placebo-controlled Evaluation): a methodology for measuring whether evidence that falsifies LLM-generated code can be used operationally by that same model. In PoPE, error content is paired with channel-specific placebos that keep the predeclared scaffold while ablating task-relevant content or deranging the task-error assignment. Frozen small code models (0.5-1.5B) are evaluated under preregistered rules through a prompt channel and a weight channel (small-data adapter training), with four generations per arm-unit pair. In the prompt channel, public-tier screening unlocked 12 units under the content-ablated form placebo versus 10 under the live error-pattern arm on a 40-unit resistant band; the result was recorded as mechanism-null. In the weight channel, an 8-8 tie was observed between the error-content adapter and the intervention-free baseline (p=1.0), while the SHA-deranged placebo adapter stayed ahead with 10 unlocks; content-attributable superiority was not confirmed. These results do not constitute evidence of equivalence or non-inferiority. Equivalence was not tested separately. Findings are restricted to the public-tier screening endpoint; hidden-tier confirmation was deferred by design. We read this not as compiled criticism disappearing as information, but as the loss of its external role in testing a new conjecture: when a representation learned from the oracle is written back into the generation state, testing is replaced by conditioning. No working JEPA-RL controller is claimed. PoPE is presented as a placebo-controlled, retestable measurement standard.
