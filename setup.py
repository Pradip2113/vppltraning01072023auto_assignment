from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in auto_assignment/__init__.py
from auto_assignment import __version__ as version

setup(
	name="auto_assignment",
	version=version,
	description="Auto Shift and Holiday Assignment",
	author="Abhishek Chougule",
	author_email="chouguleabhis@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
