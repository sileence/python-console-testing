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
    name="console-testing",
    version="0.1.0",
    description="Simple console testing for basic Python projects",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Duilio Palacios",
    author_email="duilio@styde.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["", ""],
    entry_points={"console_scripts": [""]},
)
