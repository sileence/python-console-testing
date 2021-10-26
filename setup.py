"""Setup script for realpython-reader"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="console_testing",
    version="0.1.0",
    description="Basic Python Package to help students write tests for programming exercises that interact with the console",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sileence/python-console-testing",
    author="Duilio Palacios",
    author_email="duilio@styde.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["console_testing"],
    include_package_data=True,
    install_requires=["", ""],
    entry_points={"console_scripts": [""]},
)
