from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import APIRouter, Header, HTTPException, Request
from fastapi.responses import JSONResponse

from ...services.github_webhook import handle_github_webhook


router = APIRouter(prefix="/webhooks/github", tags=["webhooks", "github"])


@router.post("")
async def github_webhook(
    request: Request,
    x_github_event: Optional[str] = Header(default=None, alias="X-GitHub-Event"),
    x_hub_signature_256: Optional[str] = Header(default=None, alias="X-Hub-Signature-256"),
) -> Dict[str, Any]:
    """Minimal GitHub webhook endpoint.

    Note: Signature verification is currently not enforced. Add secret validation
    if deploying publicly.
    """
    try:
        payload = await request.json()
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {e}")

    result = handle_github_webhook(payload)
    status = 200 if result.get("ok") else 202  # accept but may be no-op
    # echo event type for observability
    result["event"] = x_github_event
    result["signature_present"] = bool(x_hub_signature_256)
    return JSONResponse(content=result, status_code=status)
