# Discord Send-Message Integration

A platform integration action that posts a message to a Discord channel via the Discord REST API.

## Files

| File | Purpose |
| --- | --- |
| `Discord_Integration/disArbCode.py` | The action code the platform executes |
| `Discord_Integration/input.json` | Input variable schema (`channel_id`, `content`) |
| `Discord_Integration/output.json` | Output variable schema (`message`) |
| `Discord_Integration/test.py` | Local test harness |
| `Discord_Integration/.env.example` | Template for local credentials |

## How it works

The platform injects `requests`, `input_data`, and the decrypted `credential_value` into the snippet's scope, runs it, and reads back a `result` variable:

- **Success:** `{"success": True, "result": {"message": {...}}}`
- **Failure:** `{"success": False, "error": "..."}`

The credential is a bot token (`bot_token`), sent as an `Authorization: Bot <token>` header to `POST /channels/{channel_id}/messages`.

## Running it locally

```bash
cd Discord_Integration
cp .env.example .env      # add your DISCORD_BOT_TOKEN and DISCORD_CHANNEL_ID
pip install requests
python test.py
```

`test.py` mocks the platform's injected scope, executes `disArbCode.py` unmodified, and prints the returned `result`.

## Notes

`.env` holds real secrets and is gitignored — only `.env.example` is committed.
