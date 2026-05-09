# ElevenLabs tech news voice agent (Project 4)

End-to-end lab: **Cursor** → **ElevenLabs** + **Twilio** → **MCP** → **Conversational AI agent** → **outbound call** with short tech updates (AI, programming, cybersecurity).

## Start here

| Doc | Contents |
|-----|----------|
| **[docs/setup-guide.md](docs/setup-guide.md)** | Full walkthrough: install Cursor, ElevenLabs API key, Twilio number + webhook, import number, MCP `elevenlabs-mcp`, agent creation, outbound call |
| **[docs/agent-prompts.md](docs/agent-prompts.md)** | Exact **Prompt 1** / **Prompt 2** text for Cursor chat |
| **[docs/system-prompt.md](docs/system-prompt.md)** | System prompt + first message (markdown) |
| **[docs/cursor-mcp-elevenlabs.example.json](docs/cursor-mcp-elevenlabs.example.json)** | Placeholder MCP JSON — prefer output of `python -m elevenlabs_mcp ... --print` |

## Quick links (from the lab)

- [Cursor downloads](https://www.cursor.com/downloads)
- Cursor on Windows: [video](https://www.youtube.com/watch?v=4Zz-vqP3nvM)
- Cursor on Mac: [video](https://www.youtube.com/watch?v=YbyxCRBY7uA)
- Cursor on Ubuntu: [gist](https://gist.github.com/evgenyneu/5c5c37ca68886bf1bea38026f60603b6)
- [ElevenLabs Conversational AI](https://elevenlabs.io/app/conversational-ai)
- [Twilio Console](https://console.twilio.com/)
- Twilio → ElevenLabs **inbound** webhook (US example): `https://api.us.elevenlabs.io/twilio/inbound_call`

## What this repo contains

- **Course-style setup** in `docs/setup-guide.md` (no embedded WhatsApp/screenshot binaries; use consoles + videos).
- **Agent behavior** as editable text: `config/system_prompt.txt`, `config/first_message.txt`.
- **Deployed snapshot** (IDs are account-specific): `config/deployed-agent.json`.
- **API helper:** `scripts/create_agent.py` + `requirements.txt` (uses `XI_API_KEY`).
- **MCP install:** `pip install -r requirements-mcp.txt` then follow Step 4 in the setup guide.

The **LLM and TTS models run in the cloud** (ElevenLabs / provider); this repo does not ship model weights.

## Repository layout

| Path | Purpose |
|------|--------|
| [docs/setup-guide.md](docs/setup-guide.md) | Full lab: Cursor, ElevenLabs, Twilio, MCP, calls |
| [docs/agent-prompts.md](docs/agent-prompts.md) | Prompt 1 & 2 for Cursor |
| [docs/cursor-mcp-elevenlabs.example.json](docs/cursor-mcp-elevenlabs.example.json) | MCP example (replace with `--print` output) |
| [config/system_prompt.txt](config/system_prompt.txt) | System prompt source of truth |
| [config/first_message.txt](config/first_message.txt) | Opening line |
| [config/deployed-agent.json](config/deployed-agent.json) | Voice / LLM / agent id metadata |
| [scripts/create_agent.py](scripts/create_agent.py) | `POST /v1/convai/agents/create` |
| [requirements.txt](requirements.txt) | `requests` for `create_agent.py` |
| [requirements-mcp.txt](requirements-mcp.txt) | `elevenlabs-mcp` for Cursor |

## Recreate the agent via API (optional)

```powershell
cd elevenlabs-tech-news-agent
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
$env:XI_API_KEY = "your_elevenlabs_api_key"
python scripts/create_agent.py
```

Each run creates a **new** `agent_id`; update `config/deployed-agent.json` if you want the snapshot to match.

## Security

Do **not** commit API keys, Twilio secrets, or personal phone numbers. Use env vars and Cursor’s secret storage.

## API reference

- [Create agent](https://elevenlabs.io/docs/conversational-ai/api-reference/agents/create)
- [Conversational AI overview](https://elevenlabs.io/docs/conversational-ai/overview)

## Legal

ElevenLabs and Twilio terms apply to their services. This repository is documentation, configuration, and small helper scripts only.
