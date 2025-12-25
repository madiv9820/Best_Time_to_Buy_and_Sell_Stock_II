from setuptools import Extension, setup
from Cython.Build import cythonize

ext = Extension(
    name = "engine",
    sources = ["engine.pyx"],
    language = "c++"
)

setup(
    ext_modules = cythonize(ext, language_level = 3)
)