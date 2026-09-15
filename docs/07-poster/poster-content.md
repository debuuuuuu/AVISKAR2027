# Complete Poster Content & Section-by-Section Guide

This document maps the exact text, scientific claims, presenter talking points, and anticipated judge questions for each of the **10 standard academic poster sections**.

---

## Poster Section 1: Introduction
- **Poster Text:**  
  Autonomous AI agents increasingly delegate specialized subtasks (code execution, mathematical optimization, data parsing) to external third-party services. In decentralized agent ecosystems, orchestrating agents must select service providers under deep uncertainty without central gatekeepers.
- **Where Supporting Docs Live:** [`docs/01-overview/project-overview.md`](../01-overview/project-overview.md).
- **Presenter Talking Point:** *"We are moving toward an open internet of AI agents delegating work to other agents. The core challenge is how an agent decides whom to trust without human oversight."*
- **Anticipated Judge Question:** *"Why not just hardcode trusted APIs?"* $\to$ **Answer:** *"Hardcoding creates static centralization and fails to scale to millions of dynamic micro-agents in decentralized marketplaces."*

---

## Poster Section 2: Problem Statement
- **Poster Text:**  
  Open agent registries suffer from three systemic vulnerabilities: (1) *Cheap Talk*: unverified capability advertisements; (2) *Coordinated Sybil Reviews*: collusive rating syndicates artificially pumping 5-star ratings; (3) *The Halo Effect*: high reputation in simple domains masking catastrophic failure in sensitive or complex domains.
- **Where Supporting Docs Live:** [`docs/01-overview/problem-statement.md`](../01-overview/problem-statement.md).
- **Presenter Talking Point:** *"Public star ratings don't work for AI agents. An agent can buy 500 fake ratings, or have 5 stars in copywriting, and then inject malicious SQL when you assign it a database task."*
- **Anticipated Judge Question:** *"Is this a theoretical problem or does it exist today?"* $\to$ **Answer:** *"It exists today in live decentralized registries like ERC-8004, where over 85% of endpoints are dead and up to 90% of reviewers are Sybils."*

---

## Poster Section 3: Objectives & Research Question
- **Poster Text:**  
  **Central Research Question:** *Can task-specific, verifiable evidence improve autonomous AI-agent service selection compared with reputation-only scoring?*  
  **Objectives:** (1) Formulate a 6-dimensional trust model; (2) Design a closed-loop verification pipeline; (3) Implement a 30-agent controlled benchmark comparing Random, Reputation-Only, and Evidence-Based selection across 5 metrics.
- **Where Supporting Docs Live:** [`docs/01-overview/research-question.md`](../01-overview/research-question.md), [`docs/01-overview/objectives.md`](../01-overview/objectives.md).
- **Presenter Talking Point:** *"Our objective is to prove whether verified task evidence produces a measurable, statistically significant improvement over reputation-only selection."*

---

## Poster Section 4: Methodology
- **Poster Text:**  
  Controlled synthetic simulation testbed with $N = 30$ heterogeneous service agents: 20 Reliable (96% accuracy), 5 Unreliable (25% timeouts), and 5 Malicious (Sybil-boosted $\rho \in [0.93, 0.99]$, conditional poisoning). A deterministic workload generator dispatches 100 tasks across 5 domains with assigned risk stakes ($R \in [0.2, 0.85]$).
- **Where Supporting Docs Live:** [`docs/04-experiment/experimental-design.md`](../04-experiment/experimental-design.md), [`docs/04-experiment/agent-population.md`](../04-experiment/agent-population.md).
- **Presenter Talking Point:** *"We hold the task sequence and candidate fleet constant across all three strategies to isolate the exact causal effect of our evidence-based selection algorithm."*

---

## Poster Section 5: Block Diagram / System Architecture
- **Poster Visual:** High-Level 10-Component Flow (Ingestion $\to$ RAG Evidence $\to$ Risk Gating $\to$ MCP Dispatch $\to$ Sandbox Verification $\to$ Merkle Anchor).
- **Where Supporting Docs Live:** [`docs/03-system-design/architecture.md`](../03-system-design/architecture.md), [`diagrams/poster/poster-architecture.mmd`](../../diagrams/poster/poster-architecture.mmd).
- **Presenter Talking Point:** *"Notice the closed loop: every task output is sandboxed and verified, and that verified verdict immediately updates our local vector index and blockchain commitment log."*

