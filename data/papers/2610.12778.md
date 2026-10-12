# Leakage-Resistant Evaluation of AI-Generated Database Specifications in Specification-Driven Migration

- arXiv ID: `2610.12778v1`
- Authors: Oleg Grynets, Ivan Fedorchuk, Vasyl Lyashkevych
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DB`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2610.12778v1) | [pdf](https://arxiv.org/pdf/2610.12778v1)

## Abstract

This paper presents a leakage-resistant framework and benchmark (LRFB) for measuring evaluators of AI-generated Oracle PL/SQL specifications. The benchmark contains 494 labelled source-specification pairs across 19 quality metrics grouped into seven dimensions; each metric contains 26 records divided into development and held-out subsets of 13 records each, with three clean and ten defective specifications per subset. Ground truth is mechanically sealed from inference and checked with canary and label-permutation tests. Three LLM judges were evaluated with three runs per record and compared against two trivial baselines. On 247 held-out records, GPT-4o, DeepSeek V4 Pro, and Claude Sonnet 4.5 reached balanced accuracies of 0.87, 0.89, and 0.81, respectively, while a specification-length baseline reached 0.88. Exact paired tests did not separate any judge from that baseline. The judges nevertheless provided information unavailable to length: the labelled defect category appeared among findings in 84%-92% of violated records, and quoted evidence overlapped the labelled span in 92%-93%. The study therefore reframes specification evaluation from binary issue detection toward evidence-linked, typed findings and benchmark-validity controls.
