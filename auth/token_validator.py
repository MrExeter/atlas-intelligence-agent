import os
import hashlib
from datetime import datetime, timezone

import boto3
from fastapi import HTTPException, Request


TOKEN_HASH_SALT = os.getenv("TOKEN_HASH_SALT")
AWS_REGION = os.getenv("AWS_REGION", "us-west-1")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME", "atlas_invite_tokens")

if not TOKEN_HASH_SALT:
    raise RuntimeError("TOKEN_HASH_SALT not configured")


dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_TABLE_NAME)


def hash_token(token: str) -> str:
    combined = f"{token}{TOKEN_HASH_SALT}".encode("utf-8")
    return hashlib.sha256(combined).hexdigest()


async def validate_token(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")

    raw_token = auth_header.split(" ")[1]
    token_hash = hash_token(raw_token)

    response = table.get_item(Key={"token_hash": token_hash})
    item = response.get("Item")

    if not item:
        raise HTTPException(status_code=401, detail="Unauthorized")

    if not item.get("is_active", False):
        raise HTTPException(status_code=401, detail="Unauthorized")

    expires_at = datetime.fromisoformat(item["expires_at"])

    if datetime.now(timezone.utc) > expires_at:
        raise HTTPException(status_code=401, detail="Unauthorized")
