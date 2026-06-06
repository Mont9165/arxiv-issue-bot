# The World's Fastest Matching Engine Algorithm

- arXiv ID: `2606.01183v1`
- Authors: Jake Yoon
- Published: 2026-05-31
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.DB`, `cs.DS`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2606.01183v1) | [pdf](https://arxiv.org/pdf/2606.01183v1)

## Abstract

Every electronic exchange relies on an order book whose storage layer determines matching latency. The dominant implementation -- linked lists chained through a balanced tree -- imposes two costs on every operation: pointer-chased traversal to reach the insertion point, and root-to-leaf search to locate the target price level. Under micro-burst conditions these costs produce tail-latency spikes that degrade market quality when liquidity is most needed. We present two data-structure contributions that eliminate these costs. The first is the Priority-Indicated Node (PIN), a priority queue in which entries occupy fixed-capacity, contiguously addressable slots, each carrying a per-slot indicator encoding the entry's global priority. Unlike heaps, which require O(log n) comparisons per operation, the PIN resolves insertion position directly from the indicators without comparing entries; indicator updates are O(1), independent of queue size. The second addresses a broader inefficiency: balanced search trees search root-to-leaf on every insertion and deletion, even when the caller already knows the key's in-order neighbors -- as in ordered event streams, incremental index already knows the key's in-order neighbors -- as in ordered event streams, incremental index maintenance, and electronic trading. Neighbor-aware insertion and deletion exploit known neighbor references to attach or remove a node with O(1) reference writes, followed by single-path rebalancing, uniformly across red-black, AVL, and B/B+-tree variants. A single CPU core sustains 32 million order messages per second with sub-microsecond tail latency under multi-million message-per-second micro-bursts, and is 5-11x faster than the best available open-source matching engines on the same hardware. Scaled to a single 96-core instance, the engine sustains 640 million messages per second across 10,000 symbols.
