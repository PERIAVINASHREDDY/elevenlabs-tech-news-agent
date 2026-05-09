# ElevenLabs tech news voice agent

Documentation and configuration reference for a **Conversational AI** agent that places **outbound calls** and shares short, friendly updates on AI, programming, and cybersecurity.

## What this repo is

- **Config + code** to reproduce the agent: plain-text prompt, first message, a JSON snapshot of deployed IDs, and a Python script that calls ElevenLabs’ **create agent** API.
- The **LLM weights** and **voice model** are **not** in Git—they run in ElevenLabs’ / Google’s cloud. You only store *which* voice ID and LLM name to use, same as in the dashboard.

## Repository layout

| Path | Purpose |
|------|--------|
| [`config/system_prompt.txt`](config/system_prompt.txt) | System prompt (source of truth for behavior) |
| [`config/first_message.txt`](config/first_message.txt) | Opening line the agent speaks |
| [`config/deployed-agent.json`](config/deployed-agent.json) | Voice ID, LLM id, TTS model, existing `agent_id` (metadata) |
| [`scripts/create_agent.py`](scripts/create_agent.py) | `POST /v1/convai/agents/create` using the files above |
| [`requirements.txt`](requirements.txt) | `requests` for the script |
| [`docs/system-prompt.md`](docs/system-prompt.md) | Human-readable copy of the prompt (for diffs in reviews) |

### Recreate the agent from this repo

```powershell
cd elevenlabs-tech-news-agent
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
$env:XI_API_KEY = "your_elevenlabs_api_key"
python scripts/create_agent.py
```

The API returns a **new** `agent_id` each time. Update `config/deployed-agent.json` if you want the snapshot to stay in sync.

The live agent, phone number, and API keys stay in [ElevenLabs](https://elevenlabs.io/) and Twilio—do not commit secrets here.

## Agent summary

| Field | Value |
|--------|--------|
| Name | Tech friend — quick news catch-up |
| Agent ID | `agent_2901kr6yexjbfg4s3bazzcy4kkc6` |
| First message | Hey, I’ve got some quick tech updates for you — should I go ahead? |
| Default voice (premade) | Jessica — `cgSgspJ2msm6clMCkdW9` |
| Language | `en` |
| LLM | `gemini-2.0-flash-001` |

Replace voice with your **Instant Voice Clone** in the ElevenLabs agent settings if you use a custom voice.

## System prompt

See [`docs/system-prompt.md`](docs/system-prompt.md) for the full text to paste or diff when you edit the agent.

## Outbound calling

1. In ElevenLabs, connect a **phone number** (e.g. Twilio) to this agent.
2. Call destinations use **E.164** format (example: `+15551234567`).

**Do not** store personal phone numbers or API keys in this repository.

## API reference

- [Create agent](https://elevenlabs.io/docs/conversational-ai/api-reference/agents/create)
- [Agents overview](https://elevenlabs.io/docs/conversational-ai/overview)

## Legal

ElevenLabs and Twilio terms apply to their services. This repo holds configuration and helper scripts only, not proprietary models.
