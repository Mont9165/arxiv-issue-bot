# When Is One Query per Template Enough? Adapting Learned Cost Models to New Hardware

- arXiv ID: `2611.05892v1`
- Authors: Krish Patel
- Published: 2026-11-04
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2611.05892v1) | [pdf](https://arxiv.org/pdf/2611.05892v1)

## Abstract

A learned cost model that predicts query runtimes is trained on measurements from one machine. When the database moves to other hardware, its plans stay the same but their runtimes change, each by its own factor. We ask how to adapt such a model from k queries measured on the new machine: which queries to run, how to use their runtimes, and how many are enough. On PostgreSQL we timed the same plans of 1,162 TPC-H and TPC-DS queries in six environments: a laptop and a server, each with all its processors or pinned to one, the server also pinned to two, and the laptop also with a small buffer pool. No single factor describes the slowdown between two environments: most of its variance lies between query templates, so a speed factor stops improving after a few queries. A correction that fits separate lines for serial and parallel plans and adds an offset for every measured template brings the moved model, with one measured query per template, to an error (geometric mean over templates of the median Q-error) of 1.10 on TPC-H and 1.19 on TPC-DS, close to the same correction on a model trained on the new machine; fine-tuning a DACE-style neural cost model on the same queries gains at most 2%. On templates never measured, no correction we tried is on average more than 2% better than the speed factor. We then fixed hypotheses and timed new data. On TPC-H at ten times the scale the errors follow these results, but two of five repeated tests miss. On the Join Order Benchmark, whose queries differ widely within a template, the model errs by 2.36 even when retrained on the new machine, no correction gains much, and only the test on new templates holds; boosted trees and a neural model fit these queries better, and correcting the neural model works as well as fine-tuning it. We report every test as registered.
