# From TinyGo to gc Compiler: Extending Zorya's Concolic Framework to Real-World Go Binaries

- arXiv ID: `2605.03492v1`
- Authors: Karolina Gorna, Nicolas Iooss, Yannick Seurin, Rida Khatoun, Keith Makan
- Published: 2026-05-05
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03492v1) | [pdf](https://arxiv.org/pdf/2605.03492v1)

## Abstract

Zorya is a concolic execution framework that lifts compiled binaries to Ghidra's P-Code intermediate representation and uses the Z3 SMT solver to detect vulnerabilities by reasoning over both concrete and symbolic values. Previous versions supported only single-threaded TinyGo binaries. In this paper, we extend Zorya to multi-threaded binaries produced by Go's standard gc compiler. This is achieved by restoring OS thread states from gdb dumps, neutralizing runtime preemption, and introducing overlay path analysis with copy-on-write semantics to detect silent vulnerabilities on untaken branches. We rigorously assess Zorya on 11 real-world vulnerabilities from production Go projects such as Kubernetes, Go-Ethereum, and CoreDNS. Our evaluation shows that Zorya detects seven bugs at the binary level, including a silent integer overflow detects no other evaluated tool finds without a manually written oracle.
