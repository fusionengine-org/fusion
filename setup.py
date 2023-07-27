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

    def delete_c_files(self, directory):
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".c"):
                    path = os.path.join(root, file)
                    print("removing", path)
                    os.remove(path)

    def run(self):
        removed_dirs = 0
        removed_files = 0

        c_file_dirs = [
            "src/fusionengine",
            "src/fusionengine/files",
        ]
        for dir in c_file_dirs:
            self.delete_c_files(dir)

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

    def run(self):
        os.system("python setup.py clean")
        os.system("python release.py sdist bdist_wheel")
        os.system("python -m twine upload dist/*")
        os.system("python discord/send_webhook.py")

class install(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
        from release import setup_release

        os.system("python release.py")

class install_dev(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system("pip install -e .")

setup(cmdclass={"clean": clean, "release": release, "install": install, "install_dev": install_dev})