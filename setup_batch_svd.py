from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup
from setuptools import find_packages
# from setuptools import Extension

exclude_dirs = ("configs", "tests", "scripts", "data", "outputs")

setup(
    name='batch_svd',
    version="0.0.0",
    author="KinglittleQ",
    url="https://github.com/KinglittleQ/torch-batch-svd",
    description="batched version of svd in PyTorch",
    packages=find_packages(exclude=exclude_dirs),
)
