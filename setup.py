import os
from distutils.core import setup

from setuptools import find_packages

about_path = os.path.join(os.path.dirname(__file__), "deep_merge/about.py")
exec(compile(open(about_path).read(), about_path, "exec"))


setup(
    name=__name__,  # noqa
    version=__version__,  # noqa
    author=__author__,  # noqa
    author_email=__author_email__,  # noqa
    description=__description__,  # noqa
    url=__url__,  # noqa
    license=__license__,  # noqa
    packages=find_packages(),
    long_description=open('README.md').read(),
    test_suite='nose.collector',
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
