# Why We Created Yet Another Memory Framework: Understanding MGA's Role in Next-Gen Database Systems

- arXiv ID: `2608.22853v1`
- Authors: Vikramraj Sitpal, Pei Li, Shubham Kumar, Somansh Reddy Satish, Ravi Thammaiah, Nagarajan Muthukrishnan
- Published: 2026-08-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.22853v1) | [pdf](https://arxiv.org/pdf/2608.22853v1)

## Abstract

Despite the presence of multiple memory regions in modern database systems, supporting an efficient form of memory remains a challenge under production constraints. In enterprise-grade data systems, existing abstractions impose a trade-off between coarse-grained global sharing and strict process isolation, resulting in data copying, memory fragmentation, and limited support for controlled sharing. These challenges become more pronounced as workloads grow more diverse, and systems must tolerate process failures while maintaining predictable performance. This paper introduces the Managed Global Area (MGA), a scoped shared-memory abstraction in Oracle AI Database that addresses these limitations. MGA allows components to explicitly define allocation source, membership, and coordination semantics across selected processes while integrating with a production database engine. Unlike fully shared memory regions in Oracle, such as the System Global Area (SGA), MGA supports dynamic process membership and modular memory usage without imposing system-wide visibility. We evaluate MGA on analytical and AI workloads that stress shared-memory execution, including TPC-H hash joins and ONNX Runtime inference. Under concurrent execution, MGA reduces latency for join-intensive TPC-H queries by up to 35%. For ONNX- based inference, MGA-enabled model sharing reduces memory footprint by up to 90% and lowers large-model inference latency by up to 37%. These results demonstrate that dynamically scoped shared memory can improve both efficiency and predictability in production database systems.
