from __future__ import annotations

from datetime import datetime, timezone
import json
import asyncio
from typing import Any
import contextlib

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .logging import setup_logging
from .api import api_router
from .api.v1 import v1_router
from .api.v1 import health as health_module
from .api.v1 import items as items_module
from .api.v1 import github_webhooks as github_webhooks_module
from .services.ws_manager import ConnectionManager
from .services.metrics import collect_metrics
from .schemas import MetricsPayload, WSUpdate


def create_app() -> FastAPI:
    settings = get_settings()
    setup_logging(settings.log_level)

    app = FastAPI(title=settings.app_name)

    # CORS (customize origins as needed)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Mount API routers
    v1_router.include_router(health_module.router)
    v1_router.include_router(items_module.router)
    v1_router.include_router(github_webhooks_module.router)
    app.include_router(api_router)
    app.include_router(v1_router, prefix="/api")

    @app.get("/api/health", include_in_schema=False)
    async def health_root():
        # Convenience root health to match spec exactly
        return await health_module.health()

    manager = ConnectionManager()

    # WebSocket endpoint: /ws/updates
    @app.websocket("/ws/updates")
    async def websocket_updates(ws: WebSocket) -> None:
        await manager.connect(ws)
        try:
            # initial update
            first = WSUpdate(type="update", data=MetricsPayload(**collect_metrics()))
            await manager.broadcast_text(first.model_dump_json(by_alias=True))
            while True:
                # Keep the connection open; ignore incoming payloads
                try:
                    await asyncio.wait_for(ws.receive_text(), timeout=60.0)
                except asyncio.TimeoutError:
                    # no message; continue to keep connection
                    continue
        except WebSocketDisconnect:
            await manager.disconnect(ws)
        except Exception:
            await manager.disconnect(ws)
            raise

    async def _broadcast_loop():
        while True:
            msg = WSUpdate(type="update", data=MetricsPayload(**collect_metrics()))
            await manager.broadcast_text(msg.model_dump_json(by_alias=True))
            await asyncio.sleep(5)

    @app.on_event("startup")
    async def _on_startup():
        app.state.broadcast_task = asyncio.create_task(_broadcast_loop())

    @app.on_event("shutdown")
    async def _on_shutdown():
        task = getattr(app.state, "broadcast_task", None)
        if task:
            task.cancel()
            with contextlib.suppress(Exception):
                await task

    @app.get("/", include_in_schema=False)
    async def root() -> Any:
        return JSONResponse({"message": f"{settings.app_name} is running"})

    return app


app = create_app()
