# When the Next Step Is Not One Step: Distribution-Aware Execution Modeling for Concurrent Go Programs

- arXiv ID: `2606.17508v1`
- Authors: Kaviru Hapuarachchi
- Published: 2026-06-16
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DC`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.17508v1) | [pdf](https://arxiv.org/pdf/2606.17508v1)

## Abstract

Training a model to predict the next step in a concurrent program is harder than it looks: two runs of the same program from the same trace prefix can produce different next events, both valid, because the scheduler is nondeterministic. A model trained against a single label is learning to guess one outcome of a random process. We turn this around and use the nondeterminism as a training signal. We run each program many times, aggregate the observed next events into an empirical distribution, and fine-tune a 7B model to match that distribution with a KL objective. On 798 held-out predictions drawn from real production Go bugs (CockroachDB, Kubernetes, gRPC, etcd), fine-tuning on fewer than a thousand traces reaches 36.2% accuracy, ahead of Gemini 3.5 Flash used zero-shot (34.8%) and the same model without fine-tuning (28.6%). Distribution training matches cross-entropy on accuracy (35.8% vs. 36.2%) while reducing Expected Calibration Error from 0.205 to 0.169. We also derive a formal goroutine-leak signature for a class of select-blocked goroutines where P(GoUnblock)=0 holds by scheduler semantics, not by learning. We release the dataset, trained adapters, and all tooling.
