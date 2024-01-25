import os

from setuptools import setup, find_packages

base_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(base_path, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name="pinksale-python",
    version="0.1.7",
    packages=find_packages(),
    install_requires=[
        "web3"
    ],
    include_package_data=True,
    url="https://github.com/hkey0/pinksale-python",
    author="hkey",
    description=" The unofficial Python client for the Pinksale.",
    long_description=readme,
    long_description_content_type="text/markdown",
)
