# Mission (Im)Possible: Towards Autonomous Discovery of Autopilot Logic Flaws in Open-Source Drone Frameworks

- arXiv ID: `2610.19566v1`
- Authors: Ziyi Liang, Zichuan Li, Bin Yuan, Deqing Zou, Luyi Xing
- Published: 2026-10-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.19566v1) | [pdf](https://arxiv.org/pdf/2610.19566v1)

## Abstract

Autonomous drones are increasingly deployed in safety-critical tasks, yet their autopilot software can still contain subtle logic flaws that lead to unsafe behaviors. These flaws are difficult to discover with existing techniques because they often depend on semantic relationships across modules, commands, and runtime state, and rarely manifest as crashes or detectable failures. With recent advances in LLMs, we observe that, when equipped with essential domain knowledge and carefully crafted context, LLMs demonstrate strong capabilities in understanding the high-level semantics of autopilot systems, making them suitable for logic flaw discovery. However, LLMs are limited by their context and can be biased to the vulnerabilities frequently occurs in training dataset, while logic flaws often require higher-level semantic bug oracles to identify their existence. To bridge the gap, we present Impossible Mission Finder (IMF), a multi-agent system combining static analysis, dynamic execution and log analysis, that supports fully automated identify, test, and validate logic flaws in autonomous vehicles. IMF primarily contains three LLM agents, it first uses the auditor agent to propose logic flaw hypothesis based on carefully-crafted program slicing, then it launches tester agents to write and execute test cases for each candidate, and finally it spawns the log analyzer agent to validate the execution log against the flaw hypothesis. This enables IMF dynamically validate bug oracles in a case-by-case manner, making it suitable for discovering logic flaws that do not have a unified pattern. We evaluated IMF on two widely used open-source autopilot systems, PX4 and Ardupilot, leading to 105 previously unknown logic flaws, that can cause unsafe behaviors including mission interruption failures, invalid actions, entering into restricted fly zones etc.
