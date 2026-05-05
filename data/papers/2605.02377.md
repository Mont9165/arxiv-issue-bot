# Unfair by design: eBPF-based scheduling of mixed database workloads

- arXiv ID: `2605.02377v1`
- Authors: Carl-Elliott Bilodeau-Savaria, Jan Kristof Nidzwetzki, Stefanie Scherzinger, Bettina Kemme
- Published: 2026-05-04
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.02377v1) | [pdf](https://arxiv.org/pdf/2605.02377v1)

## Abstract

Modern database systems increasingly co-schedule time-sensitive and background tasks. In such mixed workloads, background tasks should ideally utilize only spare CPU capacity without interfering with latency-critical requests. While some database-level solutions address this challenge, many database systems still rely on operating system (OS) schedulers, which, despite supporting priorities, do not reliably isolate high-priority tasks. Furthermore, they remain vulnerable to priority inversion, where preempted background tasks can delay other work. We present UFS, a selectively unfair scheduler implemented as an eBPF-based sched_ext scheduler in the Linux kernel. UFS restricts background tasks to idle CPU capacity and preempts them immediately when time-sensitive tasks arrive. To address priority inversion, UFS incorporates application-level hints via eBPF maps, ensuring that background tasks are not unnecessarily delayed should time-sensitive tasks wait for them to release locks. Our integration of UFS into PostgreSQL demonstrates that, under mixed workloads, UFS improves throughput for time-sensitive tasks by up to 2X, while reducing tail latency by half, compared to existing scheduling options in Linux.
