# Data Models

These schemas are proposed and should be reconciled with actual implementation.

## Agent

- `agent_id`
- `name`
- `capabilities`
- `identity_metadata`

## Service

- `service_id`
- `provider_id`
- `capabilities`
- `endpoint`
- `status`

## Task

- `task_id`
- `description`
- `required_capabilities`
- `verification_policy`

## Evidence

- `evidence_id`
- `service_id`
- `task_id`
- `source_interaction_id`
- `observed_behaviour`
- `verification_status`
- `timestamp`
- `provenance_reference`
- `integrity_commitment`

## VerificationRecord

- `verification_id`
- `interaction_id`
- `criteria`
- `outcome`
- `timestamp`

## TrustAssessment

- `service_id`
- `task_id`
- `signals`
- `risk_indicators`
- `decision`
- `decision_reason`
