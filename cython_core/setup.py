import os

from Cython.Build import cythonize
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
pyx_path = os.path.join(here, "events_core.pyx")

setup(
    name="cython_core",
    ext_modules=cythonize([pyx_path]),
    packages=["cython_core"],
    package_dir={"cython_core": here},
)
