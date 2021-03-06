from ez_setup import use_setuptools

from setuptools import setup

use_setuptools()


VERSION = "0.0.1"

setup(
    name="Pyedra",
    version=VERSION,
    description="Implementation of phase function for asteroids in Python",
    long_description=open("README.md").read(),
    author="Milagros Colazo",
    author_email="milirita.colazovinovo@gmail.com",
    url="https://github.com/milicolazo/Pyedra",
    py_modules=["pyedra", "ez_setup"],
    classifiers=["Programming Language :: Python :: 3.8"],
    license="The MIT License",
    install_requires=["numpy", "pandas", "scipy", "attr"],
)
