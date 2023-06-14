import sys
from cx_Freeze import setup, Executable

# Dependencies
build_exe_options = {
    "packages": ["sdl2", "sdl2.ext", "pymunk"],
    "include_files": [],  # Add any additional files or data here
}

# Executable definition
executables = [
    Executable("src/example/example1.py", base=None)  # Specify the correct path to your main.py file
]

# Setup configuration
setup(
    name="YourApplicationName",
    version="1.0",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=executables
)

# Move the built executable to the desired output directory
import os
import shutil

output_dir = "build/output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for executable in executables:
    shutil.move(os.path.join("build", executable.target_name), output_dir)