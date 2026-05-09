# Cursor prompts — tech news agent and outbound call

Copy these into Cursor chat (or your course lab) after MCP and Twilio are configured.

---

## Prompt 1 — Create the agent (no call yet)

Create an agent that makes an outbound call to update someone about recent tech news

- Use a confident, friendly tone — like a helpful colleague
- Deliver updates about the latest in AI, programming, and cybersecurity
- Keep the explanation short, clear, and jargon-free
- Use my voice (female) for the call
- The agent should sound like a tech-savvy friend, not a sales rep
- First message: "Hey, I’ve got some quick tech updates for you — should I go ahead?"

You don’t have to make a call. Create an agent in the ElevenLabs simply

The agent will be created in Eleven Labs.

---

## Prompt 2 — Outbound call (provide your number)

Now make an outbound call to my number, ask for my number

The assistant should ask you for the **phone number** to call, then initiate the call using your ElevenLabs agent and configured Twilio number.

**Reminder**

- Use **E.164** format (e.g. `+91…`, `+1…`).
- Trial accounts may only call **verified** numbers.
