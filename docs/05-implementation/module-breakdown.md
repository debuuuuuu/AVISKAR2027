# Codebase Architecture & Module Breakdown

This document specifies the internal module layout of the `src/` Python package, mapping system components to concrete Python modules and classes.

---

## 1. Directory & Module Map

```text
src/
├── __init__.py                   # Package initialization & version definition
├── data_models.py               # Pydantic schemas (Agent, Task, Evidence, TrustAssessment)
│
├── agent/                       # Client Agent Runtime
│   ├── __init__.py
│   └── client_agent.py          # AutonomousClientAgent class & orchestrator loop
│
├── services/                    # Simulated Service Provider Fleet
│   ├── __init__.py
│   ├── base.py                  # BaseServiceAgent abstract class
│   ├── reliable.py              # ReliableServiceAgent implementation
│   ├── unreliable.py            # UnreliableServiceAgent (timeouts, latency spikes)
│   └── malicious.py             # MaliciousServiceAgent (Sybil, bait-and-switch poisoning)
│
├── trust/                       # Trust & Risk Evaluation
│   ├── __init__.py
│   ├── evaluator.py             # Multidimensional TrustEvaluationEngine
│   └── risk.py                  # RiskAssessmentLayer & confidence threshold mapper
│
├── evidence/                    # Evidence Storage & State Management
│   ├── __init__.py
│   ├── store.py                 # SQLite / DuckDB Document Store
│   └── lifecycle.py             # EvidenceRecord construction & updates
│
├── selection/                   # Service Selection Strategies
│   ├── __init__.py
│   └── strategies.py            # Random, Reputation-Only, and Evidence-Based strategies
│
├── verification/                # Result Verification Layer
│   ├── __init__.py
│   └── verifier.py              # Deterministic, Schema, and Consensus Validators
│
├── rag/                         # Semantic Evidence Retrieval
│   ├── __init__.py
│   └── retriever.py             # Vector embedding similarity search & domain filtering
│
├── mcp/                         # Model Context Protocol Interface
│   ├── __init__.py
│   └── tools.py                 # Standardized MCP tool declarations & handlers
│
├── blockchain/                  # Cryptographic Commitments & Provenance
│   ├── __init__.py
│   └── provenance.py            # Merkle tree batching & state commitment hashing
│
└── experiment/                  # Simulation Execution & Evaluation
    ├── __init__.py
    ├── runner.py                # ExperimentRunner orchestrator
    └── metrics.py               # Evaluation metric calculator (TSR, MASR, FRR, VCO, SDL)
```

---

## 2. Core Class Responsibilities

| Class | Module | Role |
|---|---|---|
| `AutonomousClientAgent` | `src.agent.client_agent` | Master agent executing goals and managing delegation. |
| `BaseServiceAgent` | `src.services.base` | Abstract interface for external service providers. |
| `TrustEvaluationEngine` | `src.trust.evaluator` | Computes multidimensional trust scores. |
| `EvidenceStore` | `src.evidence.store` | Manages local storage of interaction records and embeddings. |
| `ResultVerifier` | `src.verification.verifier` | Evaluates task output correctness and compliance. |
| `SelectionStrategy` | `src.selection.strategies` | Abstract base class for selection algorithms. |
| `EvidenceRetriever` | `src.rag.retriever` | Semantic cosine similarity retriever over task embeddings. |
| `MCPToolHandler` | `src.mcp.tools` | Implements MCP JSON-RPC protocol methods. |
| `ProvenanceManager` | `src.blockchain.provenance` | Computes SHA-256 Merkle roots and verifies state proofs. |
| `ExperimentRunner` | `src.experiment.runner` | Orchestrates 30-agent simulation runs across task sequences. |
