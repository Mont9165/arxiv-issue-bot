# The Bi-Channel Networking Paradigm for Database Systems in the Cloud

- arXiv ID: `2606.19969v1`
- Authors: Georg Kreuzmayr, Muhammad El-Hindi, Benjamin Wagner, Tobias Ziegler, Viktor Leis
- Published: 2026-06-18
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2606.19969v1) | [pdf](https://arxiv.org/pdf/2606.19969v1)

## Abstract

When network links were slow, cloud and distributed database systems could rely on generic kernel abstractions and treat network communication as a black box. With today's fast cloud networks, this approach breaks down: database performance becomes limited by the CPU overhead of the kernel TCP stack. Replacing TCP with user-space UDP can reduce this overhead, but it requires reimplementing essential guarantees, such as reliability and ordering. To solve this conundrum, database systems should no longer treat networking as a black box but co-design it with database operations. We propose the bi-channel paradigm for database systems, which separates communication into two channels: A high-performance data path for latency- and bandwidth-sensitive operations, and a reliable control path for coordination and recovery. We implement the paradigm by combining user-space UDP and kernel-based TCP, though other stack combinations are possible. This design exploits modern NIC capabilities while preserving TCP's reliability. We demonstrate the paradigm's efficiency and simplicity in two representative settings: a distributed shuffle saturating 200 Gbit/s with three CPU cores, and a replicated key-value store processing millions of messages per second.
