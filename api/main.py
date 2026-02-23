import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import health, research
from api.middleware.logging import logging_middleware


ENV = os.getenv("ENV", "development")

if ENV == "production":
    app = FastAPI(
        title="Atlas Intelligence Agent",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
else:
    app = FastAPI(title="Atlas Intelligence Agent")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # local dev dashboard
        # Add production dashboard domain later
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(logging_middleware)

app.include_router(health.router)
app.include_router(research.router)