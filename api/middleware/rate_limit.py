import time
from collections import defaultdict
from fastapi import Request, HTTPException, status
from config import get_rate_limit_per_minute

_requests: dict[str, list[float]] = defaultdict(list)


def rate_limit(request: Request):
    api_key = request.headers.get("X-API-Key")
    if not api_key:
        return  # auth handles this

    limit = get_rate_limit_per_minute()
    now = time.time()
    window_start = now - 60

    timestamps = _requests[api_key]
    timestamps[:] = [t for t in timestamps if t > window_start]

    if len(timestamps) >= limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded",
        )

    timestamps.append(now)
