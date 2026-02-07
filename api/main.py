from fastapi import FastAPI
from api.routes import health, research
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Atlas Intelligence Agent")

app.include_router(health.router)
app.include_router(research.router)
