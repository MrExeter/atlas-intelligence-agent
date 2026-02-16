from dotenv import load_dotenv
load_dotenv()

import sys
from pathlib import Path
import os
import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("ATLAS_API_KEY", "test")
    from api.main import app  # import after env set
    return TestClient(app)
