# Semantic Voting: Execution-Grounded Consensus for LLM Code Generation

- arXiv ID: `2605.08680v1`
- Authors: Shan Jiang, Zijian Yi, Chenguang Zhu
- Published: 2026-05-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.08680v1) | [pdf](https://arxiv.org/pdf/2605.08680v1)

## Abstract

LLM code-generation pipelines often sample multiple candidates and select one final answer without access to a complete oracle. Existing pipelines mix textual voting, ranking, and execution-based agreement, but the relative contribution of each component remains unclear. We study 18 configurations across different models, thinking levels, and benchmarks, comparing output-pattern majority voting, weighted voting, MBR-Exec, and SemanticVote - a method that clusters candidates by execution fingerprints on LLM-generated inputs. Three findings emerge. (1) The best execution-based selector exceeds output-pattern majority voting by 19-52 percentage points on every configuration, with every execution-based selector exceeding it by at least 18 points. (2) Once candidates are executed on diverse inputs, aggregation rule has limited effect: SemanticVote, weighted voting, and MBR-Exec are statistically indistinguishable across all 18 configurations. The largest factor is input quality: sketch-based input generation consistently outperforms direct LLM generation by 0.6-2.1 pp and random fuzzing by up to 11.3 pp. (3) Thinking level interacts differently with selection families: deeper thinking improves majority voting by 12 pp but execution-based methods stay flat or degrade as candidate diversity falls. These results frame inference-time code selection as a signal-quality problem rather than an aggregation-rule problem: when oracles are unavailable, the behavioral evidence matters more than the aggregation rule.
