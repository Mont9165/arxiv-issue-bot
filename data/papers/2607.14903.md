# FirmPilot: Evidence-Guided Multi-Agent Environment Recovery for IoT Firmware Rehosting

- arXiv ID: `2607.14903v1`
- Authors: Yanbing Shen, Fan Zhang, Haitao Xu
- Published: 2026-07-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.14903v1) | [pdf](https://arxiv.org/pdf/2607.14903v1)

## Abstract

Firmware rehosting executes firmware images in emulated environments such as QEMU to enable scalable dynamic analysis of Internet of Things (IoT) devices. In practice, rehosting pipelines remain fragile across diverse real-world firmware images, as reaching an externally observable execution state depends on tightly coupled artifacts spanning boot scripts, persistent configuration (e.g., NVRAM-like key-value state), and network setup. Template-driven frameworks often fail to accommodate long-tail vendor conventions, while unconstrained use of large language models (LLMs) risks unsupported modifications and irreproducible executions. We introduce FirmPilot, an evidence-guided multi-agent framework for environment recovery in firmware rehosting. FirmPilot reformulates rehosting as iterative environment reconstruction in which a search agent grounds decisions through similarity-based retrieval, a planner coordinates execution-accepted transitions, and specialized agents recover filesystem/init artifacts, persistent state, and network exposure. Through repeated execution and evidence-grounded artifact deltas, the system resolves cross-layer dependencies across boot, state, and networking that otherwise prevent firmware executions from reaching a stable, externally reachable state in emulation. Evaluated on the large-scale, real-world LFwC firmware corpus, FirmPilot improves web-service reachability over FirmAE from 25.49% to 52.39% and network reachability from 39.30% to 71.93%. The resulting rehosts raise the average number of detected services per firmware from 0.86 to 1.62 and support downstream analysis workflows, including RouterSploit interaction and protocol-aware fuzzing over recovered service surfaces. The evaluation shows that evidence- and feedback-grounded agent coordination improves rehosting success, service recovery, and downstream utility in automated firmware rehosting.
