# GapFuzz: Cross-Plane Divergence Fuzzing for Distributed SDN Controllers

- arXiv ID: `2606.11035v1`
- Authors: Moustapha Awwalou Diouf, Samuel Ouya, Jacques Klein, Tegawendé F. Bissyandé
- Published: 2026-06-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.11035v1) | [pdf](https://arxiv.org/pdf/2606.11035v1)

## Abstract

Distributed Software-Defined Networking (SDN) clusters replicate flow state asynchronously between a master node and its backups, leaving a window during which two backup nodes can each commit a contradictory rule, the master can serialize both into the data plane, and the kernel datapath can latch onto an action that no node believes authoritative. Existing SDN fuzzers miss this fault: they confine their oracle to the control plane, target a single controller, or do not steer concurrency to provoke replication races.
  We present GapFuzz, a stateful concurrency fuzzer for distributed SDN clusters. GapFuzz injects pairs of contradictory Northbound requests on two non-master nodes with controlled inter-injection delay $Δt$, and reconstructs the global cross-plane state by querying every replica and the kernel-datapath action through ovs-appctl ofproto/trace. A two-phase timing search detects whether a divergence exists, then doubles and bisects on $Δt$ to bound the injection-time window; a lifetime probe labels each verdict transient or persistent and assigns it to one of four cross-plane state classes derived from the ONOS 2.7 source.
  On a three-node ONOS 2.7 cluster, GapFuzz produces a divergent verdict in 81.7% of attempts ($N=50$, Wilson 95% CI $[77.3, 85.4]$%); every divergence sits between the cluster's authoritative state and the kernel datapath. Phase 2 separates a 5 ms race window for one template from a doubling-cap regime ($Δt_{\max}=10.24$ s) for six others, and 99.4% of divergences persist past 30 s. Replacing the kernel-datapath probe with the OpenFlow user-space probe used by prior fuzzers drops detection by 26.6 percentage points overall and by 46.5 points after excluding canonicalization-forced verdicts.
