'''
This setup.py file is an essential part of packaging and distributing python projects.
It is used by setuptools(or distutils) to define the metadata and dependencies of the project, making it easier to install and manage the project as a package.

'''

from setuptools import find_packages , setup 
from typing import List

def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                # ignore empty lines and '-e .'
                if requirement != '' and not requirement.startswith('-e .'):
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements_list

print(get_requirements())

setup(
    name = "Network-Security-ML",
    version = "0.0.0",
    author="Sumit",
    author_email="sumitr82324@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)