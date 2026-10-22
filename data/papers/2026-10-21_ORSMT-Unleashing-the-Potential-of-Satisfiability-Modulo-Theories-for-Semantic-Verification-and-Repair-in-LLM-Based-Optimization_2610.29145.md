# ORSMT: Unleashing the Potential of Satisfiability Modulo Theories for Semantic Verification and Repair in LLM-Based Optimization

- arXiv ID: `2610.29145v1`
- Authors: Rui Zhang, Chenyu Zhou, Jianghao Lin, Yaoxin Wu, Dongdong Ge, Wen Song
- Published: 2026-10-21
- Primary category: `math.OC`
- Categories: `math.OC`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.29145v1) | [pdf](https://arxiv.org/pdf/2610.29145v1)

## Abstract

Large language models increasingly automate optimization modeling from natural language problems, producing written mathematics, solver code and a returned report. Verifying one optimization problem across these artifacts requires semantic comparison: unequal models can attain the same objective, equivalent models can use different auxiliary variables, and mutually consistent artifacts can omit the same source requirement. ORSMT provides a typed semantic interface and exact SMT relation queries. It aligns observable decisions, projects auxiliary variables, proves or refutes feasible region and objective relations, localizes refutations to implicated rows or domains and links source texts when available. It then reconstructs one artifact from another, and each adopted candidate passes the required relation checks. Across 3,034 problems and six generator sizes, ORSMT improves the model-code match rate in all 72 benchmark and generator combinations before selection. Protected selection raises the aggregate rate from 43.2% to 88.2% and the share that are both correct and matched from 25.2% to 40.2%. On the 1,905 refuted outputs, certified voting under the shared fallback makes 50.9% of outputs correct and matched, compared with 44.8% for ReLoop and 49.4% for Opt-Verifier. A separate one-round source revision followed by exact reconstruction restores a model-code match for 84.4% of the refuted pairs.
