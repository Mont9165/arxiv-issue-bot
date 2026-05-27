# Names Are All You Need: Effective and Safe Regression Test Selection for Python

- arXiv ID: `2605.25356v1`
- Authors: You Wang, Michael Pradel, Zhongxin Liu
- Published: 2026-05-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.25356v1) | [pdf](https://arxiv.org/pdf/2605.25356v1)

## Abstract

Regression test selection reduces the cost of regression testing by executing only those tests affected by a code change. Despite extensive study of RTS in statically typed languages, achieving effective and safe RTS in Python is challenging. Python's dynamic typing makes precise call-graph construction difficult, which can cause call-graph-based RTS to miss affected tests. Python's eager importing mechanism, in contrast, renders file-level dependency analysis overly conservative. This paper presents NameRTS, the first Python RTS approach based on fine-grained dependency analysis. NameRTS models a Python program as a bipartite graph of code element nodes and name nodes, with edges capturing definitions and references. RTS is formulated as a reachability problem on this graph: a test is selected if any modified code element is reachable from the names used in that test. This design avoids call-graph construction, enabling a conservative analysis amenable to safety. To control dependency cascades introduced by coarse name matching, NameRTS applies two pruning strategies that leverage prior test executions and context information to refine name matching. To evaluate NameRTS, we construct the first Python RTS dataset with a ground truth indicating which test files are affected by each commit. We compare NameRTS with the best-performing baseline, BabelRTS, an RTS technique based on coarse file-level dependencies. On this benchmark, NameRTS skips 69.90% of test files on average, outperforming BabelRTS by 146.5%. It also reduces end-to-end testing time by 45.59%, yielding a 107.7% improvement over BabelRTS. In terms of safety, NameRTS selects all affected tests for 99.6% of commits, with only rare misses in exceptional cases. In contrast, BabelRTS is safe for 76.6% of commits. These results demonstrate the effectiveness of NameRTS, paving the way for more efficient regression testing in Python.
