# Record Sufficiency: What a Decision Record Must Preserve When an Unsettled Claim Becomes an Operative Status

- arXiv ID: `2611.23422v1`
- Authors: Amadeus Brandes
- Published: 2026-11-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CY`
- Links: [abs](http://arxiv.org/abs/2611.23422v1) | [pdf](https://arxiv.org/pdf/2611.23422v1)

## Abstract

Organisations keep evidence, logs and approvals, but often not the step by which an unsettled claim became an operative status, such as an accepted label or a released image, so later readers cannot tell what the status was allowed to mean. We call a decision record sufficient if it is true and a reader who has only the record and the items it cites can explain the status, bound it, re-derive it and challenge it. From these four uses we argue for ten questions a record must answer, map them onto the author's earlier JSON Schema for decision records (DRK v0.1), and define four mechanical checks. We separate conformance, which the checks decide; adequacy, whether the answers are specific enough to use, which needs a reader; fidelity, which no check on the record decides; and merits, which sufficiency does not require. On 164 single-defect variants of three synthetic records, schema validation, the only check DRK v0.1 implements, rejects every variant with a deleted required property and none of the others, and it accepts a record whose claim, rule, scope, limits and challenge route are empty. These are properties of the schema shown on defects we seeded, not estimates of performance on real records. A false record passes every check. The statement-of-reasons schema of the EU Digital Services Act Transparency Database answers 4 of the questions in full, 2 in part and 4 not at all: why the matter was unsettled, what the status depends on, whether it can be re-derived, and how to challenge it. In 25 real statements from 25 platforms, drawn by a seeded rule and coded by a language model and checked by the author, free text addressed any of those four in only 2, and in 18 (24 under a stricter reading adopted during coding) no free text said why the item fell under the rule. No deployment or legal claim is made.
