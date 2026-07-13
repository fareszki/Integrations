# test_discord.py
import os
import requests


def load_env(path=".env"):
    """Minimal .env loader (no external dependency). Existing os.environ wins."""
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


load_env()

bot_token = os.environ.get("DISCORD_BOT_TOKEN")
channel_id = os.environ.get("DISCORD_CHANNEL_ID")

if not bot_token or bot_token == "YOUR_BOT_TOKEN":
    raise SystemExit("Set DISCORD_BOT_TOKEN in your .env file (see .env.example).")
if not channel_id or channel_id == "YOUR_CHANNEL_ID":
    raise SystemExit("Set DISCORD_CHANNEL_ID in your .env file (see .env.example).")

# 1) Fake what the platform injects at execute time
env = {
    "requests": requests,
    "input_data": {
        "channel_id": channel_id,
        "content": "Hello from a local test 👋",
    },
    "credential_value": {"bot_token": bot_token},
    "credential": {},                                  # the schema; not needed here
    "credential_type": "api_key",
    "action": {"endpoint": "https://discord.com/api/v10"},
}

# 2) Load your snippet exactly as-is and run it the way the platform does
with open("disArbCode.py") as f:
    exec(f.read(), env)

# 3) Read the variable the platform would read
print("result:", env.get("result"))
