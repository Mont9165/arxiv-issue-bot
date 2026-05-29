# Claim against Measurement: Statistical Artefacts in Quantum Error Mitigation Benchmarks

- arXiv ID: `2605.29872v1`
- Authors: Dominik Köster, Wolfgang Mauerer
- Published: 2026-05-28
- Primary category: `quant-ph`
- Categories: `quant-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.29872v1) | [pdf](https://arxiv.org/pdf/2605.29872v1)

## Abstract

QEM is widely regarded as a plausible bridge from NISQ devices to FTQC. Yet the empirical studies used to assess the effectiveness of QEM techniques on concrete problems have received comparatively little scrutiny with respect to the validity of their conclusions. We systematically review 81 recent QEM papers using an eight-criterion framework covering statistical rigour, reproducibility, and reporting quality. Among the applicable papers, only 15 (25%) use inferential methods, while 25 (42%) report uncertainty only descriptively, without testing whether the claimed effects are statistically supported. To demonstrate the consequences of these omissions, we use ZNE as a representative and widely used case study and identify two compounding sources of artefacts in current QEM benchmarks. First, we observe parameter sensitivity: in a 132-configuration sweep, implicitly assumed choices such as scale factors, extrapolation method, and hardware calibration are not merely incidental but active, with variations changing conclusions from statistically significant improvement to statistically significant degradation. Second, we identify a drift-induced effectiveness illusion: in a 72-hour longitudinal study on real hardware, temporal drift alone can make the same ZNE configuration exhibit an effect size more than three times as large, depending solely on when it is executed, and also drastically reduces the effective number of independent observations. These findings do not imply that QEM methods are intrinsically unsound; rather, they show that current evaluation practice can make mitigation performance appear more robust than the evidence warrants. We therefore propose minimum reporting standards for QEM evaluations, including explicit parameter documentation, robustness checks, longitudinal drift assessment, and inferential statistical testing with effect-size reporting.
