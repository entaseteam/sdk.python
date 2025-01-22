"""Setup configuration for Entase SDK"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="entase-sdk",
    version="1.0",
    author="Entase, Inc.",
    description="Python Development Kit for Entase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/entaseteam/sdk.python",
    project_urls={
        "Documentation": "https://github.com/entaseteam/sdk.python",
        "Bug Tracker": "https://github.com/entaseteam/sdk.python/issues",
        "Source Code": "https://github.com/entaseteam/sdk.python",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
) 