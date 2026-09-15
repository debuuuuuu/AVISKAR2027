# Experimental Results & Analysis Framework

> **IMPORTANT: RESEARCH INTEGRITY NOTICE**  
> **Status:** `[EXPERIMENT NOT YET RUN]`  
> In strict accordance with scientific integrity standards, this document contains **NO FABRICATED BENCHMARK NUMBERS OR SYNTHETIC CHARTS**. Below we specify the formal **result schema**, **reporting tables**, **planned statistical tests**, and **interpretation guidelines** that will be populated once physical experiment runs are completed.

---

## 1. Expected Result Schema & Reporting Tables

Upon execution of the controlled simulation testbed (30 agents, 100 tasks, 10 random seeds), empirical results will be populated into the following schema:

### Table 1: Primary Comparative Performance Matrix
*Data to be populated via `src/experiment/metrics.py` post-execution.*

| Selection Strategy | Task Success Rate ($TSR$) $\uparrow$ | Malicious Selection Rate ($MASR$) $\downarrow$ | False Rejection Rate ($FRR$) $\downarrow$ | Verification Overhead ($VCO$) $\downarrow$ | Decision Latency ($SDL$) $\downarrow$ |
|---|---|---|---|---|---|
| **Strategy 1: Random Selection** | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` |
| **Strategy 2: Reputation-Only** | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` |
| **Strategy 3: Evidence-Based** | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` | `[EXPERIMENT NOT RUN]` |

---

## 2. Risk-Tier Breakdown Schema

To analyze performance across varying risk stakes, results will be decomposed by risk tier:

### Table 2: Performance Breakdown by Risk Stakes
| Risk Tier | Task Count | Metric | Random | Reputation-Only | Evidence-Based (Proposed) |
|---|---|---|---|---|---|
| **Low Stakes ($R = 0.20$)** | 40 | $TSR$<br/>$MASR$ | `[NOT RUN]`<br/>`[NOT RUN]` | `[NOT RUN]`<br/>`[NOT RUN]` | `[NOT RUN]`<br/>`[NOT RUN]` |
| **Medium Stakes ($R = 0.50$)** | 35 | $TSR$<br/>$MASR$ | `[NOT RUN]`<br/>`[NOT RUN]` | `[NOT RUN]`<br/>`[NOT RUN]` | `[NOT RUN]`<br/>`[NOT RUN]` |
| **High Stakes ($R = 0.85$)** | 25 | $TSR$<br/>$MASR$ | `[NOT RUN]`<br/>`[NOT RUN]` | `[NOT RUN]`<br/>`[NOT RUN]` | `[NOT RUN]`<br/>`[NOT RUN]` |

---

## 3. Planned Statistical Significance Testing

To rigorously confirm whether observed performance differences between Strategy 3 (Evidence-Based) and Strategy 2 (Reputation-Only) are statistically significant and not artifacts of random task ordering:

1. **Test Type:** Non-parametric **Wilcoxon Signed-Rank Test** across paired runs ($N = 10$ independent random seeds).
2. **Significance Threshold:** $\alpha = 0.05$ (two-tailed).
3. **Primary Hypotheses:**
   - $H_{0,1}: MASR(\mathcal{S}_{\text{evidence}}) \ge MASR(\mathcal{S}_{\text{rep}})$ vs. $H_{1,1}: MASR(\mathcal{S}_{\text{evidence}}) < MASR(\mathcal{S}_{\text{rep}})$
   - $H_{0,2}: TSR(\mathcal{S}_{\text{evidence}}) \le TSR(\mathcal{S}_{\text{rep}})$ vs. $H_{1,2}: TSR(\mathcal{S}_{\text{evidence}}) > TSR(\mathcal{S}_{\text{rep}})$

### Table 3: Statistical Comparison Summary Schema
| Metric Comparison | Mean Difference ($\Delta$) | Wilcoxon Statistic ($W$) | $p$-value | Significant? ($\alpha = 0.05$) |
|---|---|---|---|---|
| $MASR(\mathcal{S}_3) \text{ vs. } MASR(\mathcal{S}_2)$ | `[PENDING RUN]` | `[PENDING RUN]` | `[PENDING RUN]` | `[PENDING RUN]` |
| $TSR(\mathcal{S}_3) \text{ vs. } TSR(\mathcal{S}_2)$ | `[PENDING RUN]` | `[PENDING RUN]` | `[PENDING RUN]` | `[PENDING RUN]` |
| $SDL(\mathcal{S}_3) \text{ vs. } SDL(\mathcal{S}_2)$ | `[PENDING RUN]` | `[PENDING RUN]` | `[PENDING RUN]` | `[PENDING RUN]` |

---

## 4. Interpretation Guidelines

When results become available, the team will interpret findings according to the following scientific criteria:

1. **Validating Resilience ($MASR$):** If $MASR(\mathcal{S}_3)$ is significantly lower than $MASR(\mathcal{S}_2)$, it confirms that task-specific verified evidence successfully overcomes Sybil reputation inflation.
2. **Assessing the Cost of Trust ($SDL$ & $VCO$):** The framework anticipates higher latency ($SDL$) and verification overhead ($VCO$) for Strategy 3 due to RAG vector lookups and sandboxed testing. The central research question is whether this overhead is justified by the reduction in catastrophic high-stakes failures.
3. **Assessing Conservatism ($FRR$):** A high $FRR$ on low-stakes tasks indicates overly aggressive confidence thresholds, pointing to the need for threshold recalibration.
