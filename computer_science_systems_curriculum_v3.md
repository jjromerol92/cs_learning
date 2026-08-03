---
title: "Computer Science & Systems Curriculum — Source-Grounded Edition"
version: "3.0"
updated: "2026-08-03"
official_source_grounded: true
---

# Computer Science & Systems Curriculum — Source-Grounded Edition

Version 3 replaces the vague/invented portions of Version 2.

## What changed

1. P0 is now an official-syllabus placement pack.
2. `baseline.md` exists and tells you exactly what to record.
3. Every week maps to named official source units.
4. Every required exercise is labeled `OFFICIAL`.
5. Mastery expectations are labeled `SYNTHESIZED TARGET`.
6. Agent-generated work is optional and must be labeled `SUPPLEMENTAL`.
7. Every week has its own agent-readable file and copy-ready prompt.

## Start here

1. Open [`baseline.md`](baseline.md).
2. Open [`weeks/week-01.md`](weeks/week-01.md).
3. Copy its **Groundwork for Week 01** prompt into your agent.
4. Record evidence in `baseline.md` and `progress.md`.
5. Continue to Week 2 before making phase-compression decisions.

## Important scheduling rule

“60 weeks” expresses **order and grouping**, not a deadline. An official project
such as CS61C Project 3, CS162 Project 3, MIT 6.5840 Raft, or the sharded KV lab
may require multiple calendar weeks. Do not ask an agent to shrink a real
assignment by giving you its solution.

## Phase inventory

| Phase | Weeks | Subject | Grounding rule |
|---|---:|---|---|
| P0 | Weeks 1–2 | Official-syllabus placement | Use public university assignments to locate the correct starting depth. No invented diagnostic questions. |
| P1 | Weeks 3–8 | Programming abstractions | Follow Berkeley CS 61A's actual topic and assignment sequence. |
| P2 | Weeks 9–14 | Discrete mathematics and probability | Use MIT Mathematics for CS and Berkeley CS 70 official units/problem sets. |
| P3 | Weeks 15–24 | Data structures and algorithms | Use Berkeley CS 61B and MIT 6.006 official sequence. |
| P4 | Weeks 25–32 | Machine structures and architecture | Use Berkeley CS 61C's actual Summer 2026 sequence. |
| P5 | Weeks 33–42 | Operating systems | Use Berkeley CS 162's public schedule and OSTEP's official exercises. |
| P6 | Weeks 43–48 | Database systems | Use CMU 15-445/645's Spring 2026 schedule and BusTub projects. |
| P7 | Weeks 49–54 | Networking and security | Use Stanford CS 144 checkpoints and Berkeley CS 161 topic blocks. |
| P8 | Weeks 55–60 | Distributed systems and design | Use MIT 6.5840 labs plus MIT 6.033 design-writing structure. |

## Files to use

- `source_syllabus_inventory.md` — full 60-week inventory.
- `weeks/week-XX.md` — exact source/work/mastery file for a single week.
- `baseline.md` — P0 scoring and evidence.
- `AGENT_TUTOR.md` — anti-hallucination and tutoring rules.
- `progress.md` — progress/evidence tracker.
- `computer_science_systems_curriculum_v3.json` — machine-readable manifest.

## Weekly index

