# Skills That Don't Exist: A Large-Scale Study of Hallucinated Skill Recommendation in LLM Agents

- arXiv ID: `2607.12340v1`
- Authors: Weifeng Yuan, Wenbo Guo, Feng Dong, Haoyu Wang, Yang Liu
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.12340v1) | [pdf](https://arxiv.org/pdf/2607.12340v1)

## Abstract

LLM agents acquire new capabilities by downloading skills from open registries. Instead of browsing these catalogs manually, developers typically ask the agent to recommend and install a skill. This convenience hides a risk: agents frequently invent names for skills that exist in no registry. We term this flaw skill name hallucination. A fake name may seem harmless, but it opens the door to supply-chain attacks. Because registries rarely verify publishers, an adversary can prompt the agent, collect the fake names it returns, pre-register malicious skills under them, and wait for a victim to install the payload. We conducted the first large-scale measurement of skill name hallucination, evaluating 15,000 prompts across 12 configurations (4 standalone LLMs and 8 agents). We conservatively counted a name as hallucinated only if it was missing from all live registries and GitHub. The results reveal a systemic vulnerability: every configuration hallucinates. Rates average 36.0% for standalone LLMs and 36.9% for agents, rising to 43.1% on real-world developer questions. In total, the systems generated 5,669 distinct hallucinated names. Crucially, these names are not random noise. Agents repeat the same fake names across prompts and models, giving attackers highly reliable targets to hijack. Finally, we tested four model-level defenses and found a severe conflict between security and usability. The strongest, retrieval grounding, cut the hallucination rate from 40.8% to 3.2% but crippled usefulness: even the best-defended system recommended the correct skill only about one in six times. Skill name hallucination is thus a highly exploitable vulnerability requiring minimal attacker effort. Fixing it cannot rely on prompt engineering or model tuning alone. It demands ecosystem-wide structural changes: registry-level name reservations and verified recommendation pipelines.
