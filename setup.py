from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="econ_jp",
    version="0.1.5",
    license="MIT",
    install_requirements=["pandas", "openpyel", "requests"],
    author="HideyukiO",
    author_email="mazarimono@gmail.com",
    url="https://github.com/chomoku/econ_jp",
    description="""This module returns DataFrame of 
    Japanese economic indicators.""",
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
