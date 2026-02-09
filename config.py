import os


def get_atlas_api_key() -> str | None:
    return os.getenv("ATLAS_API_KEY")


def get_rate_limit_per_minute() -> int:
    return int(os.getenv("RATE_LIMIT_PER_MINUTE", "10"))

