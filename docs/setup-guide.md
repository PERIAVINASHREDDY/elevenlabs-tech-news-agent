# Project 4: ElevenLabs — full setup (Cursor, Twilio, MCP, voice agent)

This guide walks from installing **Cursor** through **ElevenLabs**, **Twilio**, **MCP in Cursor**, creating the **tech news agent**, and placing an **outbound call**. Original course screenshots are not bundled here; use the linked videos and the ElevenLabs/Twilio consoles.

---

## Part A — Install Cursor

### Windows

- **Download:** [https://www.cursor.com/downloads](https://www.cursor.com/downloads)
- **Video walkthrough:** [YouTube — Cursor on Windows](https://www.youtube.com/watch?v=4Zz-vqP3nvM)

### Mac

- **Video walkthrough:** [YouTube — Cursor on Mac](https://www.youtube.com/watch?v=YbyxCRBY7uA)

### Ubuntu 24.04

- **Install notes:** [Gist — Cursor on Ubuntu](https://gist.github.com/evgenyneu/5c5c37ca68886bf1bea38026f60603b6)

### Sign-in

Sign up with **Gmail** or **GitHub**. The browser may open for auth; when finished, **return to Cursor** and continue.

---

## Prerequisites (Project 4)

| Requirement | Why |
|-------------|-----|
| **ElevenLabs account** | API and Conversational AI (voice agent, outbound calls). |
| **Twilio account** | Buy a phone number and route voice to ElevenLabs. |
| **Cursor IDE** | Editor + terminal for Python and MCP. |
| **Python 3.10+** | Install MCP package and run helper scripts in this repo. |

**Python install help**

- Windows: [Install Python 3 on Windows](https://www.youtube.com/watch?v=0DQsjE8vMpc)
- Mac: [Install Python on Mac](https://www.youtube.com/watch?v=utVZYVJSTZA)

**Recommended:** create a virtual environment for anything you `pip install`:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

On Mac/Linux: `source .venv/bin/activate`

---

## Step 1 — ElevenLabs API key

1. Open [ElevenLabs Conversational AI](https://elevenlabs.io/app/conversational-ai) and sign in.
2. Click your **profile** (lower left) → **API keys**.
3. Click **Create API Key**.
4. **Turn off** “Restrict key” (or configure restrictions carefully per your security policy).
5. **Copy** the key and store it securely (password manager). You will use it for MCP and optional API scripts.

**Never commit API keys to Git.** This repo’s `.gitignore` ignores `.env` files.

---

## Step 2 — Twilio setup

1. Open [Twilio Console](https://console.twilio.com/) and create an account; verify email/OTP as prompted.
2. **Add and verify** your personal phone number (OTP).
3. Complete onboarding (**Continue**) as shown in Twilio.
4. **Buy a Twilio number** (trial credits often apply):
   - If **Phone Numbers** is not under **Develop**, use **Explore products** → **Super Network** → **Phone Numbers** and pin it.
   - **Develop** → **Phone Numbers** → **Manage** → **Buy a number** → choose number → **Buy** → accept terms in the popup.
5. **Configure the number for ElevenLabs inbound**
   - Open the number → **Configure** (or **Voice** configuration).
   - Under **Voice**, **A call comes in**, set the webhook URL to:

   `https://api.us.elevenlabs.io/twilio/inbound_call`

   If your ElevenLabs account uses another region, check ElevenLabs docs or dashboard for the correct inbound URL (e.g. EU/India residency endpoints).

6. **Save** configuration.

---

## Step 3 — Connect Twilio to ElevenLabs

1. In ElevenLabs: **Conversational AI** → **Phone numbers** → **Import number** → **Twilio**.
2. Add a **label** (e.g. `Tech Updates`).
3. Paste your **Twilio phone number** in the field provided.
4. In Twilio **Account Dashboard**, copy **Account SID** and **Auth Token** (**Account Info**).
5. Paste them into ElevenLabs and complete import.

Your Twilio number is now linked for Conversational AI (inbound/outbound per your plan and agent assignment).

---

## Step 4 — ElevenLabs MCP in Cursor

1. In Cursor, open **Terminal** (`` Ctrl+` `` or **View → Terminal**).
2. Activate your venv (if you use one), then install the MCP server package:

```bash
pip install elevenlabs-mcp
```

3. Print the MCP config snippet (replace with your real key only on your machine):

```bash
python -m elevenlabs_mcp --api-key=YOUR_ELEVENLABS_API_KEY --print
```

4. Copy the **JSON output** from the terminal.
5. In Cursor, open **MCP settings** and merge that JSON into your MCP configuration (often under user settings, e.g. **Cursor Settings → MCP**). A **placeholder** structure is in [`cursor-mcp-elevenlabs.example.json`](cursor-mcp-elevenlabs.example.json); prefer the exact output from `--print`.

6. Restart MCP or Cursor if the new server does not appear.

---

## Step 5 — Create the tech update agent (Cursor chat)

Use the prompts in [`agent-prompts.md`](agent-prompts.md).

**Summary**

- Tone: confident, friendly colleague; **not** salesy.
- Topics: AI, programming, cybersecurity — short, clear, low jargon.
- Voice: female (premade or your clone in ElevenLabs).
- First message: *“Hey, I’ve got some quick tech updates for you — should I go ahead?”*

You can create the agent **in the ElevenLabs UI** or via **MCP / API**. This repo includes [`config/`](../config/) plus [`scripts/create_agent.py`](../scripts/create_agent.py) to recreate the agent from files.

---

## Step 6 — Outbound call to your number

**Prompt idea (in Cursor):** ask the assistant to make an outbound call and **provide your number in E.164** (e.g. `+9180…`, `+1555…`).

**Notes**

1. Twilio trial rules may require the destination to be a **verified** number.
2. Trial calls sometimes show a **short prompt**; follow Twilio’s on-screen steps, then the call connects to your **ElevenLabs agent**.
3. The agent should deliver the **tech update** using your configured voice and system prompt.

**Privacy:** do not commit phone numbers or call logs to this repository.

---

## Repo tools (after accounts work)

| Task | Command / file |
|------|------------------|
| Recreate agent via API | `pip install -r requirements.txt` → set `XI_API_KEY` → `python scripts/create_agent.py` |
| Prompt source files | `config/system_prompt.txt`, `config/first_message.txt` |
| API docs | [Create agent](https://elevenlabs.io/docs/conversational-ai/api-reference/agents/create) |

---

## Legal

Follow [ElevenLabs](https://elevenlabs.io/) and [Twilio](https://www.twilio.com/) terms of service. This guide is for learning and integration testing.
