# 5-Minute Formal Presentation Script

This document provides a slide-by-slide script for delivering a complete, 5-minute formal academic presentation.

---

## Slide 1: Title & Introduction (0:00 – 0:30)
**Slide Content:** Project Title, Subtitle, Team Roles.  
**Script:**  
"Good morning, members of the jury and distinguished colleagues. Today, we are presenting our research on **'Trust-Aware Service Selection for Autonomous AI Agents: An Evidence-Based Trust and Verification Framework'**.  
As autonomous AI agents evolve from isolated prompt chains into distributed multi-agent networks, they must dynamically discover and invoke external third-party services. However, choosing external services under uncertainty is one of the most critical and unresolved security challenges in modern agentic systems. Our project presents an evidence-grounded framework to solve this problem."

---

## Slide 2: The Problem: The Perils of Open Agent Delegation (0:30 – 1:15)
**Slide Content:** Diagrams of Agent Delegation, Cheap Talk, Sybil Attacks, Halo Effect.  
**Script:**  
"In an open ecosystem, client agents face three profound failure modes:  
First, **cheap talk**: external agents publish self-serving capability cards that cannot be verified before invocation.  
Second, **the Halo Effect**: an agent with high ratings for writing marketing copy might fail catastrophically or inject security backdoors when assigned mathematical optimization or SQL generation.  
Third, **behavioral drift**: an agent that ran reliably during low-stakes tests can silently degrade, timeout, or execute an exit scam on high-stakes tasks."

---

## Slide 3: Existing Empirical Evidence: The ERC-8004 Baseline (1:15 – 2:00)
**Slide Content:** Bar charts of ERC-8004 study (3-15% live endpoints, 59-90% Sybil reviewers).  
**Script:**  
"This problem is not theoretical; it is happening right now. In a landmark 2026 empirical study by Xiong et al. analyzing the ERC-8004 decentralized agent ecosystem on Ethereum, BNB Smart Chain, and Base, the authors discovered that:  
- Only 3% to 15% of registered agents actually had live, working endpoints.  
- And between **59.2% and 90.6% of reviewers were coordinated Sybil bots** engaging in collusive rating rings.  
When those Sybil reviews were removed, public reputation scores collapsed. This proves empirically that global reputation alone cannot support autonomous decision-making."

---

## Slide 4: The Research Question & Solution (2:00 – 2:45)
**Slide Content:** Central Research Question & Six Trust Dimensions.  
**Script:**  
"This motivates our central research question:  
**'Can task-specific, verifiable evidence improve autonomous AI-agent service selection compared with reputation-only scoring?'**  
We propose replacing monolithic star ratings with a multi-dimensional decision model that evaluates six factors:  
**Identity**, **Capability**, **Task-Specific History**, **Evidence Quality**, **Discounted Reputation**, and **Risk Stakes**.  
Rather than treating reputation as the final answer, we treat it as a discounted prior that is rapidly superseded by empirical, verified evidence matching the current task's domain."

---

## Slide 5: System Architecture & Closed-Loop Verification (2:45 – 3:45)
**Slide Content:** High-Level Architecture Diagram (10 Components).  
**Script:**  
"Our system architecture operates as a disciplined closed-loop verification pipeline:  
1. When a task arrives, the client agent extracts the required capability and assesses objective risk stakes.  
2. Using RAG, it retrieves past interaction traces matching the semantic domain vector.  
3. It evaluates candidates against a risk-calibrated confidence threshold. If a task is high-stakes and no candidate has verified history, the agent **safely rejects** execution to prevent damage.  
4. Upon selecting a candidate, it dispatches the request using standardized Model Context Protocol (MCP) tool calls.  
5. Crucially, the returned result is routed through our **Result Verification Layer**, which runs deterministic unit tests in an isolated sandbox.  
6. Verified outcomes update our local evidence store, and a SHA-256 Merkle root is anchored to the blockchain for tamper-evident provenance."

---

## Slide 6: Experimental Methodology & Evaluation (3:45 – 4:30)
**Slide Content:** 30 Agent Population (20/5/5), 3 Strategies, 5 Metrics.  
**Script:**  
"To scientifically test our framework, we built a controlled, reproducible simulation testbed with **30 heterogeneous agents**:  
- 20 Reliable services exhibiting consistent outputs.  
- 5 Unreliable services with latency spikes and timeouts.  
- 5 Malicious services participating in Sybil rating rings and poisoning high-stakes payloads.  
We benchmark 100 sequential tasks across three strategies: **Random Selection**, **Reputation-Only Selection**, and our **Evidence-Based Selection**.  
We measure performance across five formalized metrics: **Task Success Rate**, **Malicious Selection Rate**, **False Rejection Rate**, **Verification Cost Overhead**, and **Decision Latency**."

---

## Slide 7: Research Integrity & Conclusion (4:30 – 5:00)
**Slide Content:** Roadmap, Status Table, GitHub Repository QR Code.  
**Script:**  
"In closing, we uphold strict research integrity: our testbed and schemas are fully specified and deterministic, but we do not report fabricated benchmark numbers until reproducible multi-seed runs are completed.  
By shifting the paradigm from ungrounded global reputation to verified task-specific evidence, we take a vital step toward secure, production-grade autonomous agent economies.  
Thank you, and we look forward to your questions."
