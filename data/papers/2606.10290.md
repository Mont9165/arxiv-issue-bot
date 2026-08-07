# The Linux IOCTL Census: A Source-Derived Database of the Linux Kernel Control-Code Surface

- arXiv ID: `2606.10290v1`
- Authors: Michael J. Bommarito
- Published: 2026-06-09
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.10290v1) | [pdf](https://arxiv.org/pdf/2606.10290v1)

## Abstract

The ioctl system call is Linux's catch-all device-control interface. A userspace program opens a device node and hands the driver a numeric command code and an argument buffer, and the driver does whatever that code means, whether configuring hardware, reading back state, or moving data into and out of the kernel. Drivers define these commands themselves, by the thousand, and parse their arguments in kernel context, which makes ioctl handlers one of the broadest and least uniform local attack surfaces in the kernel. A handler that trusts an argument length it never validates can read or write kernel memory out of bounds, and the command space is catalogued in no central place. We present the Linux IOCTL Census, a source-derived and queryable inventory of that surface. An allmodconfig build compiles 878 modules across 169 subtrees, and over them a single deterministic libclang pass over the kernel source recovers 586 ioctl dispatch entry points, 1,289 decoded _IOC command codes, 3,583 controlled-input sinks, and 1,298 permission gates. A second pass encodes the kernel's own documented threat model as a queryable column, separating the capability-ungated ioctl surface, an upper bound on unprivileged reach rather than proven reach, from the part a hard capability gate puts out of scope. We backtest the census against 22 recent in-tree ioctl CVEs and release the structural tier as open data, on a schema shared with the companion Windows IOCTL Census so a single query spans both operating systems.
