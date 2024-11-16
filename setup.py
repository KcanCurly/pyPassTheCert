from setuptools import setup, find_packages

setup(
    name="pyPassTheCert",
    version="1.0.0",
    author="KcanCurly",
    description="A simple way to read and write LAPS passwords from linux.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/pyLAPS",
    packages=find_packages(),
    install_requires=[
        "impacket",
        "ldap3",
        "ldapdomaindump",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "PassTheCert=src.passthecert:main",
        ],
    },
)