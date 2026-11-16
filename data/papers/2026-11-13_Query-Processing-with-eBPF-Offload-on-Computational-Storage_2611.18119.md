# Query Processing with eBPF-Offload on Computational Storage

- arXiv ID: `2611.18119v1`
- Authors: Alexander Krause, Niclas Hedam, Johannes Pietrzyk, Dirk Habich, Wolfgang Lehner, Sangjin Lee, Alberto Lerner, Philippe Bonnet
- Published: 2026-11-13
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.18119v1) | [pdf](https://arxiv.org/pdf/2611.18119v1)

## Abstract

The idea of pushing computation to storage devices has been explored for decades. In recent years, research has focused on computational storage, i.e., devices that allow a host to execute functions as I/O commands on local data. Today, the NVMe and SNIA computational storage standards share an execution model in which the host invokes functions on the device, on data that the host has moved into device memory. Both standards single out eBPF as a format for functions offloaded by the host. In this paper, we study whether this form of computational storage is a good match for query processing. We present the design and implementation of Delilah, a prototype based on an open-hardware device that implements the standard execution model on an actual device and runs eBPF programs calling device-resident functions. As an initial step, we hand-coded a portion of SSB Q3.3 for execution on the device, aiming to integrate computational storage with a database system's storage manager. The series of experiments that we ran showed that offloading gains little over host execution, execution degenerates into column-at-a-time processing, and time is spent staging and moving data in device memory. Because these roadblocks stem from the execution model rather than from the query, we did not pursue integration further. We detail these limitations and lay the groundwork for a different computational storage model better aligned with data-intensive workloads.
