# Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning

- arXiv ID: `2611.17304v1`
- Authors: Gustavo Pinto
- Published: 2026-11-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.17304v1) | [pdf](https://arxiv.org/pdf/2611.17304v1)

## Abstract

Large language model (LLM) coding agents are increasingly asked not only to write code but to debug running systems from live runtime data. We report a field observation of one such agent (Claude Code) as it diagnosed eight database incidents in a production message-dispatch engine. In every incident whose root cause depended on runtime concurrency, the agent announced a cause, shipped a fix, and later walked it back, and each wrong guess cost a deploy-and-observe cycle. Mapping each incident to what the agent lacked, we find that access to production state was the most pervasive bottleneck. The missing access included live lock views, untruncated deadlock reports, read-only execution, and an explicit environment context. An access gap was present in all five concurrency-dependent incidents: alone in one, and in four combined with a reasoning error such as anchoring on an early cause, incomplete exploration of the configuration, or a misreading of the code's transaction semantics. The three incidents that did not depend on concurrency needed nothing beyond what the agent already had. Within the incidents, the agent's wrong hypotheses were consistent with the evidence it could see; they were not fabrications. We argue that the next step for production-debugging agents is a forensics layer that gives the agent the access it lacks inside existing security controls. Such a layer would combine a safe interrogation API, a lock-and-deadlock flight recorder, and a production replay harness.
