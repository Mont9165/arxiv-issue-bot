# An Ocean Model Ported by a Large Language Model: Experience and Lessons from FESOM2 (Fortran to C to C++/Kokkos)

- arXiv ID: `2606.11356v1`
- Authors: Nikolay V. Koldunov, Suvarchal K. Cheedela, Sergey Danilov, Dmitry Sidorenko, Sebastian Beyer, Thomas Jung
- Published: 2026-06-09
- Primary category: `physics.ao-ph`
- Categories: `physics.ao-ph`, `cs.DC`, `cs.SE`, `physics.comp-ph`
- Links: [abs](http://arxiv.org/abs/2606.11356v1) | [pdf](https://arxiv.org/pdf/2606.11356v1)

## Abstract

Large language models (LLMs) can translate and modify source code, and have been shown to do so for codes of different complexity. Whether they can port a complete, production geophysical model to a different language without degrading its physics has not been established. We demonstrate that LLM-assisted code translation can preserve the physics of a complete production ocean model while moving it into a modern performance-portable form. We report our experience using an agentic LLM coding assistant, directed by domain experts, to port the FESOM2 unstructured mesh ocean--sea-ice model (about 74000 lines of core Fortran) first to C and then to C++/Kokkos for performance portability across CPUs and GPUs. We describe the practices that proved necessary, what worked and what did not, and the failure modes that we encountered. Three practices mattered most: translating in two stages that separate reproducing the numerics (Fortran to a clean C reference) from introducing parallelism (C to Kokkos); requiring a strictly literal translation in which the assistant was not permitted to ``improve'' the source; and validating each stage against an acceptance criterion suited to it.
  The C port reproduces the original Fortran at the level of long-term simulation statistics over five years. The Kokkos port is bit-for-bit identical to the C reference on CPU and statistically close on GPU over multi-year runs. On eddy-rich meshes up to 7.4 million surface vertices a single A100 GPU node runs 1.6--3.7 times faster than a CPU node, reaching the 1-2 simulated-years-per-day required for production integrations. The result is more than a single GPU port: by following a clear validation procedure, an LLM moved a full Fortran ocean model into another language and onto accelerators while preserving its physics in a matter of weeks.
