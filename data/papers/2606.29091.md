# Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models

- arXiv ID: `2606.29091v1`
- Authors: Tassilo Klein, Johannes Hoffart
- Published: 2026-06-27
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.29091v1) | [pdf](https://arxiv.org/pdf/2606.29091v1)

## Abstract

Tabular foundation models cannot reason about data produced by running systems without access to the rules that govern them. We make this statement falsifiable. The \emph{Operational Turing Test} (OTT) constructs pairs of legal and rule-violating database states whose $1$- and $2$-way column-value marginals match to a total variation of $<0.02$; Le~Cam's lemma then bounds any values-only classifier at $\geq0.49$ Bayes error. Three values-only baselines (XGBoost, TabICL, TabPFN) hit the bound exactly (accuracy $0.50$, pre-registered two one-sided tests (TOST) $p<0.002$), raw row-level access does not help, exposing relational value consistency closes most of the gap, and only a classifier fed by seven executable rule-derived audits reaches $1.00$ classification accuracy. In three matched $100$-state frontier large-language-model (LLM) runs, models given the schema, trigger source, rule tables, and state files classify at most $2/50$ legal states as LEGAL; GPT-5.5 accepts $0/50$ legal states even with higher reasoning effort and a Structured Query Language (SQL) executor. The access-ladder pattern also appears on a second schema with structurally distinct rule families (banking ledger: cross-row balance, cumulative aggregate). The barrier is identifiability, not capacity: scale, data, and richer features cannot cross it without operational grounding.