---

## Poster Section 6: Existing Research Evidence (ERC-8004 Empirical Study)
- **Poster Text:**  
  **EXISTING RESEARCH EVIDENCE (Xiong et al., 2026, arXiv:2606.26028):**  
  - *Live Endpoint Availability:* Ethereum: **3%** | BNB Chain: **4%** | Base: **15%**  
  - *Coordinated Sybil Reviewers:* Ethereum: **73.6%** | BNB Chain: **59.2%** | Base: **90.6%**  
  - *Reputation Collapse:* Usable ratings completely collapse once Sybils are filtered.
- **Where Supporting Docs Live:** [`docs/02-research/existing-evidence.md`](../02-research/existing-evidence.md).
- **Presenter Talking Point:** *"This independent empirical study published in June 2026 provides the empirical baseline proving that on-chain star ratings cannot be trusted."*

---

## Poster Section 7: Innovativeness & Differentiators
- **Poster Text:**  
  - **Task-Conditioned Trust:** Uses dense vector embeddings (RAG) to condition trust strictly on the requested task domain.
  - **Risk-Calibrated Confidence Gating:** Enforces strict confidence thresholds ($\theta$) on high-stakes tasks with safe fallback.
  - **Closed-Loop Verification Feedback:** Immediately converts verified outputs into empirical evidence.
  - **Tamper-Evident Ledger Commitments:** Merkle root commitments guarantee auditability without leaking private payloads.
- **Where Supporting Docs Live:** [`docs/02-research/novelty-positioning.md`](../02-research/novelty-positioning.md).

---

## Poster Section 8: Practical Applications
- **Poster Text:**  
  1. *Autonomous Coding Swarms:* Orchestrator safely delegates module compilation and unit test execution.  
  2. *Automated Financial Analytics:* Rejects unverified calculation oracles for high-stakes portfolio rebalancing.  
  3. *Enterprise Workflow Automation:* Sanitizes inputs and ensures zero-trust tool execution across external MCP servers.
- **Where Supporting Docs Live:** [`docs/01-overview/scope.md`](../01-overview/scope.md).

---

## Poster Section 9: Evaluation Metrics & Results Framework
- **Poster Text:**  
  Evaluated across 5 formalized metrics: Task Success Rate ($TSR \uparrow$), Malicious Selection Rate ($MASR \downarrow$), False Rejection Rate ($FRR \downarrow$), Verification Overhead ($VCO \downarrow$), and Decision Latency ($SDL \downarrow$).  
  *Status:* Full simulation testbed implemented in Python; multi-seed statistical runs pending.
- **Where Supporting Docs Live:** [`docs/04-experiment/evaluation-metrics.md`](../04-experiment/evaluation-metrics.md), [`docs/04-experiment/results.md`](../04-experiment/results.md).
- **Presenter Talking Point:** *"We uphold strict academic integrity: our testbed is fully implemented, and we report results only from verified physical runs rather than publishing synthetic numbers."*

---

## Poster Section 10: References
- **Poster Text:**  
  1. Xiong et al. (2026), *ERC-8004 Empirical Study*, arXiv:2606.26028 (Preprint)  
  2. Souza et al. (2025), *PROV-AGENT*, IEEE eScience 2025  
  3. Chishti, Oyinloye, & Li (2026), *AgentReputation*, ACM FSE 2026  
  4. Sabater & Sierra (2002), *REGRET Model*, JAAMAS  
  5. Huang et al. (2024), *LLM Self-Correction Limits*, ICLR 2024  
  6. Anthropic (2024), *Model Context Protocol (MCP) Specification*
- **Where Supporting Docs Live:** [`docs/02-research/references.md`](../02-research/references.md), [`docs/02-research/literature-matrix.md`](../02-research/literature-matrix.md).
