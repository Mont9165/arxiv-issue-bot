# General Science Ranking (GSR): An Open-Source, Citation-Normalized Journal and Conference Classification System for Computer Science and Medicine

- arXiv ID: `2605.17657v1`
- Authors: Zhikai Yu
- Published: 2026-05-17
- Primary category: `cs.DL`
- Categories: `cs.DL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.17657v1) | [pdf](https://arxiv.org/pdf/2605.17657v1)

## Abstract

The academic journal zoning system is central to evaluating research talent, funding, and institutions. The CAS journal partition system, one of East Asia's most widely used tools, will cease operation in March 2026, creating a policy gap. Existing alternatives have major limitations: JCR depends on paid databases and excludes conferences; Scimago/CiteScore relies on Elsevier proprietary data; expert-based rankings such as CCF and CORE lack quantitative foundations and update slowly.
  This paper proposes the General Science Ranking (GSR), a multidimensional bibliometric framework built entirely on open-source data. GSR covers 500 computer science venues (397 journals and 103 conferences) and 500 medical journals using OpenAlex and Semantic Scholar. Scores combine four indicators: field-weighted citation impact (FWCI), two-year impact factor (IF2), five-year h-index (h5), and citation CAGR. For CS conferences lacking citation time-series data, IF2-approx was estimated from calibration on 1.41 million OpenAlex journal papers. Rankings adopt fixed quotas: Q1 (1-50), Q2 (51-100), Q3 (101-200), and Q4 (201+). All code and data are open source.
  In CS rankings, conferences and journals each occupy 25 of the top 50 Q1 positions. The leading conferences are NeurIPS, ICCV, ICLR, and CVPR. In medicine, CA: A Cancer Journal for Clinicians ranks first, followed by New England Journal of Medicine and The Lancet. Agreement with JCR Q1 reaches 84 percent in medicine and 71 percent in CS. Sensitivity analysis shows only 1.7 percent to 2.5 percent of CS conferences change partitions, indicating robustness.
  GSR provides a free, reproducible, field-normalized ranking system covering both journals and conferences, making it suitable for institutional evaluation policies.
