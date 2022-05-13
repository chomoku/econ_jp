from setuptools import setup, find_packages

setup(
    name='econ_jp',
    version='0.1.0',
    license='MIT',
    install_requirements=['pandas'],
    author='HideyukiO',
    author_email='mazarimono@gmail.com',
    url='https://github.com/chomoku/econ_jp',
    description='This module returns DataFrame of Japanese economic indicators.',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ]
)