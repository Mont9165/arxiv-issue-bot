# Building the Truman Show: A TrustZone-Based Framework for Lightweight Out-of-band Kernel Security Monitoring

- arXiv ID: `2608.29758v1`
- Authors: Zhenling Duan, Pan Dong, Renshuang Jiang, Xiaoxiang Fang, Bao Li
- Published: 2026-08-30
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29758v1) | [pdf](https://arxiv.org/pdf/2608.29758v1)

## Abstract

The increasing number of vulnerabilities in operating systems, together with sophisticated kernel-level threats (e.g., rootkits), has weakened the effectiveness of traditional in-kernel protection mechanisms. Since these defenses operate at the same privilege level as the kernel, they share the same attack surface and can be bypassed once the kernel is compromised. Isolation-based security approaches provide stronger protection by separating security logic from the kernel, but strict isolation often introduces semantic gaps that limit system visibility and hinder timely threat detection. In this paper, we present LOOM, a lightweight out-of-band operating system monitoring architecture built on ARM TrustZone. By leveraging TrustZone's hardware-enforced isolation, LOOM establishes a tamper-resistant monitoring environment independent of the kernel. To bridge the semantic gap, we design a lightweight semantic reconstruction mechanism in the Secure World. It selectively captures the states and behavioral patterns of critical kernel objects, such as process control blocks and kernel modules. Additionally, LOOM introduces a dual-stage hazard prevention mechanism that combines atomic memory protection with an interrupt-driven adaptive agent to detect and mitigate kernel rootkit activities. An address translation cache is further incorporated to optimize repeated address access and reduce monitoring overhead. Overall, we develop a multi-layered collaborative architecture with platform, functional, and auxiliary layers for secure and efficient kernel monitoring. A prototype of LOOM has been implemented on the Phytium D2000 platform. Experimental results indicate that LOOM incurs negligible overhead while maintaining a strong monitoring capability. Furthermore, a security capability analysis based on CVE cases demonstrates that LOOM can detect and mitigate various kernel attacks.
