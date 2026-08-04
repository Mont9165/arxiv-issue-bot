# FESOM2-JAX v1.0: a differentiable shadow of the ocean-sea-ice model FESOM2, cast onto GPUs

- arXiv ID: `2608.01546v1`
- Authors: Nikolay V. Koldunov, Sergey Danilov, Suvarchal Cheedela, Dmitry Sidorenko, Sebastian Beyer, Patrick Scholz, Ivan Kuznetsov, Jan Streffing, Aleksei Koldunov, Dmitrii Pantiukhin, Svetlana N. Loza, Thomas Jung
- Published: 2026-08-02
- Primary category: `physics.ao-ph`
- Categories: `physics.ao-ph`, `cs.SE`, `physics.comp-ph`, `physics.flu-dyn`
- Links: [abs](http://arxiv.org/abs/2608.01546v1) | [pdf](https://arxiv.org/pdf/2608.01546v1)

## Abstract

We present FESOM2-JAX, a Python re-implementation of the Finite-volumE Sea ice-Ocean Model (FESOM2) in JAX. The model retains the unstructured-mesh, cell-vertex finite-volume formulation of the original, runs unchanged from a laptop CPU to 256 GPUs, and is end-to-end differentiable. FESOM2-JAX is a code shadow of the Fortran model: a projection onto the Python ecosystem, translated with large language models and verified kernel by kernel against the original. It is built to lower the barrier to experimentation, from new numerics and parameterizations to gradient-based calibration and hybrid physics-machine-learning components, while remaining close enough to the original so that what is developed in the shadow can be transferred back. In a 1958-2019 hindcast at 1$^{\circ}$ equivalent resolution with identical physics and forcing, the mean states of the JAX and Fortran versions differ from each other by two orders of magnitude less than either differs from observations, and the two runs agree for six decades in global temperature, salinity, heat content, and sea ice. The complete 1$^{\circ}$ configuration fits on a single GPU, a node of four GH200 superchips integrates $\sim$113 simulated years per wall-clock day, and meshes of up to 7.4 million surface vertices ($\sim$5 km) scale to 128 GPUs. What limits the model is communication rather than arithmetic. What the shadow adds to the original is the gradient: a single reverse-mode pass through the full time loop returns the sensitivity of a model diagnostic to a parameter at every mesh vertex, verified against finite differences. To our knowledge, FESOM2-JAX is the first global ocean-sea-ice model of CMIP-class complexity written natively in a differentiable framework, and the first on an unstructured mesh.
