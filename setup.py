

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name="Utils_Cuong",
    version="0.0.1",
    author="Cuong Tran",
    author_email="cuongtran73d1@gmail.com",
    description="My utils for AI",
    long_description="For my self",
    long_description_content_type="text/markdown",
    url="https://github.com/mwpnava/Python-Code/tree/master/My_own_Python_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
