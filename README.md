# Atlas Intelligence Agent

Production-grade agentic market intelligence backend built with LangGraph, FastAPI, and RAG.  
Generates executive startup and industry briefs with automated evaluation.

Atlas takes a topic (e.g. “AI developer tools”) and produces a structured market report including:

- Executive summary  
- Market overview  
- Competitive landscape  
- Opportunities  
- Risks  
- Automated evaluation scores  

This project demonstrates a full agentic pipeline — not a chatbot.

This repository is intended as a professional showcase for hiring managers and technical reviewers.

---

## Architectural Principles
- Explicit state machine (LangGraph)
- Parallel research with reducer-based merging
- Strict planner JSON contracts
- Deterministic evaluation policy
- Clear separation of scoring vs decision logic

---

## Features

- LangGraph-based multi-agent orchestration
- Parallel research with concurrency-safe state merging
- Modular RAG boundary
- Automated evaluation with PASS / WARN / FAIL verdicts
- Structured, executive-ready outputs
- FastAPI backend with authentication and rate limiting
- Structured logging and observability-lite metrics
- Secret-safe configuration via environment variables
- Comprehensive, risk-weighted test coverage

---

## Non-Goals (Intentional)

Atlas deliberately does **not** include:
- A chatbot interface
- Real web scraping APIs
- A frontend UI
- Vector database persistence
- Background workers or queues

These omissions are intentional to keep the focus on backend architecture and system correctness.

---

## Current Status

- End-to-end pipeline operational
- Core architecture stabilized
- Security, rate limiting, evaluation, and observability implemented
- Suitable as a portfolio-grade reference implementation
- Future work will focus on reuse of this architecture in subsequent projects rather than expanding scope here.

---

## Tech Stack

- Python 3.11+
- FastAPI
- LangGraph
- LangChain
- OpenAI
- Pytest
- Docker (optional)
