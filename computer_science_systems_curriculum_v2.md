---
title: "Computer Science, Computer Systems & System Design — 60-Week Guided Curriculum"
version: "2.0"
updated: "2026-08-03"
expected_hours_per_week: "8-10"
primary_profile: "Cybersecurity/threat-intelligence engineer with practical Python, Airflow, Kafka, MongoDB, Linux and networking experience"
required_resources_policy: "All required resources are freely accessible without paid enrollment"
agent_readable: true
---

# Computer Science, Computer Systems & System Design — 60-Week Guided Curriculum

**Version 2.0 — merged curriculum**

This plan merges the earlier 40-week systems-design curriculum with the common undergraduate computer-science core found at Berkeley, Caltech, MIT, Stanford and Carnegie Mellon. It is **not** an attempt to repeat a complete four-year degree. It deliberately omits general-education requirements and does not force an electronics engineer to redo calculus, physics or linear algebra unless the baseline diagnostic exposes a real gap.

The required path uses only free/open course sites, textbooks, documentation, assignments and papers. Paid books may be useful, but none is required to complete the curriculum.

## Why the plan changed

The former plan moved into Berkeley CS 162 after a short four-week prerequisite block. Berkeley's own course prerequisites assume mature data structures, C, assembly, caches, virtual memory, probability, debugging and computational problem solving. This version therefore adds substantial work in programming abstraction, proof, algorithms, data structures and machine structures before operating systems.

## Target outcome

At completion you should be able to take an ambiguous systems problem and produce:

1. a precise behavioral specification;
2. explicit constraints, state and invariants;
3. a decomposition into testable component contracts;
4. justified data structures and algorithms;
5. an architecture with clear consistency, security and failure guarantees;
6. a working vertical slice;
7. experiments supporting performance and reliability claims;
8. an oral defense that explains trade-offs and limitations without bluffing.

## Weekly cadence

| Activity | Time |
|---|---:|
| Lectures/readings and structured notes | 2 h |
| Hand-worked reasoning/proofs/traces | 2 h |
| Programming laboratory | 3–4 h |
| Tests, review and retrospective | 1 h |
| AI-tutor quiz and spaced repetition | 1 h |

A week is complete only when the deliverable exists and every success criterion is supported by evidence.

## Non-negotiable problem-solving protocol

Before substantial code, create a `DESIGN.md` containing:

```markdown
# Problem
## Restatement
## Observable behavior
## Inputs and outputs
## Constraints and scale
## Examples and counterexamples
## Invalid inputs
## State representation and ownership
## Invariants
## State transitions
## Component contracts
## Candidate approaches
## Complexity and resource model
## Failure cases
## Security considerations
## Test plan
## Decision and rejected alternatives
```

## Advancement rubric

Score each category from 0 to 2:

- specification;
- decomposition;
- correctness;
- testing;
- algorithmic/systems reasoning;
- explanation.

**Pass:** 10/12 and no category scored 0. Do not advance through a phase gate merely because the calendar says so.


## University curriculum mapping

