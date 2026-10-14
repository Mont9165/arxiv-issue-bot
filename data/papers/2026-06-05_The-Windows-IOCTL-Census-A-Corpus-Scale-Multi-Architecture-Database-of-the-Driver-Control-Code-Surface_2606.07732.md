# The Windows IOCTL Census: A Corpus-Scale, Multi-Architecture Database of the Driver Control-Code Surface

- arXiv ID: `2606.07732v1`
- Authors: Michael J. Bommarito
- Published: 2026-06-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.07732v1) | [pdf](https://arxiv.org/pdf/2606.07732v1)

## Abstract

A Windows driver exposes its kernel through I/O control (IOCTL) codes, and a single unchecked length on the buffer behind one turns an unprivileged call into a kernel write. The research community has strong scanners for this surface and a curated list of known-bad drivers, but no map of the surface itself. We build that map. The Windows IOCTL Census is a queryable database of the control-code dispatch surface of 27,087 signed Windows drivers, recovered by one deterministic, architecture-neutral pass with no symbolic execution. Reading a lifted intermediate representation instead of running a symbolic engine lets it recover a dispatch surface for 80% of the corpus across x86 and x64, including the 32-bit half existing scanners abort on. On the 64-bit lane it adds handler reachability, taint, and the call graph. An LLM ranks the reachable handlers for triage. We release the census as a public dataset of tens of millions of rows: 27,087 binaries, 3.1M decoded control codes, 8.18M functions, and 15.95M call edges.
