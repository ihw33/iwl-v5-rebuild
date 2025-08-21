from __future__ import annotations

import subprocess
from dataclasses import dataclass
from typing import Optional


@dataclass
class AppleScriptResult:
    ok: bool
    stdout: str
    stderr: str
    attempted_app: str


def _build_applescript(app_name: str, tab_index: int, session_index: int, send_enter: bool) -> str:
    # iTerm(2) AppleScript is 1-based for tabs/sessions
    # We try to select the tab and session, then optionally send an Enter key.
    enter_block = (
        '            try\n'
        '                tell current session to write text ""\n'
        '            on error\n'
        '                tell application "System Events" to key code 36\n'
        '            end try\n'
        if send_enter
        else ""
    )

    return f'''
tell application "{app_name}"
    activate
    if (count of windows) is 0 then
        error "No iTerm window available"
    end if
    tell current window
        if (count of tabs) < {tab_index} then
            error "Tab index out of range"
        end if
        tell tab {tab_index}
            try
                select
            end try
            try
                if (count of sessions) < {session_index} then
                    error "Session index out of range"
                end if
                set targetSession to session {session_index}
                select targetSession
            on error
                try
                    set current session to session {session_index}
                end try
            end try
{enter_block}        end tell
    end tell
end tell
'''


def focus_iterm_tab_session(
    tab_index: int,
    session_index: int,
    send_enter: bool = True,
    timeout: Optional[int] = 5,
) -> AppleScriptResult:
    """Focus a specific iTerm tab/session and optionally send Enter.

    Attempts iTerm2 first, then iTerm for compatibility.
    """
    candidates = ["iTerm2", "iTerm"]

    last_stdout = ""
    last_stderr = ""
    for app in candidates:
        script = _build_applescript(app, tab_index, session_index, send_enter)
        try:
            proc = subprocess.run(
                ["osascript", "-"],
                input=script.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
            )
            if proc.returncode == 0:
                return AppleScriptResult(
                    ok=True,
                    stdout=proc.stdout.decode("utf-8", "ignore"),
                    stderr=proc.stderr.decode("utf-8", "ignore"),
                    attempted_app=app,
                )
            # fall through to next app name
            last_stdout = proc.stdout.decode("utf-8", "ignore")
            last_stderr = proc.stderr.decode("utf-8", "ignore")
        except Exception as e:  # noqa: BLE001
            last_stderr = str(e)

    return AppleScriptResult(
        ok=False,
        stdout=last_stdout,
        stderr=last_stderr or "Failed to execute AppleScript for iTerm(2)",
        attempted_app=candidates[-1],
    )

