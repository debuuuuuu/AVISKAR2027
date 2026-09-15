# Evaluation Metrics Specification

This document formalizes the **five core evaluation metrics** used to quantitatively compare the selection strategies, establishing formulas, measurement units, data sources, and scientific significance.

---

## 1. Metrics Summary Table

| Metric Name | Symbol | Mathematical Unit | Desirable Direction | Primary Measurement Source |
|---|---|---|---|---|
| **Task Success Rate** | $TSR$ | Percentage ($[0.0, 1.0]$) | $\uparrow$ Higher is better | Result Verification Layer |
| **Malicious-Agent Selection Rate** | $MASR$ | Percentage ($[0.0, 1.0]$) | $\downarrow$ Lower is better | Selection Engine & Agent Ground Truth |
| **False Rejection Rate** | $FRR$ | Percentage ($[0.0, 1.0]$) | $\downarrow$ Lower is better | Selection Gate & Candidate Truth |
| **Verification Cost Overhead** | $VCO$ | Milliseconds (ms) / CPU FLOPs | $\downarrow$ Lower is better | Subprocess Execution Profiler |
| **Selection Decision Latency** | $SDL$ | Milliseconds (ms) | $\downarrow$ Lower is better | Client Wall-Clock Timer |

---

## 2. Metric 1: Task Success Rate ($TSR$)

### 2.1 Formal Definition
The proportion of delegated tasks whose returned execution outputs are verified as correct, safe, and schema-compliant by the Verification Layer.

### 2.2 Mathematical Formula
$$TSR = \frac{\sum_{i=1}^{N_{\text{tasks}}} \mathbb{I}\Big(\text{verdict}(\tau_i) = \text{SUCCESS}\Big)}{N_{\text{tasks}}}$$
where $\mathbb{I}(\cdot)$ is the indicator function, and $N_{\text{tasks}}$ is the total number of task trials in the experimental run.

### 2.3 Why It Matters
Represents the ultimate operational objective of the autonomous client agent. Demonstrates whether the selection strategy reliably delivers functional outcomes.

### 2.4 Collection Procedure
Logged automatically by `src/experiment/metrics.py` upon receiving the structured `VerificationRecord`.

---

## 3. Metric 2: Malicious-Agent Selection Rate ($MASR$)

### 3.1 Formal Definition
The fraction of selection decisions where the engine selects an agent belonging to the malicious/adversarial behavioral class.

### 3.2 Mathematical Formula
$$MASR = \frac{\sum_{i=1}^{N_{\text{tasks}}} \mathbb{I}\Big(S^*(\tau_i) \in \mathcal{A}_{\text{malicious}}\Big)}{N_{\text{tasks}}}$$
where $\mathcal{A}_{\text{malicious}} = \{S_{\text{mal\_01}}, \dots, S_{\text{mal\_05}}\}$.

### 3.3 Why It Matters
Crucial security metric. Directly measures resilience against Sybil reputation laundering and deceptive capability profiles. A strategy with high $TSR$ on low-stakes tasks is dangerous if its $MASR$ is high on high-stakes tasks.

### 3.4 Collection Procedure
Calculated post-run by cross-referencing selected agent IDs against the simulator ground-truth configuration.

---

## 4. Metric 3: False Rejection Rate ($FRR$)

### 4.1 Formal Definition
The proportion of trials where the selection engine outputs `REJECT`, despite the existence of at least one reachable, capable, and reliable service in the candidate pool.

### 4.2 Mathematical Formula
$$FRR = \frac{\sum_{i=1}^{N_{\text{tasks}}} \mathbb{I}\Big(S^*(\tau_i) = \text{REJECT} \wedge \exists S_j \in \mathcal{C}_i : S_j \in \mathcal{A}_{\text{reliable}}\Big)}{N_{\text{tasks}}}$$

### 4.3 Why It Matters
Quantifies excessive risk-aversion. A trust model that rejects all unfamiliar agents achieves zero $MASR$, but renders the agent completely useless (market paralysis). $FRR$ ensures the framework remains practically viable.

### 4.4 Collection Procedure
Tracked by the Selection Engine when a rejection gate triggers.

---

## 5. Metric 4: Verification Cost Overhead ($VCO$)

### 5.1 Formal Definition
The additional computational and wall-clock time required to verify returned task outputs.

### 5.2 Mathematical Formula
$$VCO = \frac{1}{N_{\text{tasks}}} \sum_{i=1}^{N_{\text{tasks}}} \Delta t_{\text{verify}}(\tau_i)$$
where $\Delta t_{\text{verify}}$ is the execution duration of the Verification Layer in milliseconds.

### 5.3 Why It Matters
Measures the computational price of trust. High verification cost undermines the economic justification of delegating tasks to external agents.

### 5.4 Collection Procedure
Captured via high-resolution Python `time.perf_counter_ns()` wrappers around the `verify_result()` function.

---

## 6. Metric 5: Selection Decision Latency ($SDL$)

### 6.1 Formal Definition
The elapsed wall-clock time between the client agent receiving a task and emitting the selection decision $S^*$, encompassing RAG evidence vector retrieval and multi-dimensional trust calculation.

### 6.2 Mathematical Formula
$$SDL = \frac{1}{N_{\text{tasks}}} \sum_{i=1}^{N_{\text{tasks}}} \Big(t_{\text{decision}}(\tau_i) - t_{\text{receive}}(\tau_i)\Big)$$

### 6.3 Why It Matters
Measures decision efficiency. Critical for real-time agentic workflows where multi-second selection pauses are unacceptable.

### 6.4 Collection Procedure
Logged by the `select_service()` orchestrator method for each candidate evaluation cycle.
