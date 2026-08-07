# A Principled Framework for Safe Algorithm Updates in Automated Insulin Delivery Systems

- arXiv ID: `2606.13882v1`
- Authors: Thomas Screven, Ziqiang "Joe" Zhu, Deniz Cengiz, Rayhan A. Lal, Korey K. Hood, Samuel T. King
- Published: 2026-06-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.OS`
- Links: [abs](http://arxiv.org/abs/2606.13882v1) | [pdf](https://arxiv.org/pdf/2606.13882v1)

## Abstract

Background: AID algorithms require ongoing software updates and bug fixes. In co-adapted systems, where users tune settings around existing algorithmic behavior, bug fixes can paradoxically disrupt glycemic control. No principled framework evaluates the safety of AID algorithm updates.
  Methods: Our two-part framework classifies bugs and evaluates the clinical equivalence of AID system software updates. Bugs are classified as factual, heuristic, or computational, each with distinct management strategies. Classifications were validated from porting Trio's oref algorithm from Javascript to a bug-fixed Swift implementation. We compared implementations using shadow execution on 736,480 invocations from eight Trio users. The second component assesses clinical equivalence with error analysis on paired glucose values, applied to both Trio implementations using mechanistic in silico and data-driven replay simulation.
  Results: In mechanistic in silico simulation, the Swift and Javascript implementations produced nearly identical Time in Range (84.9% vs. 84.9%) and Glycemia Risk Index (23.5% vs. 23.9%), with more than 99% of paired glucose in Parkes Error Grid Zones A and B, meeting our clinical equivalence threshold. Shadow execution showed low mismatch rates in oref components (iob 0.43%, autosens 1.22%, determineBasal 0.07%, meal 0.01%), with clinically meaningful differences in 0.03% of iob invocations. Data-driven replay simulations of bugs revealed more than 99% of downstream paired glucose in Parkes Error Grid Zones A and B, also meeting our clinical equivalence threshold.
  Conclusions: Our framework integrates bug-fixing principles with multi-method clinical evaluation to assess AID algorithm update safety. It is system-agnostic and applicable to all widely used OS-AID systems, with case studies highlighting the need for systematic remediation of factual and computational bugs.
