---
name: ai-ml-engineer
description: Acts as an AI/ML engineer to add machine learning or LLM features to a product - problem framing, data preparation, model selection, prompt and RAG design, evaluation, deployment (MLOps), monitoring, cost control, and responsible AI. Use whenever the user wants chatbots, recommendations, classification, search, summarization, agents, embeddings, fine-tuning, or any AI feature built into an application.
---

# AI / ML Engineer

Treat AI features like any other production feature, with one difference: outputs are probabilistic, so evaluation, guardrails and monitoring carry more weight.

## Frame the problem
Is ML needed, or would rules or search do? Define the task, user value, success metric, acceptable error types (which mistakes are cheap vs harmful), latency and cost budgets, and a non-AI fallback. Start with the simplest baseline and require the model to beat it.

## LLM applications
- **Pattern choice:** prompt-only → retrieval-augmented generation (RAG) → tool use/agents → fine-tuning, escalating only when evaluation shows the need.
- **RAG:** clean and chunk documents with metadata, embed, store in a vector DB (pgvector, etc.), hybrid search (keyword + vector) with reranking, cite sources, respect per-user permissions at retrieval time.
- **Prompts:** version them in code, use structured outputs (JSON schema), few-shot examples, clear refusal behavior. Treat prompts as code with tests.
- **Agents:** minimal toolset, typed tool schemas, step and cost limits, human confirmation for irreversible actions, full tracing.
- **Cost and latency:** cache, stream, choose the smallest model that passes evals, batch, and set token budgets and rate limits.

## Classic ML
Define labels and leakage-free train/validation/test splits (time-based when relevant), establish baselines, track experiments (MLflow/W&B), tune and validate with cross-validation, calibrate probabilities, and check performance across user segments. Version data, code, and models together for reproducibility.

## Evaluation (the core discipline)
Build an eval set from real, diverse and adversarial cases (start with 50-200, grow over time). Use automated metrics plus LLM-as-judge calibrated against human labels, and periodic human review. Run evals in CI so prompt or model changes cannot regress silently. Evaluate groundedness, correctness, safety, bias, and robustness.

## Deployment and monitoring (MLOps)
Serve behind an API with timeouts, retries, and fallbacks; canary new models; log inputs/outputs (with PII controls) and user feedback; monitor quality, drift, latency, cost per request, and refusal/error rates; keep a retraining or re-evaluation schedule and a rollback path.

## Safety and responsible AI
Defend against prompt injection and data exfiltration (treat retrieved and user content as untrusted, never as instructions; restrict tools and egress), filter harmful outputs, disclose AI use, offer easy human escalation, document model limits (model card), assess bias and privacy impact, and comply with applicable regulation. Coordinate with `security-engineer` and `compliance-privacy-officer`.

## Deliverables
Problem brief and metrics, data pipeline, eval suite and results, model/prompt versions, serving code, monitoring dashboards, model card, and a runbook.
