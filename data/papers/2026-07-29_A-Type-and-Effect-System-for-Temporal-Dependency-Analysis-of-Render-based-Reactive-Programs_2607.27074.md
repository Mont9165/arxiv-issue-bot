# A Type-and-Effect System for Temporal Dependency Analysis of Render-based Reactive Programs

- arXiv ID: `2607.27074v1`
- Authors: June Wunder, Ankush Das, Marco Gaboardi
- Published: 2026-07-29
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.27074v1) | [pdf](https://arxiv.org/pdf/2607.27074v1)

## Abstract

Reactive programming frameworks such as React allow developers to build interactive applications by declaratively specifying how outputs depend on changing inputs. Although this model makes it easy to reason about what an application computes, the temporal behavior of reactive programs remains difficult to understand and verify. Applications implicitly rely on timing assumptions buried in framework runtimes, leading to subtle bugs such as stale reads, transient inconsistencies, order-dependent behavior, and unintended feedback cycles. To address these challenges, this paper presents Willow, a core calculus for reactive programming inspired by React. Willow gives a time-aware operational semantics that models computation in terms of renders, the fundamental evaluation step in which components produce user interface descriptions, and pairs it with a novel type-and-effect system that statically tracks timing behavior as effects. A "next" modality expresses delays measured not only in renders but in any unit the host environment exposes--renders, network requests, or milliseconds. A family of modalities tracks the lifecycle of event handlers: when they are registered, when they fire, when pending events are canceled and when handlers are removed. A key insight is that the resulting effects form a temporal dependency graph, letting standard graph algorithms statically detect render cascades and inter-render loops that cause non-termination or performance degradation. We formalize Willow and prove preservation of the effect system with respect to the time-aware semantics. We also implement a prototype checker with automatic effect inference and evaluate it on representative reactive patterns such as debouncing, form inputs, and API-driven updates. Our results demonstrate that time-aware typing provides a practical foundation for reasoning about the temporal correctness of reactive programs.
