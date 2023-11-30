from setuptools import setup, find_packages

with open("requirements.txt", "r") as file:
    lines = file.readlines()
libs = [each.strip() for each in lines]


setup(name="epicureai", install_requires=libs, packages=find_packages())
