from setuptools import setup, Extension
from Cython.Build import cythonize
import os

package_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "src")

extensions = [
    Extension(
        "fusionengine",
        sources=["src/fusionengine/__init__.py"],
    ),
    Extension(
        "fusionengine.files.body",
        sources=["src/fusionengine/files/body.py"],
    ),
    Extension(
        "fusionengine.files.color",
        sources=["src/fusionengine/files/color.py"],
    ),
    Extension(
        "fusionengine.files.data",
        sources=["src/fusionengine/files/data.py"],
    ),
    Extension(
        "fusionengine.files.debug",
        sources=["src/fusionengine/files/debug.py"],
    ),
    Extension(
        "fusionengine.files.draw",
        sources=["src/fusionengine/files/draw.py"],
    ),
    Extension(
        "fusionengine.files.enums",
        sources=["src/fusionengine/files/enums.py"],
    ),
    Extension(
        "fusionengine.files.event",
        sources=["src/fusionengine/files/event.py"],
    ),
    Extension(
        "fusionengine.files.exceptions",
        sources=["src/fusionengine/files/exceptions.py"],
    ),
    Extension(
        "fusionengine.files.fonts",
        sources=["src/fusionengine/files/fonts.py"],
    ),
    Extension(
        "fusionengine.files.image",
        sources=["src/fusionengine/files/image.py"],
    ),
    Extension(
        "fusionengine.files.imports",
        sources=["src/fusionengine/files/imports.py"],
    ),
    Extension(
        "fusionengine.files.physics",
        sources=["src/fusionengine/files/physics.py"],
    ),
    Extension(
        "fusionengine.files.shape",
        sources=["src/fusionengine/files/shape.py"],
    ),
    Extension(
        "fusionengine.files.storage",
        sources=["src/fusionengine/files/storage.py"],
    ),
    Extension(
        "fusionengine.files.systems",
        sources=["src/fusionengine/files/systems.py"],
    ),
    Extension(
        "fusionengine.files.ui",
        sources=["src/fusionengine/files/ui.py"],
    ),
    Extension(
        "fusionengine.files.vector",
        sources=["src/fusionengine/files/vector.py"],
    ),
    Extension(
        "fusionengine.files.window",
        sources=["src/fusionengine/files/window.py"],
    ),

]


setup(ext_modules=extensions)