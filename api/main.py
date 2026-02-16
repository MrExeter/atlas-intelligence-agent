from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api.routes import health, research
from api.middleware.logging import logging_middleware
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Atlas Intelligence Agent")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(logging_middleware)
app.include_router(health.router)
app.include_router(research.router)
