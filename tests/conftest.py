from dotenv import load_dotenv
load_dotenv()

import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))


@pytest.fixture
def client():
    from api.main import app

    async def mock_validate_token(request):
        return None

    return TestClient(app)
