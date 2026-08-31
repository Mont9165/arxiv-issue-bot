# GraftyVul: Synthesising Insecure Programs Through Real-World Vulnerability Grafting

- arXiv ID: `2608.27928v1`
- Authors: Omri Ram, Mitchell Horner, Ron Van der Meyden, Alsharif Abuadbba, Hammond Pearce
- Published: 2026-08-28
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.27928v1) | [pdf](https://arxiv.org/pdf/2608.27928v1)

## Abstract

Vulnerability datasets underpin a wide range of security research, including vulnerability detection, automated remediation, and secure code generation. However, existing datasets sacrifice at least one of three desirable properties: diversity (of language or vulnerability type), reproducibility/executability, or realism. We therefore present GraftyVul, a system that constructs vulnerable programs by grafting real-world vulnerabilities into open-source projects. This grounds the dataset in vulnerabilities observed in real-world contexts while harnessing known good build and test environments, enabling exploit-verification scripts to guarantee that an introduced vulnerability successfully alters a program's behaviour. Using GraftyVul, we generate 212 verified and exploitable vulnerable programs spanning five programming languages (Python, TypeScript, Java, Go, and C#) across 23 CWE categories. To evaluate fidelity, we introduce a language- and context-agnostic semantic embedding that compares vulnerabilities by sink, mechanism and host-feature rather than surface code. This approach outperforms standard code embeddings on cross-language clone and CWE classification. These embeddings demonstrate that GraftyVul samples retain a strong semantic signature to their source vulnerability. We additionally compare GraftyVul against 13 widely used datasets, where it attains competitive diversity while being the only reproducible-exploit dataset with broad language and CWE coverage. Finally, we illustrate GraftyVul's practical utility through an industrial case study evaluating a production vulnerability remediation system.