| University | Contribution to this plan | Official source |
|---|---|---|
| UC Berkeley | CS/EECS lower division requires CS 61A, 61B, 61C and CS 70; the plan uses these as the primary foundation. | [Official curriculum](https://eecs.berkeley.edu/resources/undergrads/cs/degree-reqs-lowerdiv/) |
| Caltech | CS fundamentals, mathematical/theoretical intermediate courses and a multi-quarter project sequence motivate the proof and capstone gates. | [Official curriculum](https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/computer-science-option-and-minor-cs/) |
| MIT | Programming, systems and algorithmic thinking are combined with system-design subjects; MIT OCW supplies the mathematics, algorithms and design spine. | [Official curriculum](https://catalog.mit.edu/schools/engineering/electrical-engineering-computer-science/) |
| Stanford | Programming abstractions, mathematical foundations, computer organization and probability influence the core; CS 144 supplies an open networking laboratory. | [Official curriculum](https://www.cs.stanford.edu/bachelors/cs-minor) |
| Carnegie Mellon | Imperative and functional programming, data structures/algorithms, systems, theory and project rigor shape the sequencing and assessment style. | [Official curriculum](https://csd.cmu.edu/sites/default/files/2024-04/CS_Sample_Curriculum_Schedule.pdf) |

## Phase map

| Phase | Weeks | Focus | Main influence | Gate outcome |
|---|---:|---|---|---|
| P0 | 1–2 | Baseline, decomposition and learning system | Caltech project discipline + MIT 6.033 design writing | Evidence-based starting level |
| P1 | 3–8 | Programming abstractions and software construction | Berkeley CS 61A + CMU imperative/functional foundations | Programming abstraction project |
| P2 | 9–14 | Discrete mathematics, probability and proof | Berkeley CS 70 + MIT Mathematics for Computer Science + Caltech CS 18/21 | Proof/probability assessment |
| P3 | 15–24 | Data structures and algorithms | Berkeley CS 61B + MIT 6.006 + CMU 15-210/15-451 | Algorithms and data-structures project |
| P4 | 25–32 | Machine structures and computer architecture | Berkeley CS 61C + Stanford CS 107 + Caltech CS 24 | Machine-structures gate |
| P5 | 33–42 | Operating systems and systems programming | Berkeley CS 162 + OSTEP | Networked systems daemon |
| P6 | 43–48 | Database systems | CMU 15-445/645 | Recoverable mini storage engine |
| P7 | 49–54 | Networking and security | Stanford CS 144 + Berkeley CS 161 | Secure telemetry collector |
| P8 | 55–60 | Distributed systems, system design and capstone | MIT 6.5840 + MIT 6.033 + Google SRE | Portfolio capstone and oral defense |

## Compression rules for your existing experience

- **Never skip Weeks 1–2.** They decide what may be compressed.
- A phase may be compressed to its gate project only when the diagnostic and oral explanation both score at least 85%.
- Familiarity with Python frameworks does not automatically waive recursion, proof, data-structure or machine-level work.
- Your electronics background may justify skipping separate calculus/physics refreshers, but not discrete mathematics, probability or computer architecture.
- Security topics are retained even when familiar because the goal is to integrate them into system design, not merely recognize terminology.

## Repository layout

```text
systems-learning/
├── README.md
├── curriculum.md
├── curriculum.json
├── AGENT_TUTOR.md
├── progress.md
├── problem-solving-journal/
├── notes/
│   └── phase-PX/
├── labs/
│   └── week-XX/
│       ├── DESIGN.md
│       ├── README.md
│       ├── src/
│       ├── tests/
│       └── RETROSPECTIVE.md
├── architecture/
│   ├── diagrams/
│   ├── adrs/
│   └── capstone/
└── quizzes/
```


# P0 — Baseline, decomposition and learning system (Weeks 1–2)

**Influence:** Caltech project discipline + MIT 6.033 design writing  
**Goal:** Establish evidence-based starting level, repository structure, debugging habits and a mandatory decomposition protocol.


## Week 01 — Baseline diagnostic and curriculum setup

**Programming language:** Python, C, Java and technical writing


### Knowledge points
- Distinguish familiarity from demonstrated competence.
- Establish baseline in programming, data structures, proofs, C, Linux and architecture.
- Create a reproducible learning repository and progress record.

### Problem-decomposition focus
For each diagnostic problem, write inputs, outputs, constraints, examples, edge cases, state and test oracles before coding.

### Required work
- Complete a 90-minute mixed diagnostic: one Python transformation, one linked-structure problem, one proof, one C memory trace and one systems-design prompt.
- Create the repository layout from this curriculum.
- Record confidence before each answer and compare confidence with results.

### Deliverable
**baseline.md with scores, misconceptions, evidence and a personalized no-skip/compress decision for every phase.**

### Success criteria
- [ ] Every score has linked evidence.
- [ ] At least three false-confidence areas are identified.
- [ ] No phase is skipped solely because the topic feels familiar.

### Free resources
- [R15 — MIT 6.033 Computer System Engineering — Spring 2018](https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/) — Free notes, critiques, design project and examples.
- [R30 — Google Engineering Practices](https://google.github.io/eng-practices/) — Free.

## Week 02 — Problem specification, decomposition and testing

**Programming language:** Python + pseudocode


### Knowledge points
- Observable behavior versus implementation choice.
- Contracts, invariants, state transitions and failure surfaces.
- Test design from requirements rather than code branches.

### Problem-decomposition focus
Use the fixed ladder: restate → examples → constraints → state → invariants → interfaces → failures → tests → complexity.

### Required work
- Specify an IOC normalizer, a rate limiter and a duplicate-event suppressor without coding first.
- Produce two different decompositions for one problem and compare coupling.
- Implement only after the design is reviewed by the tutor.

### Deliverable
**Three DESIGN.md files plus a small tested implementation of the duplicate-event suppressor.**

### Success criteria
- [ ] Every requirement maps to a test.
- [ ] Components can be tested independently.
- [ ] Rejected alternatives are documented with reasons.

### Free resources
- [R15 — MIT 6.033 Computer System Engineering — Spring 2018](https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/) — Free notes, critiques, design project and examples.
- [R30 — Google Engineering Practices](https://google.github.io/eng-practices/) — Free.

# P1 — Programming abstractions and software construction (Weeks 3–8)

**Influence:** Berkeley CS 61A + CMU imperative/functional foundations  
**Goal:** Move beyond framework-driven coding into recursion, abstraction, multiple paradigms, interpreters, testing and clear module contracts.


## Week 03 — Expressions, functions and environment models

**Programming language:** Python


### Knowledge points
- Evaluation order and environments.
- Pure functions, side effects and referential transparency.
- Function composition and local reasoning.

### Problem-decomposition focus
Represent a program as transformations with explicit inputs and outputs before introducing shared state.

### Required work
- Follow CS 61A opening lectures/readings.
- Trace ten expression evaluations by hand.
- Refactor a monolithic enrichment script into composable functions.

### Deliverable
**A pure-function IOC normalization pipeline with unit tests and evaluation traces.**

### Success criteria
- [ ] Can explain every binding and return value.
- [ ] Core transformations have no hidden I/O.
- [ ] Tests include malformed and adversarial inputs.

### Free resources
- [R01 — UC Berkeley CS 61A — Spring 2026](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) — Open lectures, notes, labs, homework and project specifications.
- [R02 — Composing Programs](https://www.composingprograms.com/) — Free online textbook.

## Week 04 — Recursion and recursive problem decomposition

**Programming language:** Python


### Knowledge points
- Recursive definitions, base cases and progress measures.
- Tree recursion and search spaces.
- Relationship between recursion and induction.

### Problem-decomposition focus
For each recursive function state: smaller subproblem, base case, combination step and termination measure.

### Required work
- Solve recursive sequence, tree and partition problems.
- Draw call trees before running code.
- Rewrite one recursive solution iteratively and compare invariants.

### Deliverable
**Recursive domain-tree analyzer for subdomains or URL paths.**

### Success criteria
- [ ] No recursion without a stated termination argument.
- [ ] Can estimate call-tree growth.
- [ ] Can explain when recursion clarifies or obscures the solution.

### Free resources
- [R01 — UC Berkeley CS 61A — Spring 2026](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) — Open lectures, notes, labs, homework and project specifications.
- [R02 — Composing Programs](https://www.composingprograms.com/) — Free online textbook.
- [R04 — MIT 6.1200J Mathematics for Computer Science — Spring 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) — Free lectures, text, problem sets and downloadable course package.

## Week 05 — Higher-order functions and abstraction barriers

**Programming language:** Python


### Knowledge points
- Functions as values, closures and decorators.
- Separation of policy from mechanism.
- Abstraction barriers and representation independence.

### Problem-decomposition focus
Identify the varying policy and pass it through an interface instead of duplicating control flow.

### Required work
- Build reusable map/filter/fold-style transformations.
- Implement configurable scoring and filtering policies for indicators.
- Create property-based-style test cases without requiring a library.

### Deliverable
**Policy-driven IOC scoring pipeline with interchangeable scoring functions.**

### Success criteria
- [ ] Adding a policy does not modify the engine.
- [ ] Representation details do not leak into callers.
- [ ] Can explain closure-captured state precisely.

### Free resources
- [R01 — UC Berkeley CS 61A — Spring 2026](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) — Open lectures, notes, labs, homework and project specifications.
- [R02 — Composing Programs](https://www.composingprograms.com/) — Free online textbook.

## Week 06 — Data abstraction, objects and mutation

**Programming language:** Python


### Knowledge points
- Abstract data types and representation invariants.
- Mutation, aliasing and defensive copying.
- Object composition versus inheritance.

### Problem-decomposition focus
State who owns mutable data, who may mutate it and what invariant each method preserves.

### Required work
- Implement a bounded cache as an ADT.
- Create aliasing bugs deliberately and diagnose them.
- Compare functional and mutable designs for an enrichment cache.

### Deliverable
**Thread-unsafe bounded cache with rigorous sequential invariants and tests; concurrency comes later.**

### Success criteria
- [ ] Representation invariant is checked in tests.
- [ ] Public API does not expose mutable internals.
- [ ] Can identify all aliases to mutable state.

### Free resources
- [R01 — UC Berkeley CS 61A — Spring 2026](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) — Open lectures, notes, labs, homework and project specifications.
- [R02 — Composing Programs](https://www.composingprograms.com/) — Free online textbook.
- [R30 — Google Engineering Practices](https://google.github.io/eng-practices/) — Free.

## Week 07 — Functional programming, Scheme and interpreters

**Programming language:** Scheme + Python


### Knowledge points
- Symbolic expressions, lexical scope and evaluation.
- Functional recursion over lists and trees.
- Interpreter loop: parse, evaluate and apply.

### Problem-decomposition focus
Separate syntax representation, environment, evaluation rules and primitive operations.

### Required work
- Complete selected CS 61A Scheme exercises.
- Trace lexical versus dynamic scope examples.
- Implement a tiny expression evaluator in Python.

### Deliverable
**Mini interpreter supporting numbers, names, arithmetic, definitions and conditionals.**

### Success criteria
- [ ] Can trace environment frames by hand.
- [ ] Parser and evaluator are independently tested.
- [ ] Errors are represented deliberately rather than as accidental crashes.

### Free resources
- [R01 — UC Berkeley CS 61A — Spring 2026](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) — Open lectures, notes, labs, homework and project specifications.
- [R02 — Composing Programs](https://www.composingprograms.com/) — Free online textbook.
- [R28 — Crafting Interpreters](https://craftinginterpreters.com/) — Free online.

## Week 08 — Declarative programming, SQL and phase project

**Programming language:** SQL + Python


### Knowledge points
- Declarative versus imperative specification.
- Relational transformations and compositional queries.
- Module boundaries, test doubles and integration tests.

### Problem-decomposition focus
Describe desired result before execution strategy; isolate persistence from domain logic.

### Required work
- Complete selected CS 61A SQL work.
- Build a small SQLite-backed indicator catalog.
- Run an oral review covering recursion, abstraction, mutation and interpreter design.

### Deliverable
**Phase project: local IOC catalog with import, normalization, scoring, querying and a written architecture.**

### Success criteria
- [ ] All external I/O is behind interfaces.
- [ ] Database schema reflects explicit invariants.
- [ ] Tutor score is at least 10/12 with no zero category.

### Free resources
- [R01 — UC Berkeley CS 61A — Spring 2026](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) — Open lectures, notes, labs, homework and project specifications.
- [R02 — Composing Programs](https://www.composingprograms.com/) — Free online textbook.
- [R17 — SQLite Documentation](https://www.sqlite.org/docs.html) — Free.

# P2 — Discrete mathematics, probability and proof (Weeks 9–14)

**Influence:** Berkeley CS 70 + MIT Mathematics for Computer Science + Caltech CS 18/21  
**Goal:** Develop the ability to prove correctness, reason with invariants, quantify uncertainty and analyze recursive structures.


## Week 09 — Logic, sets and proof structure

**Programming language:** Mathematical writing + Python checks


### Knowledge points
- Propositions, quantifiers, implication and equivalence.
- Sets, functions, relations and counterexamples.
- Direct proof, contradiction and contrapositive.

### Problem-decomposition focus
Translate informal claims into quantified statements before attempting a proof.

### Required work
- Work MIT MCS/CS 70 logic and set exercises.
- Find counterexamples to five plausible but false engineering claims.
- Encode small finite checks in Python without treating experiments as proofs.

### Deliverable
**proof-journal-01.md with eight complete proofs and counterexamples.**

### Success criteria
- [ ] Quantifiers are explicit.
- [ ] Proof steps cite definitions or prior facts.
- [ ] Can explain why testing many cases is not a general proof.

### Free resources
- [R04 — MIT 6.1200J Mathematics for Computer Science — Spring 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) — Free lectures, text, problem sets and downloadable course package.
- [R05 — UC Berkeley CS 70 — Summer 2026](https://www.eecs70.org/) — Open notes, discussion worksheets and homework.

## Week 10 — Induction, recursion and invariants

**Programming language:** Mathematical writing + Python


### Knowledge points
- Weak and strong induction.
- Structural induction over recursive data.
- Loop invariants, initialization, maintenance and termination.

### Problem-decomposition focus
Choose an induction parameter or invariant that matches the program's state transition.

### Required work
- Prove correctness of binary search and one recursive tree function.
- Derive an invariant for a streaming deduplicator.
- Find the smallest counterexample to a broken invariant.

### Deliverable
**Correctness note for two programs, including termination and complexity.**

### Success criteria
- [ ] Invariant is true initially and preserved.
- [ ] Termination is argued separately from partial correctness.
- [ ] Can connect recursive code to an inductive proof.

### Free resources
- [R04 — MIT 6.1200J Mathematics for Computer Science — Spring 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) — Free lectures, text, problem sets and downloadable course package.
- [R05 — UC Berkeley CS 70 — Summer 2026](https://www.eecs70.org/) — Open notes, discussion worksheets and homework.
- [R06 — MIT 6.006 Introduction to Algorithms — Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Free lecture videos, notes, recitations, assignments and exams.

## Week 11 — Graphs, relations and state machines

**Programming language:** Mathematical writing + Python


### Knowledge points
- Directed and undirected graphs, paths, connectivity and trees.
- Equivalence relations and partial orders.
- Finite-state machines and reachability.

### Problem-decomposition focus
Model entities, transitions and forbidden states before choosing an algorithm.

### Required work
- Model an IOC lifecycle as a state machine.
- Prove two unreachable states under the proposed transition rules.
- Solve graph-theory exercises from MIT MCS/CS 70.

### Deliverable
**State-machine specification with diagram, transition table, invariants and executable validator.**

### Success criteria
- [ ] All transitions name preconditions and effects.
- [ ] Illegal transitions are rejected.
- [ ] Can distinguish graph model from traversal algorithm.

### Free resources
- [R04 — MIT 6.1200J Mathematics for Computer Science — Spring 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) — Free lectures, text, problem sets and downloadable course package.
- [R05 — UC Berkeley CS 70 — Summer 2026](https://www.eecs70.org/) — Open notes, discussion worksheets and homework.

## Week 12 — Number theory and cryptographic reasoning

**Programming language:** Mathematical writing + Python


### Knowledge points
- Modular arithmetic, gcd and inverses.
- Fast exponentiation and basic public-key structure.
- Difference between mathematical primitive and secure protocol.

### Problem-decomposition focus
Separate algebraic correctness, computational cost and security assumptions.

### Required work
- Implement Euclid and modular exponentiation.
- Work modular-arithmetic proofs.
- Explain why textbook RSA-like arithmetic alone is not a complete secure system.

### Deliverable
**Number-theory notebook plus a security-assumptions memo.**

### Success criteria
- [ ] Can compute and justify modular inverses.
- [ ] Fast exponentiation complexity is derived.
- [ ] No claim confuses correctness with security.

### Free resources
- [R04 — MIT 6.1200J Mathematics for Computer Science — Spring 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) — Free lectures, text, problem sets and downloadable course package.
- [R05 — UC Berkeley CS 70 — Summer 2026](https://www.eecs70.org/) — Open notes, discussion worksheets and homework.
- [R21 — Berkeley CS 161 Computer Security Textbook](https://textbook.cs161.org/) — Free HTML and PDF.

## Week 13 — Counting and discrete probability

**Programming language:** Mathematical writing + Python simulation


### Knowledge points
- Product/sum rules, permutations and combinations.
- Conditional probability, independence and Bayes' rule.
- Sample spaces and event modeling.

### Problem-decomposition focus
Define the experiment and sample space before applying formulas.

### Required work
- Solve counting and conditional-probability problems.
- Analyze false-positive rates for a multi-provider IOC workflow.
- Use simulation only to validate, not replace, an analytic result.

### Deliverable
**Probability analysis of a threat-intelligence alert pipeline.**

### Success criteria
- [ ] Events and conditioning are explicit.
- [ ] Independence is justified, not assumed.
- [ ] Simulation converges near the analytic result.

### Free resources
- [R04 — MIT 6.1200J Mathematics for Computer Science — Spring 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) — Free lectures, text, problem sets and downloadable course package.
- [R05 — UC Berkeley CS 70 — Summer 2026](https://www.eecs70.org/) — Open notes, discussion worksheets and homework.

## Week 14 — Random variables, expectation, recurrences and asymptotics

**Programming language:** Mathematical writing + Python


### Knowledge points
- Random variables, expectation and variance.
- Linearity of expectation.
- Recurrences, growth rates and asymptotic notation.

### Problem-decomposition focus
Choose a cost variable, derive its recurrence or expectation, then test the model empirically.

### Required work
- Analyze hashing and retry costs.
- Solve recurrences by expansion/substitution.
- Complete a closed-book phase assessment.

### Deliverable
**Math gate packet: proofs, probability model, recurrence analysis and corrections.**

### Success criteria
- [ ] Can derive rather than memorize common bounds.
- [ ] Can use expectation without assuming independence where unnecessary.
- [ ] Assessment reaches 80% and every error has a corrected explanation.

### Free resources
- [R04 — MIT 6.1200J Mathematics for Computer Science — Spring 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) — Free lectures, text, problem sets and downloadable course package.
- [R05 — UC Berkeley CS 70 — Summer 2026](https://www.eecs70.org/) — Open notes, discussion worksheets and homework.
- [R06 — MIT 6.006 Introduction to Algorithms — Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Free lecture videos, notes, recitations, assignments and exams.

# P3 — Data structures and algorithms (Weeks 15–24)

**Influence:** Berkeley CS 61B + MIT 6.006 + CMU 15-210/15-451  
**Goal:** Choose and implement data structures from workload requirements, prove algorithm correctness and measure rather than guess performance.


## Week 15 — Java, static types, references and testing

**Programming language:** Java


### Knowledge points
- Static typing, classes, interfaces and references.
- Unit tests, assertions and test isolation.
- Value equality versus identity.

### Problem-decomposition focus
Define the ADT and tests before selecting fields or implementation classes.

### Required work
- Complete selected CS 61B Java introduction work.
- Port the bounded cache API to Java.
- Write tests before implementation for one component.

### Deliverable
**Java project skeleton with CI, tests and style checks.**

### Success criteria
- [ ] Public interfaces contain no implementation details.
- [ ] Equality semantics are explicit.
- [ ] Tests fail for the intended reasons before code is added.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R30 — Google Engineering Practices](https://google.github.io/eng-practices/) — Free.

## Week 16 — Linked lists, deques and representation invariants

**Programming language:** Java


### Knowledge points
- Singly and doubly linked structures.
- Sentinels, boundary cases and iterator state.
- Amortized versus worst-case behavior.

### Problem-decomposition focus
Draw the representation and state every pointer invariant before implementing updates.

### Required work
- Implement linked deque from a specification.
- Test empty, singleton and mutation sequences.
- Perform code review focused on invariants and aliasing.

### Deliverable
**LinkedDeque with iterator, randomized differential tests and invariant checker.**

### Success criteria
- [ ] Every mutation preserves forward/backward links.
- [ ] No special-case explosion at boundaries.
- [ ] Iterator behavior under mutation is documented.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R27 — Open Data Structures](https://opendatastructures.org/) — Free HTML/PDF editions.

## Week 17 — Resizable arrays, generics and API design

**Programming language:** Java


### Knowledge points
- Dynamic arrays and amortized resizing.
- Generics, iterables and abstraction.
- API usability and error contracts.

### Problem-decomposition focus
Separate logical sequence behavior from storage-capacity policy.

### Required work
- Implement array deque.
- Prove amortized append cost informally with aggregate analysis.
- Compare memory locality with linked representation.

### Deliverable
**ArrayDeque and a benchmark comparing both deque implementations.**

### Success criteria
- [ ] Capacity never violates stated bounds.
- [ ] Benchmark methodology is reproducible.
- [ ] Can explain why asymptotic equality does not imply equal performance.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R27 — Open Data Structures](https://opendatastructures.org/) — Free HTML/PDF editions.

## Week 18 — Trees, search trees and balanced indexing

**Programming language:** Java


### Knowledge points
- Tree traversals and recursive structure.
- Binary-search-tree invariant.
- B-trees and balanced-tree motivation.

### Problem-decomposition focus
State ordering invariant and define each operation as a transformation preserving it.

### Required work
- Implement BST map.
- Trace worst-case degeneration.
- Work selected CS 61B tree exercises and compare BST with B-tree page behavior.

### Deliverable
**BST-based IOC map with traversal, deletion tests and shape analysis.**

### Success criteria
- [ ] Ordering invariant is tested.
- [ ] Can explain height-dependent complexity.
- [ ] Deletion cases are decomposed and verified independently.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R26 — Princeton Algorithms, 4th Edition Site](https://algs4.cs.princeton.edu/home/) — Free summaries, code and exercises.
- [R27 — Open Data Structures](https://opendatastructures.org/) — Free HTML/PDF editions.

## Week 19 — Hash tables, sets and workload-driven choices

**Programming language:** Java


### Knowledge points
- Hash functions, collisions, load factor and resizing.
- Separate chaining versus open addressing.
- Average-case assumptions and adversarial inputs.

### Problem-decomposition focus
Begin with required operations, key distribution and memory limits; then choose collision strategy.

### Required work
- Implement a hash map.
- Generate collision-heavy keys.
- Compare hash, tree and sorted-array approaches for IOC lookup.

### Deliverable
**Hash map plus workload decision record.**

### Success criteria
- [ ] Resizing preserves all entries.
- [ ] Collision tests are deliberate.
- [ ] Complexity claims list their assumptions.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R27 — Open Data Structures](https://opendatastructures.org/) — Free HTML/PDF editions.

## Week 20 — Heaps, priority queues and disjoint sets

**Programming language:** Java


### Knowledge points
- Heap invariant and priority queues.
- Union-find, path compression and union by rank/size.
- Model reduction: solving one problem through another ADT.

### Problem-decomposition focus
Identify the exact operation mix and map the domain problem to an existing abstract data type.

### Required work
- Implement binary heap.
- Use union-find for a connectivity problem.
- Build a priority-based enrichment scheduler.

### Deliverable
**Scheduler plus connectivity lab and complexity notes.**

### Success criteria
- [ ] Heap operations preserve shape and order.
- [ ] Can explain amortized union-find behavior conceptually.
- [ ] Domain mapping is documented before implementation.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R26 — Princeton Algorithms, 4th Edition Site](https://algs4.cs.princeton.edu/home/) — Free summaries, code and exercises.
- [R27 — Open Data Structures](https://opendatastructures.org/) — Free HTML/PDF editions.

## Week 21 — Sorting, selection and empirical algorithm analysis

**Programming language:** Java + Python analysis


### Knowledge points
- Insertion, merge, quick and heap sort.
- Stability, in-place behavior and lower-bound intuition.
- Experimental design for algorithm comparison.

### Problem-decomposition focus
Define data distributions, metrics and hypotheses before benchmarking.

### Required work
- Implement or instrument multiple sorting algorithms.
- Benchmark random, sorted, reverse and duplicate-heavy inputs.
- Explain discrepancies between theoretical and measured behavior.

### Deliverable
**Sorting laboratory with plots, raw data and interpretation.**

### Success criteria
- [ ] Correctness is tested separately from speed.
- [ ] Warm-up and repeated measurements are used.
- [ ] No chart is presented without workload details.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R06 — MIT 6.006 Introduction to Algorithms — Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Free lecture videos, notes, recitations, assignments and exams.
- [R26 — Princeton Algorithms, 4th Edition Site](https://algs4.cs.princeton.edu/home/) — Free summaries, code and exercises.

## Week 22 — Graph traversal, topological order and components

**Programming language:** Java or Python


### Knowledge points
- BFS, DFS and traversal invariants.
- Topological sorting and cycle detection.
- Connected and strongly connected components.

### Problem-decomposition focus
Define graph representation and the meaning of visited state before traversal.

### Required work
- Implement BFS/DFS.
- Model provider dependencies as a directed graph.
- Detect cycles and produce valid execution order when possible.

### Deliverable
**Dependency-graph analyzer with explanations for cycles.**

### Success criteria
- [ ] Traversal complexity includes representation cost.
- [ ] Cycle evidence is returned, not only a boolean.
- [ ] Can state the queue/stack invariant.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R06 — MIT 6.006 Introduction to Algorithms — Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Free lecture videos, notes, recitations, assignments and exams.
- [R26 — Princeton Algorithms, 4th Edition Site](https://algs4.cs.princeton.edu/home/) — Free summaries, code and exercises.

## Week 23 — Shortest paths and minimum spanning trees

**Programming language:** Java or Python


### Knowledge points
- Unweighted shortest path, Dijkstra and negative-weight limitations.
- Relaxation invariant.
- Minimum spanning trees and greedy-choice reasoning.

### Problem-decomposition focus
Match weight semantics and constraints to the algorithm; reject invalid choices explicitly.

### Required work
- Implement Dijkstra with a priority queue.
- Construct a counterexample for Dijkstra with negative edges.
- Solve a network-cost MST problem.

### Deliverable
**Path-analysis service with algorithm-selection ADR.**

### Success criteria
- [ ] Relaxation is explained precisely.
- [ ] Invalid input assumptions are checked.
- [ ] Can distinguish shortest-path tree from MST.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R06 — MIT 6.006 Introduction to Algorithms — Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Free lecture videos, notes, recitations, assignments and exams.
- [R26 — Princeton Algorithms, 4th Edition Site](https://algs4.cs.princeton.edu/home/) — Free summaries, code and exercises.

## Week 24 — Algorithm paradigms and phase project

**Programming language:** Java + Python


### Knowledge points
- Divide and conquer, greedy design and dynamic programming.
- Subproblem graphs, optimal substructure and memoization.
- Correctness argument as part of design.

### Problem-decomposition focus
Define state, transition, base cases and evaluation order before writing a dynamic program.

### Required work
- Solve one divide-and-conquer, one greedy and two DP problems.
- Build a content-addressed IOC history store or compact Git-like snapshot project.
- Complete oral algorithm review.

### Deliverable
**Phase project with design document, tests, benchmark and correctness explanation.**

### Success criteria
- [ ] Algorithm choice is justified against alternatives.
- [ ] Project uses at least four studied data structures appropriately.
- [ ] Tutor gate score is at least 10/12 with no zero.

### Free resources
- [R03 — UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) — Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable.
- [R06 — MIT 6.006 Introduction to Algorithms — Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Free lecture videos, notes, recitations, assignments and exams.
- [R26 — Princeton Algorithms, 4th Edition Site](https://algs4.cs.princeton.edu/home/) — Free summaries, code and exercises.
- [R27 — Open Data Structures](https://opendatastructures.org/) — Free HTML/PDF editions.

# P4 — Machine structures and computer architecture (Weeks 25–32)

**Influence:** Berkeley CS 61C + Stanford CS 107 + Caltech CS 24  
**Goal:** Understand how source code becomes machine execution, including memory, assembly, linking, caches, virtual memory and parallelism.


## Week 25 — C execution model, pointers and memory ownership

**Programming language:** C


### Knowledge points
- Compilation units, types, arrays and pointer arithmetic.
- Stack, heap, lifetime and ownership.
- Undefined behavior and sanitizer-driven debugging.

### Problem-decomposition focus
For every allocation, record owner, aliases, valid lifetime and release point.

### Required work
- Complete selected Beej/61C C work.
- Implement strings and dynamic arrays without unsafe shortcuts.
- Diagnose seeded memory bugs with GDB and sanitizers.

### Deliverable
**C utility library with ownership documentation and tests.**

### Success criteria
- [ ] No sanitizer findings.
- [ ] Can draw stack/heap state at key calls.
- [ ] No pointer operation is justified by guessing.

### Free resources
- [R07 — UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) — Open schedule, notes, slides and project specifications.
- [R08 — Berkeley CS 61C Course Notes](https://notes.cs61c.org/) — Free online notes and exercises.
- [R09 — Beej's Guide to C Programming](https://beej.us/guide/bgc/) — Free online and downloadable.
- [R10 — GNU GDB Documentation](https://sourceware.org/gdb/documentation/) — Free.

## Week 26 — Bits, integers, floating point and data representation

**Programming language:** C


### Knowledge points
- Two's complement, bit operations and overflow.
- Endianness and binary serialization.
- Floating-point representation and precision limits.

### Problem-decomposition focus
Specify bit layout, valid range and conversion rules before manipulating representations.

### Required work
- Implement bit-field utilities.
- Serialize a compact indicator record with explicit endianness.
- Investigate integer and floating-point edge cases.

### Deliverable
**Portable binary record format with encoder, decoder and golden tests.**

### Success criteria
- [ ] Round trips preserve valid values.
- [ ] Malformed encodings are rejected.
- [ ] Can explain signed overflow and floating-point comparison hazards.

### Free resources
- [R07 — UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) — Open schedule, notes, slides and project specifications.
- [R08 — Berkeley CS 61C Course Notes](https://notes.cs61c.org/) — Free online notes and exercises.

## Week 27 — RISC-V assembly and calling conventions

**Programming language:** RISC-V assembly + C


### Knowledge points
- Registers, instructions and control flow.
- Stack frames, calling convention and recursion.
- Mapping C constructs to assembly.

### Problem-decomposition focus
Track live values, register ownership and stack-frame layout at every call boundary.

### Required work
- Translate small C functions to RISC-V.
- Trace recursive assembly by hand.
- Inspect compiler-generated assembly at different optimization levels.

### Deliverable
**Annotated assembly notebook and two hand-written functions.**

### Success criteria
- [ ] Calling convention is respected.
- [ ] Can recover high-level control flow from assembly.
- [ ] Can explain compiler optimizations observed.

### Free resources
- [R07 — UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) — Open schedule, notes, slides and project specifications.
- [R08 — Berkeley CS 61C Course Notes](https://notes.cs61c.org/) — Free online notes and exercises.

## Week 28 — Compilation, linking, object files and loaders

**Programming language:** C + shell


### Knowledge points
- Preprocessing, compilation, assembly and linking.
- Symbols, relocations, static and dynamic libraries.
- Executable loading and address-space setup.

### Problem-decomposition focus
Treat build output as a graph of artifacts and symbol dependencies.

### Required work
- Create multi-file static and shared-library builds.
- Inspect symbols and sections with binutils.
- Trigger and diagnose compile-time, link-time and load-time failures.

### Deliverable
**Build-and-link laboratory with diagrams and failure catalog.**

### Success criteria
- [ ] Can distinguish declaration, definition and symbol visibility.
- [ ] Can explain relocation at a conceptual level.
- [ ] Build is reproducible from one command.

### Free resources
- [R07 — UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) — Open schedule, notes, slides and project specifications.
- [R08 — Berkeley CS 61C Course Notes](https://notes.cs61c.org/) — Free online notes and exercises.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 29 — Digital logic, datapaths and instruction execution

**Programming language:** Logic diagrams + optional HDL


### Knowledge points
- Boolean logic, combinational and sequential elements.
- Datapath, control and instruction cycle.
- Abstraction from transistor to ISA.

### Problem-decomposition focus
Split behavior into state elements, combinational transformations and control signals.

### Required work
- Work selected 61C datapath exercises.
- Trace instructions through a simple CPU.
- Optionally complete Nand2Tetris logic/CPU projects.

### Deliverable
**Single-cycle CPU explanation with annotated datapath.**

### Success criteria
- [ ] Can identify all state changes for an instruction.
- [ ] Control signals are derived from semantics.
- [ ] Can explain what the ISA hides from software.

### Free resources
- [R07 — UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) — Open schedule, notes, slides and project specifications.
- [R08 — Berkeley CS 61C Course Notes](https://notes.cs61c.org/) — Free online notes and exercises.
- [R29 — Nand2Tetris](https://www.nand2tetris.org/) — Free software, lectures and project materials.

## Week 30 — Pipelining and performance reasoning

**Programming language:** C + diagrams


### Knowledge points
- Pipeline stages, hazards, forwarding and stalls.
- Latency versus throughput.
- Amdahl's law and measurement discipline.

### Problem-decomposition focus
Identify the critical path, parallel stages and dependency hazards before proposing optimization.

### Required work
- Trace pipeline schedules.
- Calculate speedup limits.
- Optimize a small C workload and measure before/after.

### Deliverable
**Performance report with hypothesis, profile, change and evidence.**

### Success criteria
- [ ] Optimization targets measured bottleneck.
- [ ] Pipeline hazards are identified correctly.
- [ ] No speedup claim omits baseline and workload.

### Free resources
- [R07 — UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) — Open schedule, notes, slides and project specifications.
- [R08 — Berkeley CS 61C Course Notes](https://notes.cs61c.org/) — Free online notes and exercises.

## Week 31 — Caches, locality and memory hierarchy

**Programming language:** C + Python analysis


### Knowledge points
- Cache lines, mapping, associativity and replacement.
- Spatial/temporal locality.
- Cache-aware data layout and traversal.

### Problem-decomposition focus
Model access pattern first; then predict hits, misses and bandwidth needs.

### Required work
- Solve cache-address exercises.
- Benchmark row/column traversal and structure layouts.
- Use a profiler to connect code to cache behavior.

### Deliverable
**Cache-locality laboratory using an IOC parsing workload.**

### Success criteria
- [ ] Can calculate set/tag/offset.
- [ ] Measured behavior matches or corrects prediction.
- [ ] Optimization preserves readability or documents the trade-off.

### Free resources
- [R07 — UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) — Open schedule, notes, slides and project specifications.
- [R08 — Berkeley CS 61C Course Notes](https://notes.cs61c.org/) — Free online notes and exercises.

## Week 32 — Virtual memory, parallelism and architecture gate

**Programming language:** C


### Knowledge points
- Address translation, page tables and TLBs.
- Processes, protection and memory mapping.
- SIMD/multicore concepts and false sharing.

### Problem-decomposition focus
Trace virtual address → translation → permission → physical access; identify shared cache lines in parallel designs.

### Required work
- Inspect process mappings and page faults.
- Use mmap for a file-backed dataset.
- Run a small false-sharing experiment and complete phase assessment.

### Deliverable
**Machine-structures gate packet and cache-aware binary IOC reader.**

### Success criteria
- [ ] Can explain translation and protection without hand-waving.
- [ ] Reader handles malformed files safely.
- [ ] Gate score is at least 10/12 with no zero.

### Free resources
- [R07 — UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) — Open schedule, notes, slides and project specifications.
- [R08 — Berkeley CS 61C Course Notes](https://notes.cs61c.org/) — Free online notes and exercises.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

# P5 — Operating systems and systems programming (Weeks 33–42)

**Influence:** Berkeley CS 162 + OSTEP  
**Goal:** Reason about processes, concurrency, virtual memory, persistence, I/O and failure at the operating-system boundary.


## Week 33 — Operating-system roles, abstractions and system calls

**Programming language:** C + shell


### Knowledge points
- OS as resource manager, isolation boundary and service provider.
- User/kernel mode, traps and system calls.
- Processes, threads, files and sockets as abstractions.

### Problem-decomposition focus
For each abstraction name hidden mechanism, exposed contract, policy decisions and failure modes.

### Required work
- Watch opening CS 162 lectures.
- Trace selected programs with strace.
- Map one Python operation to library and system calls.

### Deliverable
**os-abstractions.md grounded in the learner's Linux/Proxmox environment.**

### Success criteria
- [ ] Can distinguish library call from syscall.
- [ ] Can explain protection boundary.
- [ ] Every abstraction includes failure examples.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R12 — UC Berkeley CS 162 — Official Course Description](https://www2.eecs.berkeley.edu/Courses/CS162/) — Free.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 34 — Processes, fork, exec, wait and signals

**Programming language:** C


### Knowledge points
- Process lifecycle and address-space inheritance.
- fork/exec/wait semantics.
- Signals, zombies and orphans.

### Problem-decomposition focus
Model process creation as state transitions and track inherited resources explicitly.

### Required work
- Implement fork/exec examples.
- Observe copy-on-write and descriptor inheritance.
- Handle child status and signals correctly.

### Deliverable
**Process laboratory plus the first version of a miniature shell.**

### Success criteria
- [ ] No zombies remain.
- [ ] Exit status propagates correctly.
- [ ] Can predict parent/child memory and descriptor behavior.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R14 — OSTEP Homework Simulators](https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html) — Free source code and exercises.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 35 — File descriptors, pipes and shell execution

**Programming language:** C


### Knowledge points
- Descriptor tables and open-file descriptions.
- dup2, redirection and pipelines.
- Blocking I/O and descriptor lifetime.

### Problem-decomposition focus
Separate parsing, execution plan, descriptor wiring, process lifecycle and error reporting.

### Required work
- Add redirection and pipelines to the shell.
- Draw descriptor state before/after dup2.
- Test missing commands, permissions and broken pipes.

### Deliverable
**Mini shell with pipelines, redirection and integration tests.**

### Success criteria
- [ ] Unused pipe ends are closed.
- [ ] No hangs from leaked descriptors.
- [ ] Parser and executor are independently testable.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 36 — Threads, races and nondeterminism

**Programming language:** C with pthreads


### Knowledge points
- Thread stacks and shared address space.
- Interleavings, atomicity and data races.
- Thread safety and reentrancy.

### Problem-decomposition focus
For every shared variable name owner, readers, writers and synchronization requirement.

### Required work
- Create a race deliberately.
- Enumerate possible interleavings.
- Build unsafe then safe parallel file hashing.

### Deliverable
**Race-condition incident report with reproduction and correction.**

### Success criteria
- [ ] Race is reproducible under stress.
- [ ] Shared state inventory is complete.
- [ ] Can distinguish data race from higher-level race condition.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R14 — OSTEP Homework Simulators](https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html) — Free source code and exercises.

## Week 37 — Locks, condition variables and semaphores

**Programming language:** C with pthreads


### Knowledge points
- Mutex discipline and critical sections.
- Condition predicates and wait loops.
- Semaphores and bounded resources.

### Problem-decomposition focus
Write the synchronization predicate and invariant before selecting a primitive.

### Required work
- Implement bounded producer-consumer queue.
- Use randomized schedules and sanitizers.
- Prove queue safety properties informally.

### Deliverable
**Concurrent IOC-enrichment work queue.**

### Success criteria
- [ ] No data race or deadlock in stress tests.
- [ ] Condition waits use predicate loops.
- [ ] Queue invariants are documented and tested.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R14 — OSTEP Homework Simulators](https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html) — Free source code and exercises.

## Week 38 — Deadlock, scheduling and liveness

**Programming language:** C + Python simulation


### Knowledge points
- Deadlock conditions, wait-for graphs and lock ordering.
- Starvation, livelock and fairness.
- CPU scheduling and latency/throughput trade-offs.

### Problem-decomposition focus
Construct resource graph and measurable scheduling objective before proposing a policy.

### Required work
- Create and fix a deadlock.
- Simulate FCFS, round-robin and priority scheduling.
- Analyze mixed CPU/I/O workloads.

### Deliverable
**Scheduling simulator and concurrency postmortem.**

### Success criteria
- [ ] Can identify all four deadlock conditions.
- [ ] Fix preserves required concurrency.
- [ ] Performance claims use multiple workloads.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R14 — OSTEP Homework Simulators](https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html) — Free source code and exercises.

## Week 39 — Address spaces, paging and replacement

**Programming language:** C + Python


### Knowledge points
- Virtual pages, page tables, TLB and protection.
- Demand paging, working sets and page faults.
- FIFO, LRU approximation and clock.

### Problem-decomposition focus
Define address-reference workload and success metric before comparing replacement policies.

### Required work
- Inspect Linux mappings/faults.
- Implement a page-replacement simulator.
- Construct a Belady-anomaly case.

### Deliverable
**Virtual-memory experiment with hand-worked validation.**

### Success criteria
- [ ] Simulator matches known traces.
- [ ] Can distinguish capacity from locality issue.
- [ ] Can explain copy-on-write.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R14 — OSTEP Homework Simulators](https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html) — Free source code and exercises.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 40 — File systems, naming and storage layout

**Programming language:** C


### Knowledge points
- Inodes, directories, links and path resolution.
- Allocation, metadata, caching and free-space management.
- Sequential versus random I/O.

### Problem-decomposition focus
State persistent invariants and separate naming, metadata and data placement.

### Required work
- Explore links and inode behavior.
- Implement directory traversal.
- Measure sequential/random file access.

### Deliverable
**Filesystem explorer and storage-path diagram.**

### Success criteria
- [ ] Can distinguish inode from pathname.
- [ ] Traversal handles cycles and errors.
- [ ] Measurements explain device/cache effects cautiously.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R14 — OSTEP Homework Simulators](https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html) — Free source code and exercises.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 41 — Crash consistency, journaling and durable updates

**Programming language:** C


### Knowledge points
- Write ordering, atomic rename and fsync.
- Journaling and recovery concepts.
- Durability boundaries and failure injection.

### Problem-decomposition focus
Enumerate every crash point between persistent state transitions.

### Required work
- Build crash-safe snapshot writer.
- Inject process termination between writes.
- Document which guarantees depend on filesystem/hardware assumptions.

### Deliverable
**Crash-safe IOC snapshot service with recovery tests.**

### Success criteria
- [ ] No partial snapshot becomes visible.
- [ ] Recovery is idempotent.
- [ ] Durability claims are precise and bounded.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R14 — OSTEP Homework Simulators](https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html) — Free source code and exercises.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 42 — Sockets, OS integration and systems gate

**Programming language:** C


### Knowledge points
- Socket lifecycle and blocking behavior.
- Client/server concurrency choices.
- Integration of processes, threads, memory and persistence.

### Problem-decomposition focus
Separate protocol, connection lifecycle, worker model, state ownership and shutdown.

### Required work
- Build a local TCP service around the work queue and snapshot store.
- Test disconnects, partial reads and shutdown.
- Complete oral OS defense.

### Deliverable
**Systems project: networked IOC ingestion daemon with graceful shutdown and durable snapshots.**

### Success criteria
- [ ] Protocol handles framing and partial I/O.
- [ ] Failure tests cover process crash and client disconnect.
- [ ] Gate score is at least 10/12 with no zero.

### Free resources
- [R11 — Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) — Free YouTube access.
- [R13 — Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free book chapters.
- [R19 — Stanford CS 144 Introduction to Computer Networking](https://cs144.github.io/) — Open lectures and lab specifications; campus submission service is not required.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

# P6 — Database systems (Weeks 43–48)

**Influence:** CMU 15-445/645  
**Goal:** Understand databases as systems: pages, indexes, query execution, transactions, concurrency control and recovery.


## Week 43 — Relational model, SQL and query plans

**Programming language:** SQL + Python


### Knowledge points
- Relations, keys, constraints and normalization trade-offs.
- Joins, aggregation and window functions.
- Logical query versus physical plan.

### Problem-decomposition focus
Start from required questions and invariants; derive schema and indexes afterward.

### Required work
- Model an IOC/detection dataset.
- Write analytical queries.
- Inspect SQLite/PostgreSQL query plans.

### Deliverable
**Schema, representative workload and query-plan notebook.**

### Success criteria
- [ ] Constraints encode domain rules.
- [ ] Queries have expected-result tests.
- [ ] Indexes are not added without a target query.

### Free resources
- [R16 — CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) — Open lectures, slides, homework and BusTub project specifications.
- [R17 — SQLite Documentation](https://www.sqlite.org/docs.html) — Free.
- [R18 — PostgreSQL Documentation](https://www.postgresql.org/docs/) — Free.

## Week 44 — Pages, records and buffer pools

**Programming language:** C++ reading + Python or C++ implementation


### Knowledge points
- Heap files, slotted pages and record layout.
- Buffer-pool pinning, dirty pages and eviction.
- Durability boundary between memory and disk.

### Problem-decomposition focus
Separate page format, disk manager, cache policy and concurrency concerns.

### Required work
- Study CMU storage lectures.
- Implement fixed-size pages and a small buffer pool.
- Inject full-disk and corrupt-page failures.

### Deliverable
**Page-based mini storage manager.**

### Success criteria
- [ ] Records survive restart.
- [ ] Page invariants are tested.
- [ ] Eviction policy is replaceable.

### Free resources
- [R16 — CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) — Open lectures, slides, homework and BusTub project specifications.
- [R17 — SQLite Documentation](https://www.sqlite.org/docs.html) — Free.

## Week 45 — B+ trees and hash indexes

**Programming language:** C++ or Python


### Knowledge points
- Fan-out, page splits and ordered scans.
- B+ tree search/insert concepts.
- Hash indexes and workload fit.

### Problem-decomposition focus
Define supported predicates and page-size constraints before choosing index structure.

### Required work
- Implement a simplified paged B+ tree or complete selected BusTub work locally.
- Test splits and root changes.
- Compare point lookup and range scan.

### Deliverable
**Index module plus invariant checker.**

### Success criteria
- [ ] Search returns correct results after repeated splits.
- [ ] Leaf ordering and linkage invariants hold.
- [ ] Choice is justified from query workload.

### Free resources
- [R16 — CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) — Open lectures, slides, homework and BusTub project specifications.
- [R17 — SQLite Documentation](https://www.sqlite.org/docs.html) — Free.
- [R18 — PostgreSQL Documentation](https://www.postgresql.org/docs/) — Free.

## Week 46 — Query execution, joins and optimization

**Programming language:** C++ reading + Python


### Knowledge points
- Iterator/Volcano execution model.
- Nested-loop, hash and merge joins.
- Cardinality estimation and cost-based choices.

### Problem-decomposition focus
Represent a query as operators with contracts, then identify dominant data movement.

### Required work
- Implement simple operators over pages.
- Compare join strategies on controlled datasets.
- Explain one PostgreSQL planner decision.

### Deliverable
**Mini query executor and benchmark report.**

### Success criteria
- [ ] Operators compose through a stable interface.
- [ ] Join output is tested against SQL reference.
- [ ] Cost explanation includes cardinality assumptions.

### Free resources
- [R16 — CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) — Open lectures, slides, homework and BusTub project specifications.
- [R18 — PostgreSQL Documentation](https://www.postgresql.org/docs/) — Free.

## Week 47 — Transactions, isolation and concurrency control

**Programming language:** SQL + Python/C++


### Knowledge points
- Atomicity, consistency, isolation and durability.
- Schedules, serializability and anomalies.
- Two-phase locking and MVCC concepts.

### Problem-decomposition focus
State required invariant and acceptable visibility per operation before choosing isolation level.

### Required work
- Reproduce dirty/non-repeatable/phantom-style behaviors where supported.
- Analyze concurrent IOC updates.
- Design lock or MVCC behavior for the mini engine.

### Deliverable
**Isolation laboratory and concurrency-control design.**

### Success criteria
- [ ] Can distinguish application invariant from DB guarantee.
- [ ] Anomalies are shown with precise schedules.
- [ ] Chosen isolation level is justified per workflow.

### Free resources
- [R16 — CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) — Open lectures, slides, homework and BusTub project specifications.
- [R18 — PostgreSQL Documentation](https://www.postgresql.org/docs/) — Free.

## Week 48 — WAL, recovery and database gate

**Programming language:** Python or C++


### Knowledge points
- Write-ahead logging, checkpoints and recovery.
- Redo, undo and idempotent replay.
- Crash points in transaction commit.

### Problem-decomposition focus
Model transaction states and crash points; derive recovery actions from persisted evidence.

### Required work
- Add a simple WAL to the storage manager.
- Inject crashes before/after log and data writes.
- Select final capstone scope and freeze its core guarantees.

### Deliverable
**Recoverable mini storage engine and capstone proposal.**

### Success criteria
- [ ] Committed data survives restart.
- [ ] Uncommitted effects are absent or undone as designed.
- [ ] Gate score is at least 10/12 with no zero.

### Free resources
- [R16 — CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) — Open lectures, slides, homework and BusTub project specifications.
- [R17 — SQLite Documentation](https://www.sqlite.org/docs.html) — Free.
- [R18 — PostgreSQL Documentation](https://www.postgresql.org/docs/) — Free.

# P7 — Networking and security (Weeks 49–54)

**Influence:** Stanford CS 144 + Berkeley CS 161  
**Goal:** Trace real network behavior, implement reliable transport concepts and design systems with explicit security boundaries.


## Week 49 — Ethernet, IP, routing and the packet path

**Programming language:** C++ or C + packet tools


### Knowledge points
- Layering, frames, packets, addressing and forwarding.
- ARP/neighbor discovery, routing tables and TTL.
- Host-to-host packet path.

### Problem-decomposition focus
Trace each hop and name state consulted, header changes and failure outcomes.

### Required work
- Study CS 144 opening material.
- Capture and annotate traffic.
- Trace packets across host, router/NAT and destination.

### Deliverable
**Packet-path report grounded in the home lab.**

### Success criteria
- [ ] Can explain L2 versus L3 decisions.
- [ ] Header fields are interpreted correctly.
- [ ] NAT and routing are not conflated.

### Free resources
- [R19 — Stanford CS 144 Introduction to Computer Networking](https://cs144.github.io/) — Open lectures and lab specifications; campus submission service is not required.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 50 — Reliable transport, flow and congestion control

**Programming language:** C++


### Knowledge points
- Sequence numbers, acknowledgments and retransmission.
- Sliding windows, flow control and congestion control.
- Connection state machines and timers.

### Problem-decomposition focus
Define sender/receiver state, invariants, timer behavior and duplicate handling.

### Required work
- Implement selected CS 144 byte-stream/TCP concepts locally.
- Simulate loss, reordering and duplication.
- Explain exactly-once illusions over an unreliable network.

### Deliverable
**Reliable-stream component with adversarial tests.**

### Success criteria
- [ ] Data is delivered in order without duplication.
- [ ] Window and sequence arithmetic are tested at boundaries.
- [ ] Timeout behavior is deterministic under a fake clock.

### Free resources
- [R19 — Stanford CS 144 Introduction to Computer Networking](https://cs144.github.io/) — Open lectures and lab specifications; campus submission service is not required.

## Week 51 — DNS, HTTP, TLS and service architecture

**Programming language:** Python/Go + packet tools


### Knowledge points
- DNS resolution and caching.
- HTTP semantics, proxies and load balancing.
- TLS handshake, certificates and trust boundaries.

### Problem-decomposition focus
Separate naming, transport security, application semantics and deployment topology.

### Required work
- Trace DNS and TLS for a controlled domain.
- Build a small HTTP service behind a reverse proxy.
- Document caching and retry implications.

### Deliverable
**End-to-end request trace and service topology.**

### Success criteria
- [ ] Can locate trust decisions in TLS.
- [ ] Can distinguish HTTP retry safety by method/operation.
- [ ] Caching behavior is explicit.

### Free resources
- [R19 — Stanford CS 144 Introduction to Computer Networking](https://cs144.github.io/) — Open lectures and lab specifications; campus submission service is not required.
- [R21 — Berkeley CS 161 Computer Security Textbook](https://textbook.cs161.org/) — Free HTML and PDF.
- [R25 — Linux man-pages Project](https://man7.org/linux/man-pages/) — Free.

## Week 52 — Security principles, threat modeling and memory safety

**Programming language:** C + design writing


### Knowledge points
- Assets, adversaries, trust boundaries and attack surfaces.
- Least privilege, defense in depth and complete mediation.
- Memory corruption and exploit primitives conceptually.

### Problem-decomposition focus
Threat model each interface: asset, attacker capability, entry point, control and residual risk.

### Required work
- Study CS 161 introduction and memory-safety units.
- Audit the C ingestion daemon.
- Create exploit-oriented tests without writing harmful deployment code.

### Deliverable
**Threat model and secure redesign for the ingestion daemon.**

### Success criteria
- [ ] Trust boundaries are diagrammed.
- [ ] Controls map to explicit threats.
- [ ] Residual risks and assumptions are acknowledged.

### Free resources
- [R20 — UC Berkeley CS 161 — Spring 2026](https://sp26.cs161.org/) — Open lectures, worksheets and project specifications.
- [R21 — Berkeley CS 161 Computer Security Textbook](https://textbook.cs161.org/) — Free HTML and PDF.

## Week 53 — Cryptography, authentication and web security

**Programming language:** Python/Go + design writing


### Knowledge points
- Hash/MAC/signature/encryption roles.
- Key management and authentication protocols.
- Injection, XSS, CSRF, session and authorization failures.

### Problem-decomposition focus
Choose primitives only after defining authenticity, confidentiality, freshness and authorization requirements.

### Required work
- Complete selected CS 161 crypto/web units.
- Design signed provider updates.
- Audit a small API for injection and authorization failures.

### Deliverable
**Authenticated update protocol and web/API security checklist.**

### Success criteria
- [ ] No custom cryptographic primitive is invented.
- [ ] Replay handling is explicit.
- [ ] Authentication and authorization are separated.

### Free resources
- [R20 — UC Berkeley CS 161 — Spring 2026](https://sp26.cs161.org/) — Open lectures, worksheets and project specifications.
- [R21 — Berkeley CS 161 Computer Security Textbook](https://textbook.cs161.org/) — Free HTML and PDF.

## Week 54 — Network security and secure-service gate

**Programming language:** Go or Python


### Knowledge points
- Network segmentation, firewall limits and shared infrastructure.
- Secure logging, rate limits and abuse resistance.
- Security versus availability trade-offs.

### Problem-decomposition focus
Define allowed flows, identities, trust zones, abuse cases and failure behavior.

### Required work
- Build a secure telemetry collector with TLS/authentication, bounded queues and audit logs.
- Test malformed clients, replay, overload and dependency failure.
- Complete security/network oral review.

### Deliverable
**Secure collector integrated with the storage engine.**

### Success criteria
- [ ] Overload is bounded rather than catastrophic.
- [ ] Logs avoid secrets while preserving evidence.
- [ ] Gate score is at least 10/12 with no zero.

### Free resources
- [R19 — Stanford CS 144 Introduction to Computer Networking](https://cs144.github.io/) — Open lectures and lab specifications; campus submission service is not required.
- [R20 — UC Berkeley CS 161 — Spring 2026](https://sp26.cs161.org/) — Open lectures, worksheets and project specifications.
- [R21 — Berkeley CS 161 Computer Security Textbook](https://textbook.cs161.org/) — Free HTML and PDF.
- [R23 — Google SRE Books](https://sre.google/books/) — Free read-online editions.

# P8 — Distributed systems, system design and capstone (Weeks 55–60)

**Influence:** MIT 6.5840 + MIT 6.033 + Google SRE  
**Goal:** Design, implement, test and defend a fault-aware threat-intelligence system using measurable guarantees.


## Week 55 — Distributed failures, time, RPC and idempotency

**Programming language:** Go


### Knowledge points
- Partial failure and unreliable communication.
- RPC semantics, deadlines, retries and duplicate requests.
- Idempotency keys and at-most/at-least-once behavior.

### Problem-decomposition focus
For each operation enumerate request loss, response loss, duplication, reordering, timeout and retry.

### Required work
- Learn required Go basics.
- Complete/adapt MIT 6.5840 MapReduce or key/value introductory lab.
- Add idempotency to one capstone operation.

### Deliverable
**Failure matrix and retry-safe API implementation.**

### Success criteria
- [ ] Every retry policy has a bound.
- [ ] Duplicate effects are prevented or detected.
- [ ] Can explain why timeout does not reveal operation outcome.

### Free resources
- [R22 — MIT 6.5840 Distributed Systems — Spring 2026](https://pdos.csail.mit.edu/6.5840/) — Open schedule, papers, questions and Go labs.
- [R31 — Go Documentation and Tour](https://go.dev/learn/) — Free.

## Week 56 — Replication, consistency and quorums

**Programming language:** Go + design writing


### Knowledge points
- Primary/backup and replicated state machines.
- Linearizability, sequential/eventual consistency.
- Read/write quorums and replication lag.

### Problem-decomposition focus
Specify consistency per operation and user-visible anomaly before choosing replication.

### Required work
- Analyze consistency needs of indicator updates versus analytics.
- Simulate replicas with delay and failure.
- Write consistency tests as histories.

### Deliverable
**Replication prototype and consistency contract.**

### Success criteria
- [ ] Consistency terms are used precisely.
- [ ] Tests include stale reads and failover.
- [ ] Trade-off is tied to product behavior.

### Free resources
- [R22 — MIT 6.5840 Distributed Systems — Spring 2026](https://pdos.csail.mit.edu/6.5840/) — Open schedule, papers, questions and Go labs.
- [R15 — MIT 6.033 Computer System Engineering — Spring 2018](https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/) — Free notes, critiques, design project and examples.

## Week 57 — Consensus and Raft

**Programming language:** Go


### Knowledge points
- Leader election, log replication and safety.
- Terms, commit index and majority reasoning.
- Persistence and restart behavior.

### Problem-decomposition focus
Model node state and message handlers as a state machine; test safety under reordered events.

### Required work
- Read the Raft paper.
- Implement/adapt the first Raft stages from MIT 6.5840.
- Use deterministic simulation or controlled tests.

### Deliverable
**Raft implementation notes, state diagram and passing safety tests.**

### Success criteria
- [ ] Election safety and log matching are explainable.
- [ ] Persistent state survives restart.
- [ ] No correctness argument depends on timing alone.

### Free resources
- [R22 — MIT 6.5840 Distributed Systems — Spring 2026](https://pdos.csail.mit.edu/6.5840/) — Open schedule, papers, questions and Go labs.
- [R24 — Raft Consensus Paper](https://raft.github.io/raft.pdf) — Free PDF.

## Week 58 — Partitioning, streams and distributed transactions

**Programming language:** Go + SQL


### Knowledge points
- Sharding keys and hotspot risk.
- Event ordering, consumer groups and idempotent processing.
- Sagas, two-phase commit and atomic-outbox pattern.

### Problem-decomposition focus
Define atomicity boundary, ordering scope and recovery action for each multi-component workflow.

### Required work
- Design partitioning for telemetry/IOC workloads.
- Implement idempotent event consumption with an outbox or equivalent.
- Inject duplicates and consumer restarts.

### Deliverable
**Capstone event pipeline with recovery tests.**

### Success criteria
- [ ] Partition key follows access pattern.
- [ ] Consumer replay is safe.
- [ ] Cross-system invariants have an explicit reconciliation strategy.

### Free resources
- [R22 — MIT 6.5840 Distributed Systems — Spring 2026](https://pdos.csail.mit.edu/6.5840/) — Open schedule, papers, questions and Go labs.
- [R16 — CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) — Open lectures, slides, homework and BusTub project specifications.
- [R23 — Google SRE Books](https://sre.google/books/) — Free read-online editions.

## Week 59 — System design, capacity, SLOs and failure injection

**Programming language:** Design writing + Go/Python


### Knowledge points
- Requirements clarification and back-of-envelope estimation.
- SLIs, SLOs, error budgets and observability.
- Load, fault and recovery testing.

### Problem-decomposition focus
Use a timed design flow: requirements → estimates → model/API → architecture → deep dive → failure/security → recap.

### Required work
- Complete an MIT 6.033-style design document.
- Define capstone SLOs and capacity model.
- Run load and failure-injection experiments.

### Deliverable
**Final architecture packet: diagrams, ADRs, threat model, capacity model, SLOs and experiment results.**

### Success criteria
- [ ] Numbers influence architecture.
- [ ] Critical guarantees have tests.
- [ ] Unknowns are listed as risks rather than hidden.

### Free resources
- [R15 — MIT 6.033 Computer System Engineering — Spring 2018](https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/) — Free notes, critiques, design project and examples.
- [R23 — Google SRE Books](https://sre.google/books/) — Free read-online editions.
- [R30 — Google Engineering Practices](https://google.github.io/eng-practices/) — Free.

## Week 60 — Capstone completion, oral defense and next specialization

**Programming language:** Go/Python/SQL/C as appropriate


### Knowledge points
- Synthesis across algorithms, architecture, OS, databases, networks, security and distributed systems.
- Evidence-based technical decisions.
- Technical communication and honest limitation analysis.

### Problem-decomposition focus
Freeze scope; map each requirement to component contract, test and evidence.

### Required work
- Finish one production-quality vertical slice of the threat-intelligence platform.
- Run a clean-room setup from documentation.
- Conduct a 60-minute oral defense with an AI tutor and record corrections.

### Deliverable
**Portfolio capstone: repository, runnable demo, architecture document, ADRs, tests, benchmarks, failure evidence and retrospective.**

### Success criteria
- [ ] A new engineer can run it from documentation.
- [ ] At least three failure modes are demonstrated and recovered from.
- [ ] Final tutor score is at least 10/12 with no zero and every limitation is stated.

### Free resources
- [R15 — MIT 6.033 Computer System Engineering — Spring 2018](https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/) — Free notes, critiques, design project and examples.
- [R16 — CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) — Open lectures, slides, homework and BusTub project specifications.
- [R19 — Stanford CS 144 Introduction to Computer Networking](https://cs144.github.io/) — Open lectures and lab specifications; campus submission service is not required.
- [R20 — UC Berkeley CS 161 — Spring 2026](https://sp26.cs161.org/) — Open lectures, worksheets and project specifications.
- [R22 — MIT 6.5840 Distributed Systems — Spring 2026](https://pdos.csail.mit.edu/6.5840/) — Open schedule, papers, questions and Go labs.
- [R23 — Google SRE Books](https://sre.google/books/) — Free read-online editions.

# Free resource catalog

| ID | Resource | Type | Access | Role |
|---|---|---|---|---|
| R01 | [UC Berkeley CS 61A — Spring 2026](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) | Course | Open lectures, notes, labs, homework and project specifications | Programming abstraction, recursion, functional programming, interpreters and SQL |
| R02 | [Composing Programs](https://www.composingprograms.com/) | Open textbook | Free online textbook | Stable reading companion for CS 61A |
| R03 | [UC Berkeley CS 61B — Spring 2026](https://sp26.datastructur.es/) | Course | Open lectures, worksheets, homework and project specifications; institutional autograding may be unavailable | Data structures, Java, testing and software construction |
| R04 | [MIT 6.1200J Mathematics for Computer Science — Spring 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) | Course / open textbook | Free lectures, text, problem sets and downloadable course package | Proofs, induction, graph theory, counting, probability and recurrences |
| R05 | [UC Berkeley CS 70 — Summer 2026](https://www.eecs70.org/) | Course | Open notes, discussion worksheets and homework | Discrete mathematics and probability at Berkeley depth |
| R06 | [MIT 6.006 Introduction to Algorithms — Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | Course | Free lecture videos, notes, recitations, assignments and exams | Algorithm modeling, correctness and efficiency |
| R07 | [UC Berkeley CS 61C — Spring 2026](https://cs61c.org/sp26/) | Course | Open schedule, notes, slides and project specifications | C, RISC-V, caches, virtual memory and parallelism |
| R08 | [Berkeley CS 61C Course Notes](https://notes.cs61c.org/) | Open notes | Free online notes and exercises | Stable machine-structures reference |
| R09 | [Beej's Guide to C Programming](https://beej.us/guide/bgc/) | Open book | Free online and downloadable | C syntax, pointers, memory and practical reference |
| R10 | [GNU GDB Documentation](https://sourceware.org/gdb/documentation/) | Official documentation | Free | Low-level debugging |
| R11 | [Berkeley CS 162 Lecture Playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) | Lecture series | Free YouTube access | Primary operating-systems lecture spine selected by the learner |
| R12 | [UC Berkeley CS 162 — Official Course Description](https://www2.eecs.berkeley.edu/Courses/CS162/) | Official course page | Free | Scope and prerequisite reference |
| R13 | [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) | Open textbook | Free book chapters | Processes, concurrency, virtual memory and persistence |
| R14 | [OSTEP Homework Simulators](https://pages.cs.wisc.edu/~remzi/OSTEP/Homework/homework.html) | Exercises | Free source code and exercises | Hands-on OS reasoning |
| R15 | [MIT 6.033 Computer System Engineering — Spring 2018](https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/) | Course | Free notes, critiques, design project and examples | System design, technical writing, modularity, reliability and security |
| R16 | [CMU 15-445/645 Intro to Database Systems — Spring 2026](https://15445.courses.cs.cmu.edu/spring2026/) | Course | Open lectures, slides, homework and BusTub project specifications | Database internals |
| R17 | [SQLite Documentation](https://www.sqlite.org/docs.html) | Official documentation | Free | Practical SQL, storage and transaction experiments |
| R18 | [PostgreSQL Documentation](https://www.postgresql.org/docs/) | Official documentation | Free | Query plans, transactions, indexes and production behavior |
| R19 | [Stanford CS 144 Introduction to Computer Networking](https://cs144.github.io/) | Course | Open lectures and lab specifications; campus submission service is not required | Internet architecture and transport implementation |
| R20 | [UC Berkeley CS 161 — Spring 2026](https://sp26.cs161.org/) | Course | Open lectures, worksheets and project specifications | Memory, cryptographic, web and network security |
| R21 | [Berkeley CS 161 Computer Security Textbook](https://textbook.cs161.org/) | Open textbook | Free HTML and PDF | Stable security reference |
| R22 | [MIT 6.5840 Distributed Systems — Spring 2026](https://pdos.csail.mit.edu/6.5840/) | Course | Open schedule, papers, questions and Go labs | Replication, consistency, consensus and fault tolerance |
| R23 | [Google SRE Books](https://sre.google/books/) | Open books | Free read-online editions | Reliability, operations, SLOs and secure systems |
| R24 | [Raft Consensus Paper](https://raft.github.io/raft.pdf) | Research paper | Free PDF | Understandable consensus algorithm |
| R25 | [Linux man-pages Project](https://man7.org/linux/man-pages/) | Official-style reference | Free | System calls, POSIX APIs and Linux behavior |
| R26 | [Princeton Algorithms, 4th Edition Site](https://algs4.cs.princeton.edu/home/) | Course companion | Free summaries, code and exercises | Alternative data-structures and algorithms practice |
| R27 | [Open Data Structures](https://opendatastructures.org/) | Open textbook | Free HTML/PDF editions | Language-neutral data-structure reference |
| R28 | [Crafting Interpreters](https://craftinginterpreters.com/) | Open book | Free online | Optional deeper interpreter implementation |
| R29 | [Nand2Tetris](https://www.nand2tetris.org/) | Course / projects | Free software, lectures and project materials | Optional constructive computer architecture |
| R30 | [Google Engineering Practices](https://google.github.io/eng-practices/) | Engineering guide | Free | Code review, change quality and maintainability |
| R31 | [Go Documentation and Tour](https://go.dev/learn/) | Official documentation | Free | Go preparation for distributed-systems labs |

# Optional paid supplements — never required

These may be useful if you already own them or can borrow them legally, but the plan does not depend on them:

- *Designing Data-Intensive Applications*;
- *Computer Systems: A Programmer's Perspective*;
- *Operating Systems: Principles and Practice*;
- *Introduction to Algorithms*;
- a printed edition of any free online text.

# AI tutor contract

The complete tutor instructions are in `AGENT_TUTOR.md`. The essential rule is: the tutor must require an attempt and reasoning before giving a solution. It should quiz prior material, inspect the current week's `DESIGN.md`, generate exercises inside the current scope, grade the rubric, and block advancement when a core criterion is zero.

# Start command

```text
Act as my computer-science and systems tutor. Read curriculum.md,
curriculum.json, AGENT_TUTOR.md and progress.md completely. Determine the
current week from progress.md. Begin with five retrieval questions from prior
weeks. Then require me to restate and decompose the current problem before
coding. Do not provide the full solution before a serious attempt. Grade all
work with the six-category rubric and update only the evidence-based status.
```
