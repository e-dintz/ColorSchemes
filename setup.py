# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 21:48:16 2018

@author: e-dintz
"""

from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'colorschemes/VERSION.txt'), 'r') as f:
    _version = f.read().rstrip()

setup(name='colorschemes',
      version=_version,
      author='Ethan Dintzner',
      description='colorschemes: A package for aesthetically pleasing and colorblindness-friendly color schemes',
      long_description='colorschemes contains a collection of several hundred multicolor palettes from Color Inspirations by Darius A. Monsef IV.',
      packages=[
          'colorschemes',
      ],
      package_data={
		  'colorschemes': ['*.txt'],
      },
      install_requires=[
        'numpy>=2.0.0',
        'matplotlib>=3.0.0',
        ],
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        ],
      )

