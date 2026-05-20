# When Web Apps Heal Themselves: A MAPE-K Based Approach to Fault Tolerance and Adaptive Recovery

- arXiv ID: `2605.19261v1`
- Authors: Sales Aribe, Rov Japheth Oracion
- Published: 2026-05-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.HC`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2605.19261v1) | [pdf](https://arxiv.org/pdf/2605.19261v1)

## Abstract

Ensuring the reliability and resilience of modern web applications remains a critical challenge due to increasing system complexity and dynamic runtime environments. This study proposes a modular self-healing framework based on the monitor-analyze-plan-execute over a shared knowledge base (MAPE-K) model, integrated with an AutoFix-inspired mechanism for adaptive fault recovery. Using a design and development research (DDR) approach, the system was implemented and evaluated through controlled fault injection experiments across twenty runtime failure scenarios, including service crashes, memory leaks, and database disconnections. Experimental results demonstrate that the proposed framework achieved a mean fault detection F1-score of 90.7% and a recovery success rate of 93.2%. The AutoFix module reduced the average time-to-recovery (TTR) by 56.2%, achieving an average recovery time of 3.92 seconds. System throughput was maintained between 88% and 95% during fault conditions, with only a 3.1% increase in response time. Additionally, iterative feedback mechanisms improved recovery efficiency by 18.6% over multiple cycles. These findings indicate that the proposed framework provides a practical and extensible approach to enhancing fault tolerance in web applications through feedback-driven adaptation. While the current implementation relies on predefined recovery strategies, the integration of learning-oriented feedback establishes a foundation for future development of more autonomous self-healing systems.
