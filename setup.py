from setuptools import setup

setup(
    name="updog-py",
    version="0.0.3",
    packages=["updog"],
    install_requires=["psycopg2", "requests", "flask"],
    package_data={"updog": ["docs/source/*"]},
)
