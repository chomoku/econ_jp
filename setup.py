from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent


def _requires_from_file(filename):
    return open(this_directory / filename).read().splitlines()


setup(
    name="econ_jp",
    version="0.1.13",
    license="MIT",
    install_requires=_requires_from_file("requirements.txt"),
    author="HideyukiO",
    author_email="mazarimono@gmail.com",
    url="https://github.com/chomoku/econ_jp",
    description="""This module returns DataFrame of 
    Japanese economic indicators.""",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
