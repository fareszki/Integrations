# Discord Send-Message Integration

A platform integration action that posts a message to a Discord channel via the Discord REST API.

## Files

| File | Purpose |
| --- | --- |
| `DisIntegrations/disArbCode.py` | The action code the platform executes |
| `DisIntegrations/input.json` | Input variable schema (`channel_id`, `content`) |
| `DisIntegrations/output.json` | Output variable schema (`message`) |
| `DisIntegrations/test.py` | Local test harness |
| `DisIntegrations/.env.example` | Template for local credentials |

## How it works

The platform injects `requests`, `input_data`, and the decrypted `credential_value` into the snippet's scope, runs it, and reads back a `result` variable:

- **Success:** `{"success": True, "result": {"message": {...}}}`
- **Failure:** `{"success": False, "error": "..."}`

The credential is a bot token (`bot_token`), sent as an `Authorization: Bot <token>` header to `POST /channels/{channel_id}/messages`.

## Running it locally

```bash
cd DisIntegrations
cp .env.example .env      # add your DISCORD_BOT_TOKEN and DISCORD_CHANNEL_ID
pip install requests
python test.py
```

`test.py` mocks the platform's injected scope, executes `disArbCode.py` unmodified, and prints the returned `result`.

## Notes

`.env` holds real secrets and is gitignored — only `.env.example` is committed.
