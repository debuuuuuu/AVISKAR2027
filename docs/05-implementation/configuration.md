# System Configuration Specification

This document details the configuration schema, environment variables, and parameter options governing simulation execution, trust thresholds, vector retrieval, and blockchain anchoring.

---

## 1. Environment Variables Reference

Environment variables are managed via `.env` (derived from `.env.example`). Secrets must **never** be committed to version control.

| Variable Name | Default Value | Description |
|---|---|---|
| `SIM_ENVIRONMENT` | `local_simulation` | Execution environment (`local_simulation` or `distributed_testbed`). |
| `SIM_RANDOM_SEED` | `42` | Global integer seed controlling stochastic events and task sequencing. |
| `SIM_AGENT_POPULATION` | `30` | Number of service agents instantiated in simulation. |
| `SIM_DEFAULT_ROUNDS` | `100` | Number of sequential task trials per benchmark run. |
| `SIM_LOG_LEVEL` | `INFO` | Console and file logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`). |
| `VECTOR_STORE_BACKEND` | `in_memory` | Vector database backend (`in_memory`, `chroma`, or `faiss`). |
| `EMBEDDING_MODEL_DIMENSION` | `384` | Dimensionality of semantic task domain embedding vectors. |
| `EVIDENCE_RECENCY_HALF_LIFE_DAYS`| `30` | Number of days after which evidence weight decays by 50% ($\lambda$). |
| `BLOCKCHAIN_NETWORK` | `simulated_ledger` | Ledger target (`simulated_ledger`, `base_sepolia`, or `local_anvil`). |
| `PROVENANCE_CONTRACT_ADDRESS` | `0x0...` | Smart contract address for anchoring Merkle root state commitments. |

---

## 2. YAML Simulation Configuration Schema (`experiments/configs/default_simulation.yaml`)

```yaml
experiment:
  name: "trust_aware_service_selection_benchmark"
  version: "0.1.0"
  random_seed: 42
  num_tasks: 100
  pre_conditioning_burn_in_rounds: 50

population:
  total_agents: 30
  reliable:
    count: 20
    availability: 0.98
    accuracy: 0.96
    latency_ms_mean: 120
    latency_ms_std: 15
    reputation_min: 0.82
    reputation_max: 0.94
  unreliable:
    count: 5
    availability: 0.80
    timeout_rate: 0.25
    schema_error_rate: 0.20
    latency_ms_median: 330
    reputation_min: 0.45
    reputation_max: 0.68
  malicious:
    count: 5
    sybil_rating_min: 0.93
    sybil_rating_max: 0.99
    poison_on_high_stakes_rate: 0.85
    low_stakes_accuracy: 0.90
    latency_ms_mean: 90

trust_engine:
  sybil_reputation_discount_delta: 0.25
  evidence_confidence_gamma: 0.35
  time_decay_lambda_per_day: 0.0231
  semantic_relevance_threshold: 0.65
  risk_thresholds:
    low: 0.50
    medium: 0.75
    high: 0.90

storage:
  db_path: "experiments/runs/evidence_store.db"
  vector_index_path: "experiments/runs/vector_index.bin"
  batch_commit_size: 50
```
