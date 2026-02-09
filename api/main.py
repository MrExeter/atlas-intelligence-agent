from fastapi import FastAPI
from api.routes import health, research
from api.middleware.logging import logging_middleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Atlas Intelligence Agent")

app.middleware("http")(logging_middleware)
app.include_router(health.router)
app.include_router(research.router)
