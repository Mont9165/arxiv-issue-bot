# RegoMender: A Multi-agent Framework for Automated Rego Policy Repair

- arXiv ID: `2610.29456v1`
- Authors: Ruijie Zhang, Huaxiao Yin, Li Hu, Fanqi Kong, Haozhe Liang, Shaoyin Cheng, Kun Zhang, Bibo Tu
- Published: 2026-10-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.29456v1) | [pdf](https://arxiv.org/pdf/2610.29456v1)

## Abstract

Policy-as-Code (PaC) has emerged as a foundational paradigm in cloud-native systems. However, repairing Rego policies remains challenging due to their strict syntax, declarative semantics, and specific verification requirements. Existing automated program repair (APR) methods are mainly designed for mainstream languages and struggle to accommodate the unique policy logic and repair workflows of Rego. Thus, Rego policy repair remains a manual process driven by trial and error. To address this, we introduce RegoBench, the first automated Rego policy benchmark comprising 1,159 real-world defects, and propose RegoMender, a feedback-guided multi-agent framework. Collaborating via a shared blackboard and an atomic toolkit, RegoMender dynamically executes patching, rewriting, or rolling back, to resolve complex repair scenarios. Evaluated on RegoBench, RegoMender achieves syntactic and test-based semantic success rates of 82.9\% and 77.9\%, respectively, outperforming the strongest baseline by 13.4\%. Unlike other approaches whose performance drops in complex scenarios, RegoMender maintains effectiveness across single-step and chained repair tasks. Furthermore, it generalizes strongly across HCL and SQL and achieves an 86.4\% repair rate on 132 real-world CVE vulnerabilities, proving its robustness and practical utility for security.
