"""Setup script for realpython-reader"""

# Third party imports
from setuptools import setup

# This call to setup() does all the work
setup(
    name="console_testing",
    packages=["console_testing"],
    version="0.1",
    description="Basic Python Package to help students write tests for programming exercises that interact with the console",
    url="https://github.com/sileence/python-console-testing",
    keywords = ['Console', 'Testing'],
    author="Duilio Palacios",
    author_email="duilio@styde.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    install_requires=["", ""],
    entry_points={"console_scripts": [""]},
)
