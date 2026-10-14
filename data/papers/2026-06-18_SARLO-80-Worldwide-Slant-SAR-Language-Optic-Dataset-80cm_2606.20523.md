# SARLO-80: Worldwide Slant SAR Language Optic Dataset 80cm

- arXiv ID: `2606.20523v1`
- Authors: Solène Debuysère, Nicolas Trouvé, Nathan Letheule, Elise Colin, Georgia Channing
- Published: 2026-06-18
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.20523v1) | [pdf](https://arxiv.org/pdf/2606.20523v1)

## Abstract

Multimodal foundation models have advanced rapidly thanks to large optical benchmarks, but comparable resources for synthetic aperture radar (SAR) remain limited. Existing SAR--optical datasets largely rely on low-resolution, intensity-only Ground Range Detected~(GRD) products and do not preserve complex-valued SAR measurements or native acquisition geometry, which restricts physically grounded multimodal learning. In particular, large-scale public datasets combining very-high-resolution (VHR) SAR SLC, aligned optical imagery, and natural-language descriptions are still lacking. We present a VHR SAR--optical--text dataset built from open-access Umbra spotlight acquisitions distributed as Sensor Independent Complex Data (SICD). From around 2,500 worldwide scenes (VV/HH, 20cm--2m native resolution), we standardize all SAR data to an 80cm slant-range grid via band-limited FFT resampling and tile the imagery into 1024 by 1024 patches. For each SAR patch, we retrieve a high-resolution optical tile and warp it into the SAR grid using local coordinate correspondences for local pixel-level alignment. We further generate three caption variants (SHORT/MID/LONG) per sample to support vision--language training and evaluation. Our dataset contains 119,566 triplets (complex and amplitude slant-range SAR patch, aligned optical patch, natural-language description) covering 257 locations across 72 countries and a broad range of land types and infrastructures. We release fixed train/validation/test splits and the full preprocessing and baseline code to enable reproducible benchmarks for multimodal alignment on cross-modal retrieval and conditional generation in native SAR geometry. The dataset is publicly available on the Hugging Face Hub at https://huggingface.co/datasets/ONERA/SARLO-80.
