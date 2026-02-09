from fastapi import Header, HTTPException, status
from config import get_atlas_api_key


def require_api_key(x_api_key: str | None = Header(default=None)):
    expected_key = get_atlas_api_key()

    # Treat missing config as server misconfiguration, not test failure
    if expected_key is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API key authentication not configured",
        )

    if x_api_key != expected_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
