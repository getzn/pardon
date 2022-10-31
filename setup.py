from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pardon',
    version='2.0.0',
    include_package_data=True,
    install_requires=required,
    packages=find_packages()
    )
