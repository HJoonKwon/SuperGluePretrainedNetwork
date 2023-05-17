from setuptools import setup

setup(
    name="spsg",
    packages=["models"],
    version="0.0.0",
    author="J",
    install_requires=open("requirements.txt", "r").read().split("\n"),
)
