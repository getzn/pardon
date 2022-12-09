from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory/"README.md").read_text(encoding='utf-8')

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pardon',
    version='2.0.5',
    python_requires='>=3.8.1, <3.11',
    include_package_data=True,
    install_requires=required,
    description='The Data Transformation and Machine Learning Accelerator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages()
    )
