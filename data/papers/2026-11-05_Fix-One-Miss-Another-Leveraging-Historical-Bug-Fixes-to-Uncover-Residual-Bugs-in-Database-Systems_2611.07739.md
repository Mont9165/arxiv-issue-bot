# Fix One, Miss Another: Leveraging Historical Bug Fixes to Uncover Residual Bugs in Database Systems

- arXiv ID: `2611.07739v1`
- Authors: Yankai Rong, Zhaoyang Zhang, Shuang Liu, Wei Lu, Xiaoyong Du
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07739v1) | [pdf](https://arxiv.org/pdf/2611.07739v1)

## Abstract

Database management systems (DBMSs) implement SQL constructs through grammar-driven dispatch handlers. Although handlers for syntactic siblings implement different SQL constructs, they often share a common implementation pattern, including argument extraction, type checking, and permission validation. Consequently, a bug fix that hardens the handler exercised by a historical bug may leave the corresponding logic in sibling handlers vulnerable to the same semantic flaw. We refer to such defects as sibling bugs. Despite the structural similarity among sibling handlers, existing bug-finding techniques rarely exploit historical fixes to systematically uncover these related defects.
  We present Reaper, a novel approach for detecting sibling bugs guided by historical bug fixes. Reaper first analyzes a bug fix to infer a trigger profile, which characterizes the conditions under which the defect is exposed, and a validation profile, which captures the semantic evidence needed to distinguish buggy behavior from correct behavior. It then projects the trigger profile onto syntactic siblings through grammar-guided test mutation, generating tests that exercise corresponding semantic paths in sibling handlers. Finally, Reaper validates suspicious behaviors using the inferred validation profile through a staged validation process, reducing false positives caused by complex DBMS behavior.
  We evaluate Reaper on four widely used DBMSs, including MariaDB, MySQL, OceanBase, and CockroachDB. Reaper uncovers 61 previously unknown bugs, of which 57 have been confirmed by developers and 13 have been fixed at the time of writing. These results demonstrate that historical bug fixes contain actionable semantic knowledge that can be systematically transferred across syntactic siblings to uncover otherwise overlooked defects.
