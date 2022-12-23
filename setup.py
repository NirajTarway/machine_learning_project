from setuptools import setup
from typing import List


def get_requirement_list() -> List[str]:
    with open(REQUIREMENT_FILE) as req_file:
        return req_file.readlines()


PROJECT_NAME = 'Housing Predictor'
VERSION = '0.0.1'
AUTHOR = 'Niraj Tarway'
DESCRIPTION = 'creating a housing price predictor'
PACKAGES = ['housing']
REQUIREMENT_FILE = 'requirements.txt'

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirement_list()
)
