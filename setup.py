from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-x-forwarded-host",
    description="Treat the X-Forwarded-Host header as the Host header",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-x-forwarded-host",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-x-forwarded-host/issues",
        "CI": "https://github.com/simonw/datasette-x-forwarded-host/actions",
        "Changelog": "https://github.com/simonw/datasette-x-forwarded-host/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_x_forwarded_host"],
    entry_points={"datasette": ["x_forwarded_host = datasette_x_forwarded_host"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-x-forwarded-host[test]"],
    python_requires=">=3.6",
)
