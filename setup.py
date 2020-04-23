from setuptools import setup, find_packages

setup(
    name="medium",
    packages=find_packages(include="medium"),
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "marshmallow",
    ],
)
