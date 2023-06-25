import sys
from cx_Freeze import setup, Executable

example = 3

# Dependencies
build_exe_options = {
    "packages": ["sdl2", "sdl2.ext", "pymunk"],
    "include_files": [],  # Add any additional files or data here
}

# Executable definition
executables = [
    Executable("src/example/example" + str(example) + ".py", base=None)  # Specify the correct path to your main.py file
]

# Setup configuration
setup(
    name="YourApplicationName",
    version="1.0",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=executables
)

