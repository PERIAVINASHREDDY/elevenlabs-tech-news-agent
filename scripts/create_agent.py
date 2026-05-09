"""
Create (or recreate) the Conversational AI agent via ElevenLabs HTTP API.

Requires: pip install requests
Environment: XI_API_KEY — your ElevenLabs API key (never commit it).

Docs: https://elevenlabs.io/docs/conversational-ai/api-reference/agents/create
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests

API_URL = "https://api.elevenlabs.io/v1/convai/agents/create"

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config"


def load_text(name: str) -> str:
    return (CONFIG / name).read_text(encoding="utf-8").strip()


def build_body() -> dict:
    system_prompt = load_text("system_prompt.txt")
    first_message = load_text("first_message.txt")
    meta_path = CONFIG / "deployed-agent.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    return {
        "name": meta.get("name", "Tech friend — quick news catch-up"),
        "conversation_config": {
            "tts": {
                "model_id": meta.get("tts_model_id", "eleven_turbo_v2"),
                "voice_id": meta["voice_id"],
                "optimize_streaming_latency": 3,
                "stability": 0.5,
                "similarity_boost": 0.8,
            },
            "agent": {
                "first_message": first_message,
                "language": meta.get("language", "en"),
                "prompt": {
                    "prompt": system_prompt,
                    "llm": meta.get("llm", "gemini-2.0-flash-001"),
                    "temperature": 0.55,
                },
            },
        },
    }


def main() -> int:
    api_key = os.environ.get("XI_API_KEY")
    if not api_key:
        print("Set XI_API_KEY to your ElevenLabs API key.", file=sys.stderr)
        return 1

    body = build_body()
    r = requests.post(
        API_URL,
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
        },
        json=body,
        timeout=120,
    )
    if not r.ok:
        print(r.status_code, r.text, file=sys.stderr)
        return 1

    data = r.json()
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
