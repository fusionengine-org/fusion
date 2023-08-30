from discord_webhook import DiscordWebhook
import fusionengine as fusion
import os
from dotenv import load_dotenv

load_dotenv()


def send_discord_webhook(message):
    webhook = os.environ.get("DISCORD_WEBHOOK")

    if webhook:
        webhook = DiscordWebhook(url=webhook, content=message)
        webhook.execute()
    else:
        print("Discord webhook URL not found in environment variables.")


version = fusion.__version__
author = fusion.__author__

message = f"Fusion Engine {version} of package has been released to PyPI by {author}! Check it out at https://pypi.org/project/fusion-engine/{version}"

print("Sending webhook...")

send_discord_webhook(message)

print("Webhook sent!")
