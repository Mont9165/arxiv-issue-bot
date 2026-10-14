# X.js: A Live Benchmark for Node.js Taint-Style Vulnerabilities

- arXiv ID: `2610.18585v1`
- Authors: José Afonso, João Madeira Pereira, Ronghao Ni, Limin Jia, José Fragoso Santos, Pedro Adão
- Published: 2026-10-13
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.18585v1) | [pdf](https://arxiv.org/pdf/2610.18585v1)

## Abstract

JavaScript vulnerabilities in npm packages pose a significant risk to the Node.js ecosystem, and a growing body of work aims to detect, exploit, and mitigate them. Studying and evaluating this work requires up-to-date collections of real vulnerabilities, yet the most commonly used datasets stop recording vulnerabilities in 2022. We present X.js, a live benchmark of real-world Node.js taint-style vulnerabilities covering code and command injection, prototype pollution, and path traversal. Built from 1,738 advisories collected through mid-2026, primarily from the GitHub Advisory Database, X.js pairs each vulnerability with precise source and sink locations, a validated executable exploit and its execution trace, and, when available, a patched version of the package. X.js supports long-term reproducibility and growth: dependencies are mirrored in a self-hosted registry to guard against package removal from the ecosystem, and dedicated infrastructure generates and validates exploits for newly reported vulnerabilities. The current release contains 1,159 validated exploits for 965 packages. Using X.js, we characterize how the frequency, structure, and complexity of Node.js taint-style vulnerabilities have evolved over time. We find that these vulnerabilities are increasingly reported in large packages: the median vulnerable package grew from roughly 250 LoC in 2021--2022 to 6,100 LoC in 2026.
