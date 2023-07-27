import glob
import os
import sys
import shutil
import base64
import json
import urllib.request

from setuptools import Command, setup


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
        url = base64.b64decode(encoded_url.encode()).decode()

        headers = {
            "Content-Type": "application/json",
        }
        
        payload = {
            "content": message,
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers)
        
        try:
            with urllib.request.urlopen(req) as response:
                response_data = response.read()
                print(response_data.decode())
        except urllib.error.URLError as e:
            print(f"Error occurred: {e}")


    def run(self):
        os.system("python setup.py clean")
        os.system("python release.py sdist bdist_wheel")
        os.system("python -m twine upload dist/*")

        message = "A new version of package has been released to PyPI! Check it out at https://pypi.org/project/fusion-engine/"
        self.send_discord_webhook(message)

class install(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
        from release import setup_release

        setup_release()

class install_dev(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system("pip install -e .")

setup(cmdclass={"clean": clean, "release": release, "install": install, "install_dev": install_dev})