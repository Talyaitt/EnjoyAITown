# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name="ta",
    packages=["ta"],
    version="0.11.0",
    description="Technical Analysis Library in Python",
    install_requires=[
        "numpy",
        "pandas",
    ],
    download_url="https://github.com/bukosabino/ta/tarball/0.11.0",
    keywords=["technical analysis", "python3", "pandas"],
    license="The MIT License (MIT)",
    license_files=["LICENSE"],
    classifiers=[
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Documentation": "https://technical-analysis-library-in-python.readthedocs.io/en/latest/",
        "Bug Reports": "https://github.com/bukosabino/ta/issues",
        "Source": "https://github.com/bukosabino/ta",
    },
)
