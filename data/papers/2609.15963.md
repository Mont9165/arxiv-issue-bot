# Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities

- arXiv ID: `2609.15963v1`
- Authors: Fares Trad, Simin Chen, Hung Viet Pham, Gias Uddin, Baishakhi Ray
- Published: 2026-09-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.15963v1) | [pdf](https://arxiv.org/pdf/2609.15963v1)

## Abstract

Software agents with Large Language Models (LLMs) are designed for Automated Program Repair (APR) tasks, raising the possibility that, in the near future, APR agents will fix bugs automatically without much human intervention. Can we trust an APR agent to produce both functionally correct and secure code in such situations? What if attackers target production APR agents with adversarial issues that seem benign but may influence the agents to produce correct but insecure code? In this paper, we took a first step towards answering these questions by conducting an empirical study. First, we created SWEADV, a benchmark of 750 adversarial issue descriptions constructed from 150 repair tasks in SWE-bench Verified. For each repair task, we created five adversarial issue descriptions, one for each attack type: command execution, deserialization, path traversal, denial of service, and weak hashing. Second, we evaluated mini_swe APR agents from three LLM backends on SWEADV: GPT-5-Mini, MiniMax-M2.5, and DeepSeek-R. We found that on average, adversarial issue descriptions can induce malicious behaviors with successful repair in 51.7% of cases. Third, we investigated whether typical detection mechanisms are sufficient to prevent such malicious patches from being accepted. Pre-repair detection with LLM-as-judge on the adversarial issue descriptions resulted in an average detection accuracy of only 62.3%. Post-repair detection on adversarial APR patches using static analysis tools and LLM-as-judge achieved average detection accuracies of only 39.4% and 55.4%, respectively. We conclude that autonomous APR agents cannot be trusted yet in production deployment, given their susceptibility to adversarial attacks.
