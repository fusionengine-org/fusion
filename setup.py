from setuptools import find_packages, setup

with open("requirements.txt", encoding="UTF-8") as f:
    requirements = f.read().split()

setup(
    name = "fusion-engine",
    install_requires = requirements,
    packages = find_packages(where="src"),
    package_dir = {"": "src"},
)
