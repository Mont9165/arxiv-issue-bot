# From Migration to Calibration: Preserving Agent Capabilities across Models, Jurisdictions, and Scale

- arXiv ID: `2609.35149v1`
- Authors: Yaxiao Liu, Pengbo Liu, Yiwen Liu, Yihua Guan, Jiaxing Song
- Published: 2026-09-28
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.35149v1) | [pdf](https://arxiv.org/pdf/2609.35149v1)

## Abstract

Agents need calibration when deployment conditions change: replacing a driving model, including a foundation-to-post-trained transition; crossing jurisdictions; or scaling across heterogeneous markets and sources. Interface compatibility alone does not establish capability retention or target-contract satisfaction. We formulate agent calibration as constrained behavioral adaptation across three interacting layers: information preservation, harness adaptation, and user acceptance; the layers apply to every scenario, not one-to-one to the three. The basic objective is non-degradation on prespecified capability measures while satisfying target requirements; aggregate improvement is stronger. Information calibration preserves independently validated source content still applicable to the target task. Harness calibration aligns observable artifacts at semantic checkpoints and repairs them through iteration, tool substitution, or local replanning within explicit budgets. User calibration enforces recipient-specific output contracts: templates, schemas, and section-level preferences. A global e-commerce example shows how shared standards coexist with site- and market-specific adapters and validation. We distinguish trainable policies from frozen-backbone configuration or controller optimization, and evidence verification from relative judgment and DPO/GRPO optimization. Recent harness-transfer and judge-validity studies motivate target-native execution records, separate audits of task validity and near-tie ranking, and matched target-native optimization controls. We propose held-out evaluations for model changes, cross-border adaptation, and scale, including a factorial test of source evidence and checkpoint repair and group-level reporting to prevent aggregate gains from masking local failures. This is a methodological proposal; implementation and empirical validation remain future work.
