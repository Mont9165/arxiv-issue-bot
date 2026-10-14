# Collaborative Multi-Agent Testing for Emergent Failure Discovery in Autonomous Driving Systems

- arXiv ID: `2607.06078v1`
- Authors: Ruizhen Gu, Konstantinos Koufos, Donghwan Shin, Vahid Garousi, Mehrdad Dianati
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06078v1) | [pdf](https://arxiv.org/pdf/2607.06078v1)

## Abstract

Autonomous Driving Systems (ADS) can fail because of faults within individual modules as well as from interactions across perception, planning, and control. Yet existing ADS testing research often treats key testing functions, such as perturbation generation, behavioural assessment, and test case selection and exploration, as loosely coupled steps rather than coordinated roles for discovering such failures. We present CREAD, a collaborative multi-agent testing framework for testing ADS that organises perturbation generation, behavioural validation, and search coordination through a shared blackboard and an orchestrator. In the current work-in-progress instantiation, the framework focuses on perception-oriented perturbation generation, while remaining extensible to other ADS modules, including planning and control. It currently comprises a Perception Fuzzer Agent, a Metamorphic Validator Agent, and an Orchestrator Agent. Respectively, they generate perturbations, assess behavioural consistency across related scenario pairs, and coordinate further exploration. Experiments in HighwayEnv simulator show that the collaborative configuration improves failure discovery in the highway environment and remains competitive in the roundabout setting. Across the two environments, it yields about 2.1x as many failures per 100 scenarios as the single-agent baseline on average, while gains over a non-collaborative two-agent baseline vary across environments. These results suggest that collaborative multi-agent testing is a promising research direction for emergent ADS behaviour discovery.
