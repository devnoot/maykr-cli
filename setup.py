from setuptools import setup, find_packages

setup(
    name="maykr",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "dm=maykr.cli:main",
        ],
    },
    author="Anthony W. Weed <anthony.w.weed@gmail.com>",
    description="Maykr - Your go to CLI for classic doom modding.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
