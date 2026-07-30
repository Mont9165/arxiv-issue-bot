# Not In My Git Yard: Catching Backdoors at Commit and Release Time

- arXiv ID: `2607.26719v1`
- Authors: Dimitri Kokkonis, Michaël Marcozzi, Stefano Zacchiroli
- Published: 2026-07-29
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26719v1) | [pdf](https://arxiv.org/pdf/2607.26719v1)

## Abstract

Code-level backdoors-stealthy code changes that grant hidden privileges via secret triggers-pose a persistent threat to opensource software. Known attempts to inject such backdoors into widely used projects through malicious commits, tampered release packages, or compromised third-party dependencies, were stopped only by luck and manual review. Existing Continuous Integration (CI) pipelines cannot detect these attacks, and downstream binary analysis tools require substantial manual effort. In this work, we present Lily, an automated approach that strengthens open-source development and release processes against backdoor injection. Lily integrates a backdoor detection mechanism into (1) CI pipelines to block malicious commits, and (2) release vetting workflows to prevent tampered releases or compromised dependencies from entering large ecosystems, such as Linux distributions. Lily offers two key contributions. First, it enhances CI-compatible fuzzing with the capability to detect triggers of suspicious behavior based on historical and current software executions. This enables fast, precise backdoor detection suitable for both CI and update validation workflows. Second, it combines code change analysis with fuzzing data to precisely point maintainers to backdoor-revealing code regions, even when release updates modify millions of lines of code. We also outline five strategies attackers could use to evade Lily, and evaluate corresponding defenses. Our experiments across hundreds of benign and backdoored commits and releases show that Lily achieves high detection accuracy with low false alarm rates, reliably identifies malicious code, resists adversarial attempts, and would have prevented real-world backdoor incidents.
