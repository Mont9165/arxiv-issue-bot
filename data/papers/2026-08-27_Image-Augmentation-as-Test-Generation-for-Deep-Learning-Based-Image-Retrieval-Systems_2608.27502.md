# Image Augmentation as Test Generation for Deep Learning-Based Image Retrieval Systems

- arXiv ID: `2608.27502v1`
- Authors: Yehan De Silva, Anirudh Sridhar, Armin Lotfy, Nafiseh Kahani, Yvan Labiche, Ziyu Wang, Frank Ouyang, Clare Carty, Azalia Shamsaei
- Published: 2026-08-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CV`
- Links: [abs](http://arxiv.org/abs/2608.27502v1) | [pdf](https://arxiv.org/pdf/2608.27502v1)

## Abstract

Ensuring the reliability of deep learning-based image retrieval systems is a software engineering challenge. This paper presents a dual contribution: (1) a literature review of augmentation and generation techniques which resulted in the identification of 50 techniques which we organized into a ten-category taxonomy, and (2) a large-scale empirical study that evaluates these techniques as test generators for embedding-based image retrieval systems. Augmented images are embedded using Amazon Titan and OpenCLIP, and evaluated across four analytical dimensions: (1) embedding-space similarity, (2) embedding uncertainty measured via four estimators, (3) semantic realism scored by LLaVA, and (4) retrieval failure rate. Experiments are performed on three datasets: CIFAR-10, ImageNet-1K, and a dataset from an industrial partner (March Networks). Across all evaluated datasets and embedding models, and under the single severity level tested for each technique, weather simulation and SaSPA are the image augmentation/generation techniques that produce the highest embedding uncertainty and failure rates while maintaining a favorable balance between performance stability, visual realism, and augmentation effectiveness. The results we discuss are configuration-specific and may shift under milder or stronger perturbation settings. In contrast, GAN-based augmentation techniques are among the lowest in realism, indicating the presence of synthetic artifacts and perceptual inconsistencies that reduce their suitability to produce realistic test inputs. Overall, our findings provide practical guidelines for selecting augmentation techniques that maximize test diversity while preserving realistic image characteristics, thereby enabling the construction of comprehensive and effective test suites for image retrieval systems while reducing the cost of manual data labeling through the use of metamorphic testing.
