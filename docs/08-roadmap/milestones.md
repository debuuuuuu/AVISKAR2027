# Project Milestones & Verification Criteria

This document defines the formal milestones for the **Trust-Aware Service Selection** framework, outlining verification criteria and deliverables for each milestone.

---

## Milestone 1: Problem Formulation & Literature Grounding [COMPLETED]
- **Target Date:** 2026-08-15
- **Deliverables:**
  - Formal formulation of the Central Research Question.
  - Comprehensive literature review analyzing multi-agent reputation systems and the ERC-8004 empirical study (Xiong et al., 2026).
  - Clean distinction between trust, reputation, and evidence.
- **Verification Criteria:** Annotated bibliography complete; research gap clearly positioned without unsubstantiated hype.

---

## Milestone 2: Complete System Architecture & Threat Model [COMPLETED]
- **Target Date:** 2026-08-31
- **Deliverables:**
  - 10-component modular architecture with C4 context and component diagrams.
  - Comprehensive threat model covering 14 adversarial vectors with mitigations and boundaries.
  - Architectural role definition for RAG, MCP, Blockchain, and x402.
- **Verification Criteria:** Mermaid diagrams render cleanly; explicit data flow and sequence diagrams specified.

---

## Milestone 3: Core Simulation Engine & Data Schemas [COMPLETED]
- **Target Date:** 2026-09-15
- **Deliverables:**
  - Validated Pydantic models in `src/data_models.py` for all 13 core entities.
  - Modular implementation of Selection Strategies (Random, Reputation, Evidence-Based).
  - Subprocess sandboxed Result Verification Layer.
  - Local RAG vector evidence retrieval engine with exponential time decay.
- **Verification Criteria:** 100% test pass rate across unit test suites (`pytest tests/unit/`).

---

## Milestone 4: Benchmark Experiment Execution [IN PROGRESS]
- **Target Date:** 2026-09-25
- **Deliverables:**
  - Execution of 100-task deterministic workload on 30 simulated agents across 10 random seeds.
  - Generation of raw JSONL execution logs in `experiments/runs/`.
  - Population of formal metric tables in `docs/04-experiment/results.md`.
- **Verification Criteria:** Deterministic replication confirmed via `scripts/experiment/reproduce_eval.py`.

---

## Milestone 5: Statistical Validation & Academic Publication [PLANNED]
- **Target Date:** 2026-10-15
- **Deliverables:**
  - Wilcoxon signed-rank paired statistical tests ($p < 0.05$).
  - Generation of high-resolution metric visualization plots.
  - Preparation of conference preprint for submission.
