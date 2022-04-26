from skbuild import setup  # This line replaces 'from setuptools import setup'
import argparse

import io
import os

# Select the python used to call this script as the one we force cmake to use:
import sys

v = sys.version_info

py_version = ".".join([str(v.major), str(v.minor), str(v.micro)])
print(py_version)

setup(
    name="larcv",
    version="1.0.0",
    cmake_source_dir='src/',
    cmake_args=[
        '-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9',
        '-DCMAKE_PYTHON_BINDINGS=True',
        f'-DCMAKE_PYVERSION={py_version}'
    ],
    include_package_data=True,
    author=['Corey Adams',],
    description='Test for pybind11 failure on linux.',
    license='MIT',
    project_urls={
        'Source Code': 'https://github.com/DeepLearnPhysics/larcv3'
    },
    install_requires=[
        'scikit-build',
    ],
    packages=['larcv','src/pybind11'],
)
