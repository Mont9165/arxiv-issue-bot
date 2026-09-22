# io_uring in Oracle Database: A Hybrid Storage I/O Architecture at Production Scale

- arXiv ID: `2609.22781v1`
- Authors: Rajarshi Chowdhury, Akshay Shah, Margaret Susairaj, Ayush Agrawal
- Published: 2026-09-19
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2609.22781v1) | [pdf](https://arxiv.org/pdf/2609.22781v1)

## Abstract

We describe the integration of io_uring into Oracle Database's storage layer and the architectural decisions required to deploy it in a production multi-process RDBMS. Our design uses per-process ring contexts that eliminate inter-process synchronization, a shared buffer registration mechanism now part of the mainline Linux kernel, and a transparent fallback to libaio on error. Evaluation on an internal development build of Oracle Database 26ai shows that io_uring's benefits concentrate on asynchronous batched I/O paths: on a mixed OLTP workload (TPC-C), io_uring delivers identical throughput while reducing server CPU utilization by 1.2 percentage points through more efficient background writes; on analytical queries (TPC-H), CPU per query drops by 8.5% (geometric mean). Isolating the write path alone shows 29% lower CPU per write and 34% higher throughput. Synchronous read paths -- the dominant I/O in OLTP -- show no improvement and even increased CPU usage for very large I/O sizes. These results motivate a hybrid I/O architecture that retains pread/pwrite for synchronous operations, adopts io_uring for asynchronous batched I/O, and falls back transparently to libaio -- a selective strategy that may also be relevant to other database systems facing the same integration question.
