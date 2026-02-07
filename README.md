# Atlas Intelligence Agent

Production-grade agentic market intelligence backend built with LangGraph, FastAPI, and RAG.  
Generates executive startup and industry briefs with automated evaluation.

Atlas takes a topic (e.g. “AI developer tools”) and produces a structured market report including:

- Executive summary  
- Market overview  
- Competitive landscape  
- Opportunities  
- Risks  
- Quality evaluation scores  

This project demonstrates a full agentic pipeline — not a chatbot.

---

## Features

- LangGraph-based multi-agent orchestration
- Planner → parallel research agents → RAG → synthesis → evaluation
- Structured executive output (JSON + markdown-ready)
- Automated quality scoring
- FastAPI backend
- Modular RAG boundary
- Production-style repo layout
- Secret-safe configuration via environment variables
- Designed for AWS deployment

---

## Architecture (High Level)
```
User Topic
↓
Planner Agent
↓
Parallel Research Agents
(news | funding | hiring | competitors)
↓
RAG Retrieval
↓
Synthesizer Agent
↓
Evaluator Agent
↓
Executive Market Brief + Scores

```

---

## Tech Stack

- Python 3.11+
- FastAPI
- LangGraph
- LangChain
- OpenAI
- Docker (optional)
- Redis / Postgres (planned)
---