| Week | Phase | Subject | Week file |
|---:|---|---|---|
| 01 | P0 | Placement A: programming, Java structures and proof | [Open Week 01](weeks/week-01.md) |
| 02 | P0 | Placement B: C, machine structures and operating-system prerequisites | [Open Week 02](weeks/week-02.md) |
| 03 | P1 | Functions, control, higher-order functions and environments | [Open Week 03](weeks/week-03.md) |
| 04 | P1 | Recursion and tree recursion | [Open Week 04](weeks/week-04.md) |
| 05 | P1 | Sequences, mutability, data abstraction and trees | [Open Week 05](weeks/week-05.md) |
| 06 | P1 | Iterators, generators, exceptions and object-oriented programming | [Open Week 06](weeks/week-06.md) |
| 07 | P1 | Linked structures, interfaces and efficiency | [Open Week 07](weeks/week-07.md) |
| 08 | P1 | Scheme, interpreters and declarative SQL | [Open Week 08](weeks/week-08.md) |
| 09 | P2 | Logic, sets, quantifiers and proof methods | [Open Week 09](weeks/week-09.md) |
| 10 | P2 | Induction, recursive definitions and state-machine invariants | [Open Week 10](weeks/week-10.md) |
| 11 | P2 | Asymptotics, recurrences and algorithmic cost | [Open Week 11](weeks/week-11.md) |
| 12 | P2 | Number theory, modular arithmetic and RSA foundations | [Open Week 12](weeks/week-12.md) |
| 13 | P2 | Graphs, partial orders, matching and counting | [Open Week 13](weeks/week-13.md) |
| 14 | P2 | Discrete probability, random variables and concentration | [Open Week 14](weeks/week-14.md) |
| 15 | P3 | Java, classes, references and testing | [Open Week 15](weeks/week-15.md) |
| 16 | P3 | Recursion, IntLists, SLLists, DLLists and array lists | [Open Week 16](weeks/week-16.md) |
| 17 | P3 | Inheritance, interfaces, iterators and polymorphism | [Open Week 17](weeks/week-17.md) |
| 18 | P3 | Asymptotics and disjoint sets | [Open Week 18](weeks/week-18.md) |
| 19 | P3 | Binary search trees, B-trees and red-black trees | [Open Week 19](weeks/week-19.md) |
| 20 | P3 | Heaps and priority queues | [Open Week 20](weeks/week-20.md) |
| 21 | P3 | Graph representations, BFS and DFS | [Open Week 21](weeks/week-21.md) |
| 22 | P3 | Shortest paths, minimum spanning trees and DAGs | [Open Week 22](weeks/week-22.md) |
| 23 | P3 | Hashing, tries and comparison-based sorting | [Open Week 23](weeks/week-23.md) |
| 24 | P3 | Dynamic programming and computational complexity | [Open Week 24](weeks/week-24.md) |
| 25 | P4 | Number representation and C foundations | [Open Week 25](weeks/week-25.md) |
| 26 | P4 | C memory management, generics, debugging and function pointers | [Open Week 26](weeks/week-26.md) |
| 27 | P4 | RISC-V instructions, registers and control flow | [Open Week 27](weeks/week-27.md) |
| 28 | P4 | Instruction formats, CALL and calling conventions | [Open Week 28](weeks/week-28.md) |
| 29 | P4 | Synchronous digital systems and CPU datapaths | [Open Week 29](weeks/week-29.md) |
| 30 | P4 | Pipelining and processor performance | [Open Week 30](weeks/week-30.md) |
| 31 | P4 | Caches and locality | [Open Week 31](weeks/week-31.md) |
| 32 | P4 | Parallelism and virtual memory | [Open Week 32](weeks/week-32.md) |
| 33 | P5 | OS abstractions, protection and system calls | [Open Week 33](weeks/week-33.md) |
| 34 | P5 | Processes, files, threads and I/O | [Open Week 34](weeks/week-34.md) |
| 35 | P5 | Synchronization: races, locks and atomicity | [Open Week 35](weeks/week-35.md) |
| 36 | P5 | Condition variables, semaphores and monitors | [Open Week 36](weeks/week-36.md) |
| 37 | P5 | Scheduling and deadlock | [Open Week 37](weeks/week-37.md) |
| 38 | P5 | Virtual memory: address spaces and paging | [Open Week 38](weeks/week-38.md) |
| 39 | P5 | Virtual memory: replacement, faults and memory homework | [Open Week 39](weeks/week-39.md) |
| 40 | P5 | General I/O, caches and file systems | [Open Week 40](weeks/week-40.md) |
| 41 | P5 | Crash consistency, reliability and distributed OS services | [Open Week 41](weeks/week-41.md) |
| 42 | P5 | OS synthesis and official cumulative assessment | [Open Week 42](weeks/week-42.md) |
| 43 | P6 | Relational model, SQL and database overview | [Open Week 43](weeks/week-43.md) |
| 44 | P6 | Storage managers and buffer pools | [Open Week 44](weeks/week-44.md) |
| 45 | P6 | Hash tables, indexes, filters and index concurrency | [Open Week 45](weeks/week-45.md) |
| 46 | P6 | Sorting, joins and query execution | [Open Week 46](weeks/week-46.md) |
| 47 | P6 | Query planning, transactions and concurrency control | [Open Week 47](weeks/week-47.md) |
| 48 | P6 | Logging, recovery and distributed databases | [Open Week 48](weeks/week-48.md) |
| 49 | P7 | Internet datagrams and byte streams | [Open Week 49](weeks/week-49.md) |
| 50 | P7 | TCP receiver and sender | [Open Week 50](weeks/week-50.md) |
| 51 | P7 | Measurement, network interfaces and IP routing | [Open Week 51](weeks/week-51.md) |
| 52 | P7 | Security principles, x86 review and memory safety | [Open Week 52](weeks/week-52.md) |
| 53 | P7 | Cryptographic building blocks and secure channels | [Open Week 53](weeks/week-53.md) |
| 54 | P7 | Web, authentication and network security | [Open Week 54](weeks/week-54.md) |
| 55 | P8 | MapReduce, RPC, Go and partial failure | [Open Week 55](weeks/week-55.md) |
| 56 | P8 | Reliable RPC and a linearizable key/value service | [Open Week 56](weeks/week-56.md) |
| 57 | P8 | Consensus and Raft | [Open Week 57](weeks/week-57.md) |
| 58 | P8 | Replicated state machines and fault-tolerant key/value storage | [Open Week 58](weeks/week-58.md) |
| 59 | P8 | Sharding, distributed transactions and cache consistency | [Open Week 59](weeks/week-59.md) |
| 60 | P8 | System-design report, review and cumulative defense | [Open Week 60](weeks/week-60.md) |