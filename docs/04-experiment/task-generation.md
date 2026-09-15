# Task Generation & Benchmark Workload Specification

This document defines the task generation engine, domain taxonomy, complexity tiers, and risk assignment methodology for experimental trials.

---

## 1. Domain Taxonomy & Task Generators

To rigorously test whether task-specific evidence outperforms global reputation, tasks are generated across **five distinct semantic domains**:

```text
Benchmark Task Corpus (100 Deterministic Tasks)
├── Domain 1: Math Computation       (25 Tasks) | Exact numerical evaluation
├── Domain 2: Code Execution         (25 Tasks) | Sandboxed Python algorithmic logic
├── Domain 3: Schema Transformation  (20 Tasks) | Structural JSON/YAML conversions
├── Domain 4: SQL Query Generation   (15 Tasks) | Relational queries against SQLite
└── Domain 5: Text Classification    (15 Tasks) | Deterministic sentiment/category labeling
```

### 1.1 Domain 1: Mathematical Computation (`math_computation`)
- **Objective:** Evaluate symbolic or numerical equations (e.g., matrix determinants, prime factorizations, numerical integration).
- **Verification Method:** Deterministic numerical comparison against a ground-truth math solver with floating-point tolerance ($\epsilon = 10^{-6}$).

### 1.2 Domain 2: Code Execution (`code_execution`)
- **Objective:** Implement algorithmic functions satisfying formal docstring specifications (e.g., Dijkstra's algorithm, LRU cache implementation).
- **Verification Method:** Subprocess execution running 5 isolated unit test assertions against the generated code.

### 1.3 Domain 3: Schema Transformation (`schema_transformation`)
- **Objective:** Map unstructured or semi-structured JSON objects into a strict target JSON Schema draft-07.
- **Verification Method:** Formal schema validation using Python `jsonschema` library.

### 1.4 Domain 4: SQL Query Generation (`sql_generation`)
- **Objective:** Convert natural language business queries into valid SQL against a sample eCommerce database.
- **Verification Method:** Execute the query against an in-memory SQLite instance and verify result set parity with the gold-standard query.

### 1.5 Domain 5: Text Classification (`text_classification`)
- **Objective:** Categorize multi-sentence documents into one of 10 predetermined classes.
- **Verification Method:** Exact string match against verified benchmark labels.

---

## 2. Risk Tiering & Stakes Distribution

Every task $T$ is assigned an objective Risk Score $R \in [0, 1]$:

| Risk Tier | Risk Value $R$ | Proportion | Criteria / Consequence of Failure |
|---|---|---|---|
| **Low Stakes** | $R = 0.20$ | 40% | Reversible computation; non-sensitive data; exploratory queries. |
| **Medium Stakes** | $R = 0.50$ | 35% | Moderate operational consequence; consumes significant compute; data used in intermediate workflows. |
| **High Stakes** | $R = 0.85$ | 25% | Irreversible execution; critical computational input; high security sensitivity; vulnerable to prompt injection. |

---

## 3. Workload Determinism & Seeding

- All tasks are pre-generated using a deterministic pseudorandom generator initialized with `seed = 42`.
- The task sequence is serialized to `experiments/datasets/benchmark_tasks.jsonl`.
- Each selection strategy evaluates the **exact same task sequence in the exact same order**, ensuring fair, paired statistical comparisons.
