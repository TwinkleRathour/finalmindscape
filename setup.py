from setuptools import setup, find_packages

setup(
    name="flask_to_django",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Django>=5.2',
    ],
)
