# Delta Debugging in the Absence of Test Oracles Through Metamorphic Testing

- arXiv ID: `2607.00929v1`
- Authors: Mingyue Jiang, Yongqiang Tian, Tsong Yueh Chen
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00929v1) | [pdf](https://arxiv.org/pdf/2607.00929v1)

## Abstract

Delta debugging provides an automatic way to minimize a program input while preserving a certain property. However, its effectiveness fundamentally relies on the availability of test oracles to determine whether a reduced input still preserves the specific property. Consequently, the oracle problem substantially limits the applicability of existing delta debugging techniques, particularly for oracle-deficient programs where output correctness cannot be directly determined. To address this problem, this paper proposes a novel approach, DDMT, to enhance the applicability of delta debugging, especially facilitating its application to oracle-deficient programs. Our key insight is to redesign an oracle-independent test function and incorporate it into the reduction procedure of delta debugging such that the property-preservation validation can be accomplished without requiring a test oracle. To this end, DDMT employs the technique of metamorphic testing, which is a property-based and oracle-independent testing method. It establishes a metamorphic testing-based test function, using it as a replacement for the original test function adopted by delta debugging. The experiments evaluate DDMT on 66 subjects across both oracle-available and oracle-deficient scenarios, with different delta debugging approaches. The results positively confirm that DDMT can enhance the applicability of delta debugging while often preserving or improving reduction effectiveness and query efficiency. Furthermore, compared to the relevant delta debugging approaches, DDMT is also able to achieve performance improvements with proper configurations.
