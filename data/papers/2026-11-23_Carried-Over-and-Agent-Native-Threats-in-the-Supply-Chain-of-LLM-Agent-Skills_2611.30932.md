# Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills

- arXiv ID: `2611.30932v1`
- Authors: Kaixuan Li, Wenbo Guo, Sen Chen, Yang Liu
- Published: 2026-11-23
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.30932v1) | [pdf](https://arxiv.org/pdf/2611.30932v1)

## Abstract

Agent skills are reusable packages that extend a large language model (LLM) agent with scripts, third-party dependencies, and natural-language instructions. An agent builds a skill's arguments from user requests and untrusted external content, so a flaw left by a benign author can escalate a prompt injection to code execution. Existing studies target malicious skills or a single attack vector, and none tests whether an agent can reach such flaws. We present the first registry-scale empirical study of the supply chain attack surface arising from unintentional vulnerabilities in agent skills, over all 48,682 skills in ClawHub. The study covers two carried-over risks, dependencies and first-party code, and two agent-native ones, install instructions and credentials printed to stdout. We screen all skills by static analysis, manually review all 3,428 cases flagged by the four main detectors, and test reachability by running sampled flagged skills in a sandbox and with a live LLM agent under indirect prompt injection. First, dependency risk carries over in a different form: 49.6% of the skills with resolvable dependencies depend on a version with a known CVE, and unlike npm packages, which mostly become vulnerable after release, 78.3% of them are born vulnerable, already exposed at publication. Second, few of these CVEs are reachable: agent input reaches the vulnerable function in only 3.0% of the affected skills, whereas 21 of 22 sampled first-party flaws are exploited end to end in the sandbox. Third, a live agent executes the injected payload in 48.5% of the sampled flagged skills, but almost always in its own shell before the skill runs, and the payload reaches a flaw in the skill itself in only 5.0%. Hence, registries should prioritize first-party flaws over dependency alerts, and agent runtimes should not pass skill arguments through a shell.
