# Software Refactoring Research with Large Language Models: A Systematic Literature Review

- arXiv ID: `2611.14027v1`
- Authors: Sofia Martinez, Luo Xu, Mariam Elnaggar, Eman Abdullah AlOmar
- Published: 2026-11-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.14027v1) | [pdf](https://arxiv.org/pdf/2611.14027v1)

## Abstract

Background: Code refactoring is the improvement of code internally without changing the external functionalities of the program. Due to its exhaustive nature, developers often avoid manually refactoring code. Researchers have since looked into utilizing LLMs to automate the task of refactoring. Aim and Method: Despite the promising results, there is a lack of clear un- derstanding of LLMs' effectiveness in automated refactoring. Result: From our literature review we found that: (i) there are various tools that different studies use to enhance and study LLM-driving refactoring, with tools that were used to detect code smells, generate code bases, and compare refactoring outcomes. (ii) Various datasets were collected from multiple open- source projects in multiple programming languages for analysis. These platforms included GitHub, Apache, and F-Droid, with the most popular language collec- ted and analyzed being Java. (iii) One-Shot, Few-Shot, Context-Specific, and Chain-of-Thought prompting methods have been shown to be the most effective depending on the language used. In some instances, being capable of reducing code smell by up to 89%. (iv) The definition of "accuracy" varies significantly across the literature surveyed, as this depends on the context of the study, thus calling for a need to have a standardized measurement for Accuracy. (v) The most often mentioned code smells were Large Class and Long Method, with a lot of studies also not specifying, while the most often applied refactoring type is Extract Method, showing promising results in using LLM to perform this refactoring type. (vi) When working with LLMs, they often generate erroneous code, struggle with more complex refactoring, and often misunderstand the developers' requests and miss refactoring requests.
