---
week: 58
phase: P8
title: "Replicated state machines and fault-tolerant key/value storage"
official_source_grounded: true
---

# Week 58 — Replicated state machines and fault-tolerant key/value storage

## Place in the curriculum

- **Phase:** P8 — Distributed systems and design
- **Phase purpose:** Use MIT 6.5840 labs plus MIT 6.033 design-writing structure.
- **Prerequisite check:** Working Raft implementation and database state-machine concepts.

## Exact official source map

- **MIT65840 — [MIT 6.5840 — Distributed Systems](https://pdos.csail.mit.edu/6.5840/) (Spring 2026):** Lab 4 Fault-tolerant Key/Value Service; ZooKeeper, chain replication and transaction-related case studies.

## Official source work

These are the only required exercises for this week.

- **OFFICIAL · Core · Programming lab:** [MIT 6.5840 Lab 4: Fault-tolerant Key/Value Service](https://pdos.csail.mit.edu/6.5840/labs/lab-kvraft1.html) — Public specification/material.
- **OFFICIAL · Core · Reading questions:** [Official reading questions for ZooKeeper/replication case studies](https://pdos.csail.mit.edu/6.5840/) — Public specification/material.

## Official stretch work

- None designated.

## What you should know afterward

The following are **synthesized mastery targets** derived from the official
topics. They are not quotations or invented university assignments.

- SYNTHESIZED TARGET: connect client deduplication, Raft log entries and state-machine application.
- SYNTHESIZED TARGET: explain snapshot/restart interaction with replicated state.
- SYNTHESIZED TARGET: reason about visible behavior during leader change and network partition.

## Access and integrity notes

- No special access note beyond the source catalog.

## Evidence to record

- Record which official item and question/section you attempted.
- Record elapsed time, hints used, and whether solutions were consulted.
- Save your own work or notes; link the local path in progress.md.
- After checking official solutions where available, write the corrected reasoning—not only the final answer.
- Explain at least two representative concepts without notes to the tutor.

## What the agent may generate

By default: **nothing additional**.

After your attempt, the agent may create a short analogous example or retrieval
quiz, but it must label it `SUPPLEMENTAL — agent-generated`. It may not present
that material as part of the source university's syllabus.

## Copy-ready agent prompt

```text
Let's do the groundwork for Week 58.

Read:
1. weeks/week-58.md
2. source_syllabus_inventory.md
3. baseline.md and progress.md
4. AGENT_TUTOR.md

Rules:
- Treat only items under "Official source work" as university coursework.
- Verify the official source link and unit title before teaching.
- Do not invent, rename, or silently replace an official assignment.
- Do not reveal an official solution or search for student solution repositories.
- Begin by explaining the source unit's place in the original course and its prerequisites.
- Then ask me 5 short diagnostic questions based only on the listed source topics.
- Help me plan the official work, one item at a time.
- Require my attempt before hints; use the hint ladder in AGENT_TUTOR.md.
- When reviewing, distinguish official requirements from your own optional reinforcement.
- Update progress only from evidence I provide.

Start with the source map and prerequisite check for Week 58: Replicated state machines and fault-tolerant key/value storage.
```
