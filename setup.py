import glob
import os
import shutil
import base64

from discord_webhook import DiscordWebhook
from setuptools import Command, setup
from src.fusionengine import __version__


class clean(Command):
    user_options = []
    CLEAN_DIRS = [
        "./build",
        "./dist",
        *[dir for dir in glob.glob("./**/*.egg-info", recursive=True)],
        *[dir for dir in glob.glob("./**/__pycache__", recursive=True)],
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        removed_dirs = 0
        removed_files = 0
        for dir in self.CLEAN_DIRS:
            dir = os.path.relpath(dir)
            for path in glob.glob(os.path.join(dir, "**/*"), recursive=True):
                print("removing", path)
                removed_files += 1
            for path in glob.glob(dir):
                print("removing", path)
                removed_dirs += 1
            if os.path.exists(dir):
                shutil.rmtree(dir)
        print(f"removed {removed_files} files and {removed_dirs} directories")

class release(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def send_discord_webhook(self, message):
        encoded_url = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEzNDA1NjMwMzU2MDQ5OTM0MC94YlNQeGhyWC1fQ2F5M0pqenhWLWJ6OUhuUzAtZzVqanVXZzU0OThwR3VTRVg4Y3JzQjZfMUxET0pmUHg0NkRpeXNxag=="
        webhook_url = base64.b64decode(encoded_url.encode()).decode()

        webhook = DiscordWebhook(url=webhook_url, content=message)
        response = webhook.execute()

        if response.ok:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")

    def run(self):
        os.system("python setup.py clean")
        os.system("python setup.py sdist bdist_wheel")
        os.system("python -m twine upload dist/*")

        version = __version__
        message = f"A new version {version} of your package has been released to PyPI! Check it out at https://pypi.org/project/fusion-engine/{version}/"
        self.send_discord_webhook(message)  

setup(cmdclass={"clean": clean, "release": release})