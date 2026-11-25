# Generating Property-Based Regression Tests from Source Code Semantics

- arXiv ID: `2611.32636v1`
- Authors: Clemens Bauer, Johann Glock, Martin Pinzger
- Published: 2026-11-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.32636v1) | [pdf](https://arxiv.org/pdf/2611.32636v1)

## Abstract

Conventional unit tests (CUTs) check a method under test at fixed concrete inputs. A test can therefore miss a regression if its input produces the expected output despite a fault. Property-based testing (PBT) checks universally quantified specifications across many randomly generated inputs, but writing properties and input generators by hand is difficult. Existing approaches automate PBT creation by generalizing an existing or generated unit test suite. They either over-approximate concrete inputs across repetitive tests or apply single-path symbolic analysis along concrete test runs. This paper presents an approach that derives property-based regression tests directly from source code semantics via multipath symbolic execution (SE). For each explored path through a target method, the approach records a path semantics comprising the path condition, the symbolic return value, and the state change map. Each path semantics induces a Hoare triple that compiles into an executable property. Because SE leaves parts of a class unspecified, the approach complements the generated properties with search-based CUTs for the whole class. We evaluate our Java implementation against EvoSuite and the test generalization tool Teralizer on EqBench and on 11 projects from TOGBench. On EqBench, our approach keeps validated properties for 82.0% of all methods. Its mean mutation score of 63.8% exceeds the 55.2% of EvoSuite and the 60.3% of Teralizer. On TOGBench, target selection, SE limitations, and property validation restrict validated properties to 2.8% of all methods. The resulting mean mutation score of 48.6% falls below the 50.9% of EvoSuite and the 51.1% of Teralizer. Failures during test generation leave a few classes without effective tests and lead to this gap.
