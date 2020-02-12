from skbuild import setup  # This line replaces 'from setuptools import setup'
import argparse

import io
import os




setup(
    name="pybind11-test-symbols",
    version="1.0.0",
    cmake_source_dir='src/',
    cmake_args=[
        '-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9',
        '-DCMAKE_PYTHON_BINDINGS=True',
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
)
