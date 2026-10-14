# Evaluating human and LLM screening workflows in a conceptually complex scoping review: Recall--workload trade-offs and run-to-run consistency

- arXiv ID: `2608.26885v1`
- Authors: Nikol Figalová, Lynn Huestegge, Anne Böckler-Raettig
- Published: 2026-08-27
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.HC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.26885v1) | [pdf](https://arxiv.org/pdf/2608.26885v1)

## Abstract

Background. Large language models (LLMs) are increasingly used for screening in evidence synthesis, where false negatives can remove relevant studies before full-text assessment. We compared human and LLM title-and-abstract screening workflows in a preregistered study embedded in a conceptually complex scoping review.
  Methods. After a conservative title-only screen, 1,131 records were screened by one review lead, four trained assistants screening non-overlapping subsets, and seven complete LLM runs using different models and processing configurations, including a nominally identical repeat run. We compared retained workload, operational recall against 316 verified eligible records, agreement, run-to-run consistency, and procedural burden. Because eligibility was verified only for records advanced and assessed in the parent review, recall estimates were operational.
  Results. No workflow recovered all verified eligible records. The human workflows and two GPT-5.4 file-batch runs retained 42.2-45.0% of records while achieving 82.3-82.9% recall. Gemini 3.1 file batches achieved the highest recall (83.9%) but retained 56.7% of records. All-at-once configurations recovered fewer eligible records than corresponding file-batch configurations. Two nominally identical GPT-5.4 file-batch runs agreed on 91.7% of records but differed on 94 records, including 29 verified eligible records retained by only one run.
  Discussion. LLM screening performance depended on the implemented workflow, not model identity alone. Processing configuration, workload, record-level variation, and human-LLM decision integration are therefore substantive properties of deployed systems. For high-recall tasks, LLMs are better suited to validated, auditable, human-supervised workflows than autonomous exclusion.
