# Themis: A Filesystem Model Checker That Owns the Machine

- arXiv ID: `2608.01135v1`
- Authors: Daeyeon Son
- Published: 2026-08-02
- Primary category: `cs.OS`
- Categories: `cs.OS`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.01135v1) | [pdf](https://arxiv.org/pdf/2608.01135v1)

## Abstract

Filesystem model checkers explore an unmodified in-kernel filesystem's state space to find bugs that escape unit tests. The state of the art, Metis, runs inside the OS: it drives syscalls, and, lacking a cheap way to snapshot in-kernel state from user space, it hand-codes a reference filesystem (RefFS) as its differential oracle and sets time aside as noise. Where a checker sits shapes what it can see.
  I present Themis, a filesystem model checker built beneath an unmodified in-kernel filesystem on a bare-metal Type-1 AMD-V hypervisor. Themis owns the machine: the virtual block device and the virtual clock under a stock Linux/ext2 guest. Ownership buys four things. (1) A machine-layer epsilon-copy fork whose restore cost is proportional to dirtied pages, not filesystem image size, so every unmodified filesystem becomes its own differential reference and no hand-coded reference is required. (2) Below-filesystem observation and byte-level whole-disk diffs with nuisance-field normalization. (3) Control of the clock, turning time into an explored search dimension. (4) The same fork, made re-armable, doubling as a checkpoint for bit-exact deterministic replay.
  Over a campaign of 40+ hardware runs on an AMD Zen5 9800X3D, the mechanism is proven end-to-end: a real ext2 write is served inside a fork window and fully reverted (DRAM, disk, and device state) in 9 microseconds for the dirtied set. The principal result is the clock: Themis drives real ext2 across a clock sweep and witnesses a real Y2038 defect, a 128-byte-inode clamp that a time-excluded fingerprint cannot register. A real ext2 workload replays whole-DRAM and whole-disk bit-exact across nine passes, and a timing-flaky outcome (nine distinct hashes raw) becomes reproducible when the clock is served (nine identical).
