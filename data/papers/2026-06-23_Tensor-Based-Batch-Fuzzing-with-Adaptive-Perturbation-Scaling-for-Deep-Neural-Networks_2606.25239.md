# Tensor-Based Batch Fuzzing with Adaptive Perturbation Scaling for Deep Neural Networks

- arXiv ID: `2606.25239v1`
- Authors: Guanqin Zhang, Yulei Sui
- Published: 2026-06-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.25239v1) | [pdf](https://arxiv.org/pdf/2606.25239v1)

## Abstract

Deep neural networks are increasingly deployed in safety-critical domains such as autonomous driving and medical diagnosis, yet their opaque, high-dimensional parameter spaces make it difficult to systematically assess model reliability on unseen inputs. Existing coverage-guided sequential fuzzing frameworks for DNNs inherit a one-input-per-iteration design from traditional software fuzzing and apply uniform perturbation budgets across all input dimensions, limiting both testing throughput (i.e., inputs processed per unit time) and the precision of input-space exploration. We present a new specification-aware batch fuzzing framework with adaptive perturbation scaling that addresses both limitations. Rather than relying on a fixed global perturbation radius epsilon, our approach derives mutation step sizes from specification-defined feasible ranges (the gap between lower and upper bounds) using a shared scale factor. This scaling can be applied either as a global scalar (isotropic) or as per-dimension step sizes (anisotropic), keeping perturbations consistent with the underlying constraint structure. As a result, the fuzzer can explore input spaces with heterogeneous feature scales more effectively across all specifications in the batch. We embed input constraints and output property checks directly into the network as non-trainable layers, yielding a wrapped model that processes B specification instances in a single batched iteration, substantially improving fuzzing efficiency and counterexample exploration. We evaluate our framework extensively on three benchmarks, covering six networks and over 400 specifications across TrafficSigns, Cifar100, and TinyImageNet. Our tensor-based fuzzing achieves up to 40X higher throughput and 4X more violations than the sequential baseline under the same time budget, demonstrating significantly improved effectiveness in specification-guided fuzzing.
