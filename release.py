from setuptools import setup, Extension, find_packages
import os

# Get a list of all .py files in the src/fusionengine directory
py_files = []
for root, dirs, files in os.walk("src/fusionengine"):
    for file in files:
        if file.endswith(".py"):
            module_path = os.path.join(root, file)
            module_name = module_path.replace(os.path.sep, '.')[:-3]
            py_files.append((module_name, module_path))

# Create a list of Extension objects
extensions = [
    Extension(module_name, sources=[module_path])
    for module_name, module_path in py_files
]

setup(ext_modules=extensions, include_package_data=True)
