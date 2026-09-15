# Experiment Reproducibility Guide

This guide provides exact instructions for reproducing the experimental evaluation from source code, guaranteeing deterministic replicability across different machines and operating systems.

---

## 1. Reproducibility Guarantee & Seed Control

To guarantee scientific replicability:
- All stochastic processes (agent availability, latency jitter, task order, error injection) are governed by explicit integer random seeds.
- The default benchmark uses `seed: 42`.
- Software dependencies are pinned in `requirements.txt`.

---

## 2. Step-by-Step Reproduction Instructions

### Step 1: Environment Setup
```bash
# Clone the repository
git clone https://github.com/your-org/trust-aware-agent-service-selection.git
cd trust-aware-agent-service-selection

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# Install exact dependencies
pip install -r requirements.txt
```

### Step 2: Verify Test Suite
```bash
pytest tests/unit/
pytest tests/integration/
```

### Step 3: Execute Single Benchmark Run (Seed 42)
```bash
python -m src.experiment.runner --config experiments/configs/default_simulation.yaml --seed 42
```
This will:
1. Initialize 30 agents (20 Reliable, 5 Unreliable, 5 Malicious).
2. Execute 100 sequential tasks across Random, Reputation-Only, and Evidence-Based selection.
3. Write trial logs to `experiments/runs/run_seed_42.jsonl`.
4. Generate summary CSV and metric tables in `experiments/results/metrics_seed_42.csv`.

### Step 4: Execute Multi-Seed Statistical Validation (10 Runs)
```bash
python scripts/experiment/run_multi_seed_eval.py --start-seed 42 --runs 10
```
This computes means, standard deviations, and Wilcoxon signed-rank $p$-values across seeds 42–51.

---

## 3. Hardware & Runtime Requirements

- **Operating System:** Windows 10/11, Ubuntu 20.04+, or macOS 12+
- **Python Version:** 3.10, 3.11, or 3.12
- **RAM:** Minimum 4 GB (8 GB recommended for parallel subprocess sandboxes)
- **Execution Time:** ~30 to 60 seconds per 100-task simulation run on modern CPU hardware.
