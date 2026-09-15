# Poster-to-Repository Evidence Mapping

This document provides a direct cross-reference matrix mapping each section of the physical poster to its authoritative documentation file, empirical source, and implementation module in the repository.

---

## 1. Traceability Cross-Reference Matrix

| Poster Section | Authoritative Documentation File | Code / Data Source | Empirical / Literature Source |
|---|---|---|---|
| **1. Introduction** | [`docs/01-overview/project-overview.md`](../01-overview/project-overview.md) | `src/agent/client_agent.py` | Anthropic MCP Spec (2024) |
| **2. Problem Statement** | [`docs/01-overview/problem-statement.md`](../01-overview/problem-statement.md) | `src/services/malicious.py` | Xiong et al. (2026), arXiv:2606.26028 |
| **3. Objectives & RQ** | [`docs/01-overview/research-question.md`](../01-overview/research-question.md) | `project.yaml` | Section 0 & 1 of Project Charter |
| **4. Methodology** | [`docs/04-experiment/experimental-design.md`](../04-experiment/experimental-design.md) | `experiments/configs/default_simulation.yaml` | Controlled 30-Agent Testbed |
| **5. Block Diagram** | [`docs/03-system-design/architecture.md`](../03-system-design/architecture.md) | `diagrams/poster/poster-architecture.mmd` | C4 Architecture Specification |
| **6. Existing Evidence**| [`docs/02-research/existing-evidence.md`](../02-research/existing-evidence.md) | `research/evidence/erc8004_stats.json` | Xiong et al. (2026), arXiv:2606.26028 |
| **7. Innovativeness** | [`docs/02-research/novelty-positioning.md`](../02-research/novelty-positioning.md) | `src/trust/evaluator.py` | Sabater & Sierra (2002); Jøsang (2002) |
| **8. Applications** | [`docs/01-overview/scope.md`](../01-overview/scope.md) | `src/mcp/tools.py` | Enterprise Multi-Agent Workflows |
| **9. Metrics & Eval** | [`docs/04-experiment/evaluation-metrics.md`](../04-experiment/evaluation-metrics.md) | `src/experiment/metrics.py` | 5 Formalized Mathematical Metrics |
| **10. References** | [`docs/02-research/references.md`](../02-research/references.md) | `research/references.bib` | Master BibTeX Catalog |

---

## 2. Presenter Defense Mapping

When standing by the poster during evaluation sessions:
- If a judge points to **Existing Research Evidence**, cite:  
  *"Xiong et al. (2026) in arXiv:2606.26028, which showed that 59.2% to 90.6% of reviewers on ERC-8004 registries exhibit coordinated Sybil collusion."*
- If a judge points to the **Block Diagram**, trace the path:  
  *"Task Specification $\to$ Semantic RAG $\to$ Multi-Dimensional Trust Gating $\to$ MCP Dispatch $\to$ Isolated Verification Sandbox $\to$ Merkle State Commitment."*
- If a judge asks about **Results**, state:  
  *"Our simulation testbed is fully implemented in Python. In strict compliance with research integrity, empirical results will be populated from verified physical runs without synthetic fabrication."*
