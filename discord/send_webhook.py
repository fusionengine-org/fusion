from discord_webhook import DiscordWebhook
import fusionengine as fusion
import os


def send_discord_webhook(message):
    if webhook := os.environ.get("DISCORD_WEBHOOK"):
        DiscordWebhook(url=webhook, content=message).execute()
    else:
        print("Discord webhook URL not found in environment variables.")


version = fusion.__version__
author = fusion.__author__

message = f"Fusion Engine {version} of package has been released to PyPI by {author}! Check it out at https://pypi.org/project/fusion-engine/{version}"

print("Sending webhook...")

send_discord_webhook(message)

print("Webhook sent!")
