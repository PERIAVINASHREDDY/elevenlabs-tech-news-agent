# ElevenLabs tech news voice agent

Documentation and configuration reference for a **Conversational AI** agent that places **outbound calls** and shares short, friendly updates on AI, programming, and cybersecurity.

## What this repo is

- A **spec and checklist** you can version in Git.
- The live agent, phone number, and API keys stay in [ElevenLabs](https://elevenlabs.io/) and Twilio—do not commit secrets here.

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

ElevenLabs and Twilio terms apply to their services. This repo is documentation only.
