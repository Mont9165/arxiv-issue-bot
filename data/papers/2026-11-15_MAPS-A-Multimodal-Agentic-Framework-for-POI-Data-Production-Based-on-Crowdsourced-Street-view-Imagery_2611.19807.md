# MAPS: A Multimodal Agentic Framework for POI Data Production Based on Crowdsourced Street-view Imagery

- arXiv ID: `2611.19807v1`
- Authors: Sijie Ruan, Tingyu Xie, Mingfei Liu, Yicheng Tang, Haoyu Han, Jingnan Qi, Jingshu Zeng, Dongqi Xu, Jing Wang, Shuliang Wang
- Published: 2026-11-15
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.19807v1) | [pdf](https://arxiv.org/pdf/2611.19807v1)

## Abstract

Point-of-interest (POI) databases support location-based services, yet urban changes quickly make their records stale and manual maintenance is costly. Crowdsourced street-view images provide timely visual evidence, but converting them into database actions requires separating multiple POIs and irrelevant text in each image, then resolving incomplete observations against ambiguous records. We study Street-view Image-based POI Data Production and propose MAPS, the first framework to integrate structured POI extraction with database maintenance from such imagery. MAPS contains two cascaded modules. SPICE progressively adapts a lightweight vision-language model to reconstruct and filter text, group entries belonging to the same POI, and classify their semantics and completeness. RIMA retrieves candidate records, performs evidence-grounded POI matching and attribute-level reasoning, and selectively acquires complementary visual, geospatial, or external-source evidence when necessary. In human-reviewed full-task evaluation, MAPS outperforms the strongest baseline by 21.8\%. MAPS has also been deployed in Kuaishou's large-scale POI production pipeline, reducing average processing time by 76.9\% relative to manual annotation. These results demonstrate the effectiveness and practical value of MAPS for scalable POI maintenance.
