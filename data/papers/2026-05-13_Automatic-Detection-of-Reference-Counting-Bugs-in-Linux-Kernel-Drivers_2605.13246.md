# Automatic Detection of Reference Counting Bugs in Linux Kernel Drivers

- arXiv ID: `2605.13246v1`
- Authors: Joe Hattori, Naoki Kobayashi, Ken Sakayori
- Published: 2026-05-13
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.13246v1) | [pdf](https://arxiv.org/pdf/2605.13246v1)

## Abstract

Reference counting bugs in Linux kernel drivers can lead to severe resource mismanagement and security vulnerabilities. We introduce DrvHorn, a novel automated tool to detect these bugs by reducing reference counting verification to an assertion checking problem leveraging the Linux driver interface. Through efficient modeling of the Linux kernel and aggressive program slicing, DrvHorn discovered 545 bugs, of which 424 were previously unknown, across all platform drivers in v6.6 Linux kernel, with a lower false positive rate of 29.9% compared to prior studies. To address the root causes of these newly discovered bugs, we submitted patches to the Linux kernel, and 45 of them were merged.
