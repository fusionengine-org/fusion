from discord_webhook import DiscordWebhook
import base64
import fusionengine as fusion

def send_discord_webhook(message):
    encoded_webhook_url = ""
    decoded_webhook = base64.b64decode(encoded_webhook_url.encode()).decode()

    webhook = DiscordWebhook(url=decoded_webhook, content=message)
    webhook.execute()

version = fusion.__version__
author = fusion.__author__

message = f"Fusion Engine {version} of package has been released to PyPI by {author}! Check it out at https://pypi.org/project/fusion-engine/{version}"
send_discord_webhook(message)