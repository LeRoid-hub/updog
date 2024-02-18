from setuptools import setup

# Settings for the package to be built
# and uploaded to PyPI
setup(
    name="updog-py",
    version="0.0.3",
    packages=["updog"],
    install_requires=["psycopg2", "requests", "flask"],
    package_data={"updog": ["docs/source/*"]},
)
