# unitTestPython/setup.py
# run: pip install -e .

from setuptools import setup, find_packages

setup(
    name="myunitestproject",
    version="1.1.0",
    packages=find_packages(where="src")+find_packages(where="test"),
    package_dir={
    "": ".",
    "src": "src",
    "test":"test"
    },
)
