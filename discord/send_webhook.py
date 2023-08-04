from discord_webhook import DiscordWebhook
import base64
import fusionengine as fusion

def send_discord_webhook(message):
    encoded_webhook_url = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEzNDA1NjMwMzU2MDQ5OTM0MC94YlNQeGhyWC1fQ2F5M0pqenhWLWJ6OUhuUzAtZzVqanVXZzU0OThwR3VTRVg4Y3JzQjZfMUxET0pmUHg0NkRpeXNxag=="  # Replace with the encoded webhook URL
    decoded_webhook = base64.b64decode(encoded_webhook_url.encode()).decode()

    webhook = DiscordWebhook(url=decoded_webhook, content=message)
    response = webhook.execute()

version = fusion.__version__
author = fusion.__author__

message = f"Fusion Engine {version} of package has been released to PyPI by {author}! Check it out at https://pypi.org/project/fusion-engine/{version}"
send_discord_webhook(message)