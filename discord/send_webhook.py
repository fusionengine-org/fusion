from discord_webhook import DiscordWebhook
import fusionengine as fusion
from dotenv import load_dotenv
import os

load_dotenv()

version = fusion.__version__
author = fusion.__author__

message = f"Fusion Engine {version} of package has been released to PyPI by {author}! Check it out at https://pypi.org/project/fusion-engine/{version}"

if webhook := os.getenv("FUSION_WEBHOOK"):
    print("Sending webhook...")

    DiscordWebhook(url=webhook, content=message).execute()

    print("Webhook sent!")
    
else:
    print("Discord webhook URL not found in environment variables.")

