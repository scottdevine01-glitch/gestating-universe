"""
Setup file for Gestating Universe Theory prediction tools.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="gestating-universe",
    version="1.0.0",
    author="Scott Devine",
    author_email="scottdevine01@gmail.com",
    description="Tools for the Gestating Universe Theory of Everything",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scottdevine01/gestating-universe",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gestating-predictions=run_all_predictions:main",
        ],
    },
)
