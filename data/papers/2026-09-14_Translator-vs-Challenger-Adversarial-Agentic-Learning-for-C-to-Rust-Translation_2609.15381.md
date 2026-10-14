# Translator vs. Challenger: Adversarial Agentic Learning for C-to-Rust Translation

- arXiv ID: `2609.15381v1`
- Authors: Chaofan Wang, Xiaodong Gu, Yuling Shi, Chao Hu, Beijun Shen
- Published: 2026-09-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.15381v1) | [pdf](https://arxiv.org/pdf/2609.15381v1)

## Abstract

C-to-Rust translation remains challenging due to the substantial semantic gap between the two languages. Recent experience-enhanced LLM translators improve translation quality by learning reusable insights from prior failures and repairs. Yet learned insights do not automatically constitute reusable translation knowledge: derived from sparse, program-specific traces, they often contain missing conditions, narrow applicability boundaries, or overlooked corner cases. This limits their robustness and generalizability in new translation scenarios. We present TRAIL, an adversarial agentic learning framework for robust C-to-Rust translation. TRAIL employs two collaborating agents: a Translator that derives candidate insights from translation failures and accepted repairs, and a Challenger that actively searches for weaknesses, gaps, and boundary cases through adversarial challenges. To improve the robustness of individual insights and the completeness of insight collections, TRAIL performs adversarial learning at two levels. Individual-insight adversarial learning repeatedly stress-tests each insight to refine its applicability conditions and constraints, while compositional insight adversarial learning strengthens groups of related insights by exposing conflicts, gaps, and uncovered corner cases. By challenging insights and their compositions with executable counterexamples, TRAIL transforms trace-specific experience into robust, reusable, and generalizable translation knowledge. We evaluate TRAIL on two project-level benchmarks, CRUST-Bench and SmartC2Rust-Bench. Compared with the strongest LLM-based baseline, TRAIL achieves average relative improvements of 23.1% in syntax accuracy and 15.9% in semantic accuracy. Furthermore, the adversarially refined insights transfer effectively across benchmarks, demonstrating strong generalizability across diverse C-to-Rust translation tasks.
