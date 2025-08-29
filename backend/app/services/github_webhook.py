from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

from .applescript_sender import focus_iterm_tab_session, AppleScriptResult


# Label → (tab_index, session_index)
LABEL_SESSION_MAP: Dict[str, Tuple[int, int]] = {
    "claude": (4, 1),
    "gemini": (4, 3),
    "codex": (4, 4),
}


def _extract_label_name(payload: Dict[str, Any]) -> Optional[str]:
    """Try to extract a single label name from various GitHub event payloads.

    Priority: explicit `label` field (for labeled events), else first matching
    label from `issue.labels` / `pull_request.labels` that exists in our map.
    """
    # Explicit label object (issues, pull_request labeled actions)
    if isinstance(payload.get("label"), dict):
        name = payload["label"].get("name")
        if isinstance(name, str):
            return name.lower()

    # Fallback: scan issue labels
    issue = payload.get("issue") or {}
    pr = payload.get("pull_request") or {}
    for container in (issue, pr):
        labels = container.get("labels") or []
        for lbl in labels:
            nm = (lbl or {}).get("name")
            if isinstance(nm, str) and nm.lower() in LABEL_SESSION_MAP:
                return nm.lower()

    return None


def handle_github_webhook(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Handle GitHub webhook payload and trigger iTerm focus by label.

    Returns a response dict with action taken and result from AppleScript.
    """
    action = payload.get("action")
    event_label = _extract_label_name(payload)

    if not event_label:
        return {
            "ok": False,
            "reason": "No relevant label found in payload",
            "action": action,
        }

    mapping = LABEL_SESSION_MAP.get(event_label)
    if not mapping:
        return {
            "ok": False,
            "reason": f"Label '{event_label}' not mapped",
            "action": action,
        }

    tab_idx, sess_idx = mapping
    result: AppleScriptResult = focus_iterm_tab_session(tab_idx, sess_idx, send_enter=True)

    return {
        "ok": result.ok,
        "label": event_label,
        "tab": tab_idx,
        "session": sess_idx,
        "applescript_app": result.attempted_app,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }

