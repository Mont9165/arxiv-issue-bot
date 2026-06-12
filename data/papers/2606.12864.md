# Beyond Problem Solving: UOJ-Bench for Evaluating Code Generation, Hacking, and Repair in Competitive Programming

- arXiv ID: `2606.12864v1`
- Authors: Tingqiang Xu, Hangrui Zhou, Tianle Cai, Alex Gu, Kaifeng Lyu
- Published: 2026-06-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.12864v1) | [pdf](https://arxiv.org/pdf/2606.12864v1)

## Abstract

Despite strong performance in competitive programming, the role of Large Language Models (LLMs) in supporting human learning in the same setting remains largely unexplored. In this work, we introduce UOJ-Bench, a benchmark designed to evaluate not only the problem-solving ability of LLMs, but also their ability to identify errors in human-written code -- a crucial educational activity traditionally supported by running test cases over online judge systems. UOJ-Bench consists of three distinct tasks: code generation, code hacking, and code repair, all constructed from real-world code submissions on the Universal Online Judge (UOJ) and evaluated through UOJ's native judging infrastructure. Our results show that under one-shot evaluation, even the strongest models fail to identify errors in more than 50% of a set of submissions that have been found to be incorrect by UOJ users. While test-time scaling improves success rates to above 90%, the substantial computational costs incurred from model inference limit its practicality for large-scale deployment. Despite these limitations, we find that the best-performing models under test-time scaling can uncover errors in over 5% of full-score submissions across roughly 30 problems, suggesting that frontier LLMs can already provide complementary signals beyond standard judging systems.
